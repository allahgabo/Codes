import django_filters
from django.db.models import Max, Min, When, Case
from django.db.models.functions import TruncDate
from django.utils.translation import ugettext_lazy as _
from rest_framework import mixins, serializers
from rest_framework.response import Response
from django_filters.rest_framework import FilterSet

from mysite.att.api import fields
from mysite.att.api.serializers import NoneSerializer
from mysite.att.api.utils_class import ReportUtilGenericViewSet
from mysite.att.api.filters import ReportGenericFilter
from mysite.iclock.models import Transaction
from mysite.att.api.base_serializers import TransactionShowEmployeeExtraInfoSerializer
from mysite.att.utils import short_date_format

class FirstInLastReportSerializer(TransactionShowEmployeeExtraInfoSerializer):
    """
    CREATING API FOR FIRST IN AND LAST OUT 
    """
    emp_code = serializers.CharField(label=_('report_column_empCode'), source='emp__emp_code')
    first_name = serializers.CharField(label=_('report_column_firstName'), source='emp__first_name', allow_null=True)
    dept_name = serializers.CharField(
        label=_('report_column_departmentName'), source='emp__department__dept_name', allow_null=True)
    weekday = fields.WeekdayField(label=_('report_column_attendanceWeekday'), source='att_date')
    att_date = serializers.SerializerMethodField(label=_('report_column_attendanceDate'))
    check_in = fields.TimeField(label=_('report_column_firstIn'), source='first_in')
    check_out = fields.TimeField(label=_('report_column_lastOut'), source='last_out')
    total_time = serializers.SerializerMethodField(label=_('report_column_totalDuration'))

    def get_att_date(self, obj):
        att_date = obj.get('att_date', None)
        if not att_date:
            return ""
        return short_date_format(att_date)

    def get_total_time(self, obj):
        total = ''
        if obj['last_out'] and obj['first_in']:
            total = (obj['last_out'] - obj['first_in']).seconds
            minutes = total // 60
            return '{hour:0>2d}:{minute:0>2d}'.format(hour=minutes // 60, minute=minutes % 60)

        return total

    class Meta:
        model=Transaction
        fields = (
            'emp_code', 'first_name', 'dept_name', 
            'att_date', 'weekday', 'check_in', 'check_out', 'total_time')

class ReportGenericFilter(FilterSet):
    employees = django_filters.CharFilter(method='employee_filter')
    departments = django_filters.CharFilter(method='department_filter')
    areas = django_filters.CharFilter(method='area_filter')
    groups = django_filters.CharFilter(method='group_filter')
    start_date = django_filters.DateFilter(field_name='att_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='att_date', lookup_expr='lte')

    

class FirstInLastReportFilter(ReportGenericFilter):
    start_date = django_filters.DateFilter(field_name='att_date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='att_date', lookup_expr='lte')

    def employee_filter(self, queryset, name, value):
        if not value or str(value) == '-1':
            return queryset
        objs = value.split(',')
        try:
            objs = [int(i) for i in objs if i]
        except ValueError:
            objs = []
        queryset = queryset.filter(emp_id__in=objs)
        return queryset
    
    class Meta:
        model = Transaction
        fields = ['employees', 'departments','start_date', 'end_date']

class FirstInLastReportViewSet(mixins.ListModelMixin, ReportUtilGenericViewSet):
    """
    API FOR FIRST IN AND LAST OUT 

    """
    model = Transaction
    queryset = Transaction.objects.get_queryset()
    filter_class = FirstInLastReportFilter

    serializer_dict = {
        "list": FirstInLastReportSerializer,
       
    }
    summary_fields = ('total_time',)

    def get_queryset(self):
        queryset = super(FirstInLastReportViewSet, self).get_queryset()
        queryset = queryset.annotate(att_date=TruncDate('punch_time'))
        return queryset

    def annotate_queryset(self, queryset):
        from mysite.att.calc.utils import get_punch_states
        punch_state=get_punch_states()
        check_in,check_out=punch_state['check_in'],punch_state['check_out']
        queryset=queryset.annotate(
            att_date=TruncDate('punch_time'),
            weekday=TruncDate('punch_time'),
            total_time=TruncDate('punch_time'),
        )
        queryset = queryset.values(
            'emp_id', 'emp__emp_code', 'emp__first_name', 'emp__gender',
            'emp__department__dept_name','att_date', 'weekday', 'total_time'
        )
        
        queryset=queryset.annotate(
            first_in=Min(Case(When(punch_state=check_in,then='punch_time'))),
            last_out=Max(Case(When(punch_state=check_out,then='punch_time'))),
        ).order_by("emp_id")
        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.annotate_queryset(self.get_queryset()))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)

    def get_serializer_class(self):
        return self.serializer_dict.get(self.action, NoneSerializer)

