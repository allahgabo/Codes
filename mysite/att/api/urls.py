#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Arvin
# datetime: 2018/11/6 14:33
# software: PyCharm
from django.conf.urls import url, include
# from rest_framework import routers
from rest_framework_nested import routers

from mysite.att.api import views
from mysite.att.api import report_views

router = routers.DefaultRouter()

router.register(r'att_rules',
                views.AttRuleViewSet, base_name='att_rules')
router.register(r'attschedules',
                views.AttScheduleViewSet, base_name='att_schedules')
router.register(r'attshifts',
                views.AttShiftViewSet, base_name='att_shifts')
router.register(r'breaktimes',
                views.BreakTimeViewSet, base_name='break_times')
router.register(r'deptattrules',
                views.DeptAttRuleViewSet, base_name='dept_attRules')
router.register(r'holidays',
                views.HolidayViewSet, base_name='holiday')
router.register(r'leaves',
                views.LeaveViewSet, base_name='leaves')
router.register(r'manuallogs',
                views.ManualLogViewSet, base_name='manual_logs')
router.register(r'webpunches',
                views.WebPunchViewSet, base_name='web_punches')
router.register(r'leavegroups',
                views.LeaveGroupViewSet, base_name='leave_groups')
router.register(r'leavegroupdetails',
                views.LeaveGroupDetailViewSet, base_name='leave_group_details')
router.register(r'leaveyearbalances',
                views.LeaveYearBalanceViewSet, base_name='leave_year_balances')
router.register(r'overtimes',
                views.OvertimeViewSet, base_name='overtimes')
router.register(r'trainings',
                views.TrainingViewSet, base_name='trainings')
router.register(r'changeschedules',
                views.ChangeScheduleViewSet, base_name='changeschedules')
router.register(r'report_params',
                views.ReportParamViewSet, base_name='report_params')
router.register(r'report_template',
                views.ReportTemplateViewSet, base_name='report_template')
router.register(r'report_setting',
                views.AttReportSettingViewSet, base_name='report_setting')
router.register(r'calculation',
                views.AttCalculationViewSet, base_name='calculation')
router.register(r'shift_details',
                views.ShiftDetailViewSet, base_name='shift_details')
router.register(r'tempschedules',
                views.TempScheduleViewSet, base_name='temp_schedules')
router.register(r'timeintervals',
                views.TimeIntervalViewSet, base_name='time_intervals')
router.register(r'transactionReport',
                views.TransactionReportViewSet, base_name='transaction_report')
router.register(r'firstLastReport',
                views.FirstLastReportViewSet, base_name='first_last_report')
router.register(r'firstInLastOutReport',
                views.FirstInLastOutReportViewSet, base_name='first_in_last_out_report')

router.register(r'firstlastout',
                views.FirstInLastReportViewSet,base_name='first_in_last_out')

router.register(r'timeCardReport',
                views.TimeCardReportViewSet, base_name='time_card_report')
router.register(r'empScheduleReport',
                views.EmployeeScheduleReportViewSet, base_name='employeeschedule_report1')

router.register(r'appReport',
                report_views.APPReportViewSet, base_name='app_report')

router.register(r'totalTimeCardReportV2',
                report_views.PayloadTimeCardViewSet, base_name='total_time_report_v2')
router.register(r'scheduledPunchReport',
                report_views.PayloadEffectPunchViewSet, base_name='scheduled_punch_report')
router.register(r'punchParingReport',
                report_views.PayloadParingViewSet, base_name='punch_paring')
router.register(r'dailyActivityReport',
                report_views.DailyActivityViewSet, base_name='daily_activity')
router.register(r'dailyOvertimeReport',
                report_views.DailyOvertimeViewSet, base_name='daily_overtime')
router.register(r'dailyLeaveReport',
                report_views.DailyLeaveViewSet, base_name='daily_leave')
router.register(r'dailyLateInReport',
                report_views.DailyLateInViewSet, base_name='daily_late_in')
router.register(r'dailyEarlyOutReport',
                report_views.DailyEarlyOutViewSet, base_name='daily_early_out')
router.register(r'dailyAbsentReport',
                report_views.DailyAbsentViewSet, base_name='daily_absent')
router.register(r'dailyExceptionReport',
                report_views.DailyExceptionViewSet, base_name='daily_exception')
router.register(r'weeklyWorkedHoursReport',
                report_views.WeeklyWorkedHoursViewSet, base_name='weekly_worked_hours')
router.register(r'weeklyOvertimeReport',
                report_views.WeeklyOvertimeViewSet, base_name='weekly_overtime')
router.register(r'employeeOvertimeReport',
                report_views.EmployeeOvertimeViewSet, base_name='employee_overtime')
router.register(r'employeeLeaveReport',
                report_views.EmployeeLeaveViewSet, base_name='employee_leave')

router.register(r'empSummaryReport',
                report_views.EmployeeSummaryViewSet, base_name='emp_summary_report')
router.register(r'departmentSummaryReport',
                report_views.DepartmentSummaryViewSet, base_name='department_summary_report')
router.register(r'groupSummaryReport',
                report_views.GroupSummaryViewSet, base_name='group_summary')
router.register(r'monthlyStatusReport',
                report_views.MonthlyStatusReportViewSet, base_name='monthly_status')
router.register(r'monthlyWorkHoursReport',
                report_views.MonthlyWorkHoursReportViewSet, base_name='monthly_work_hours')
router.register(r'monthlyPunchReport',
                report_views.MonthlyPunchReportViewSet, base_name='monthly_punch')
router.register(r'monthlyOvertimeReport',
                report_views.MonthlyOvertimeReportViewSet, base_name='monthly_overtime')
router.register(r'monthlyAbsenceReport',
                report_views.MonthlyAbsenceReportViewSet, base_name='monthly_absence')
router.register(r'departmentOvertimeReport',
                report_views.DepartmentOvertimeViewSet, base_name='department_overtime')
router.register(r'groupOvertimeReport',
                report_views.GroupOvertimeViewSet, base_name='group_overtime')

router.register(r'dailyMultiplePunchParingReport',
                report_views.DailyMultiplePunchParingViewSet, base_name='daily_multiple_punch_paring')
router.register(r'dailyMultipleBreakParingReport',
                report_views.DailyMultipleBreakParingViewSet, base_name='daily_multiple_break_paring')
router.register(r'sageVIPReport',
                report_views.SageVIPViewSet, base_name='sage_vip')

router.register(r'leaveBalanceSummaryReport',
                report_views.LeaveBalanceSummaryViewSet, base_name='leave_balance_summary_report')

v1_router = routers.DefaultRouter()
v1_router.register(r'att_groups', views.AttGroupViewSet, base_name='att_groups')
group_nested_router = routers.NestedSimpleRouter(v1_router, r'att_groups', lookup='att_group')
group_nested_router.register(r'employees', views.AttGroupEmployeeViewSet, base_name='att_group_employees')
v1_router.register(r'manual_logs', views.ManualLogViewSet, base_name='att_manual_log')
v1_router.register(r'leaves', views.LeaveViewSet, base_name='att_leave')
v1_router.register(r'overtimes', views.OvertimeViewSet, base_name='att_overtime')
v1_router.register(r'trainings', views.TrainingViewSet, base_name='att_training')
v1_router.register(r'change_schedules', views.ChangeScheduleViewSet, base_name='att_change_schedule')
v1_router.register(r'leave_groups', views.LeaveGroupViewSet, base_name='att_leave_group')
manual_log_router = routers.NestedSimpleRouter(v1_router, r'manual_logs', lookup='instance')
manual_log_router.register(r'node_instances', views.ManualLogNodeInstanceViewSet,
                           base_name='att_manual_log_node_instances')
leave_router = routers.NestedSimpleRouter(v1_router, r'leaves', lookup='instance')
leave_router.register(r'node_instances', views.LeaveNodeInstanceViewSet,
                      base_name='att_leave_node_instances')
overtime_router = routers.NestedSimpleRouter(v1_router, r'overtimes', lookup='instance')
overtime_router.register(r'node_instances', views.OvertimeNodeInstanceViewSet,
                         base_name='att_overtime_node_instances')
training_router = routers.NestedSimpleRouter(v1_router, r'trainings', lookup='instance')
training_router.register(r'node_instances', views.TrainingNodeInstanceViewSet,
                         base_name='att_training_node_instances')
change_schd_router = routers.NestedSimpleRouter(v1_router, r'change_schedules', lookup='instance')
change_schd_router.register(r'node_instances', views.ChangeScheduleNodeInstanceViewSet,
                            base_name='att_change_schedule_node_instances')

leave_group_employee_router = routers.NestedSimpleRouter(v1_router, r'leave_groups', lookup='instance')
leave_group_employee_router.register(r'employees', views.LeaveGroupEmployeeViewSet, base_name='leave_group_employees')

att_api_docs_urls = [url(r'^', include(router.urls)), ]

urlpatterns = [
    url(r'^v1.0/', include(v1_router.urls)),
    url(r'^v1.0/', include(group_nested_router.urls)),
    url(r'^v1.0/', include(manual_log_router.urls)),
    url(r'^v1.0/', include(leave_router.urls)),
    url(r'^v1.0/', include(overtime_router.urls)),
    url(r'^v1.0/', include(training_router.urls)),
    url(r'^v1.0/', include(change_schd_router.urls)),
    url(r'^v1.0/', include(leave_group_employee_router.urls)),
    url(r'^', include(router.urls)),
]
