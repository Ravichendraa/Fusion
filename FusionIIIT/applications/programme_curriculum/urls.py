from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'programme_curriculum'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.programme_curriculum, name='programme_curriculum'),

    path('programmes/', views.view_all_programmes, name='view_all_programmes'),
    path('working_curriculums/', views.view_all_working_curriculums, name='view_all_working_curriculums'),
    path('curriculums/<programme_id>/', views.view_curriculums_of_a_programme, name='view_curriculums_of_a_programme'),
    path('curriculum_semesters/<curriculum_id>/', views.view_semesters_of_a_curriculum, name='view_semesters_of_a_curriculum'),
    path('semester/<semester_id>/', views.view_a_semester_of_a_curriculum, name='view_a_semester_of_a_curriculum'),
    path('courseslot/<courseslot_id>/', views.view_a_courseslot, name='view_a_courseslot'),
    path('courses/', views.view_all_courses, name='view_all_courses'),
    path('course/<course_id>/', views.view_a_course, name='view_a_course'),
    path('disciplines/', views.view_all_discplines, name='view_all_discplines'),
    path('batches/', views.view_all_batches, name='view_all_batches'),

    path('admin_programmes/', views.admin_view_all_programmes, name='admin_view_all_programmes'),
    path('admin_working_curriculums/', views.admin_view_all_working_curriculums, name='admin_view_all_working_curriculums'),
    path('admin_curriculums/<programme_id>/', views.admin_view_curriculums_of_a_programme, name='admin_view_curriculums_of_a_programme'),
    path('admin_curriculum_semesters/<curriculum_id>/', views.admin_view_semesters_of_a_curriculum, name='admin_view_semesters_of_a_curriculum'),
    path('admin_semester/<semester_id>/', views.admin_view_a_semester_of_a_curriculum, name='admin_view_a_semester_of_a_curriculum'),
    path('admin_courseslot/<courseslot_id>/', views.admin_view_a_courseslot, name='admin_view_a_courseslot'),
    path('admin_courses/', views.admin_view_all_courses, name='admin_view_all_courses'),
    path('admin_course/<course_id>/', views.admin_view_a_course, name='admin_view_a_course'),
    path('admin_disciplines/', views.admin_view_all_discplines, name='admin_view_all_discplines'),
    path('admin_batches/', views.admin_view_all_batches, name='admin_view_all_batches'),
    
    path('admin_add_programme/', views.add_programme_form, name='add_programme_form'),
    path('admin_add_discipline/', views.add_discipline_form, name='add_discipline_form'),
    path('admin_add_curriculum/', views.add_curriculum_form, name='add_curriculum_form'),
    path('admin_add_course/', views.add_course_form, name='add_course_form'),
    path('admin_add_courseslot/', views.add_courseslot_form, name='add_courseslot_form'),
    path('admin_add_course/', views.add_course_form, name='add_course_form'),
    path('admin_add_batch/', views.add_batch_form, name='add_batch_form'),

    path('admin_update_course/<course_id>/', views.update_course_form, name='update_course_form'),
    path('admin_edit_curriculum/<curriculum_id>/', views.edit_curriculum_form, name='edit_curriculum_form'),
    path('admin_edit_programme/<programme_id>/', views.edit_programme_form, name='edit_programme_form'),
    path('admin_edit_courseslot/<courseslot_id>/', views.edit_courseslot_form, name='edit_courseslot_form'),
    path('admin_delete_courseslot/<courseslot_id>/', views.delete_courseslot, name='delete_courseslot'),
    path('admin_edit_batch/<batch_id>/', views.edit_batch_form, name='edit_batch_form'),
    path('admin_edit_discipline/<discipline_id>/', views.edit_discipline_form, name='edit_discipline_form'),
    path('admin_instigate_semester/<semester_id>/', views.instigate_semester, name='instigate_semester'),
    path('admin_replicate_curriculum/<curriculum_id>/', views.replicate_curriculum, name='replicate_curriculum'),
    
    
    
    #new
    path('course_proposal_form/',views.course_proposal_form,name='course_proposal_form'),
    path('view_course_proposal_forms/',views.view_course_proposal_forms,name='view_course_proposal_forms'),
    path('update_course_proposal_form/<course_id>/',views.update_course_proposal_form,name='update_course_proposal_form'),
    path('faculty_view_all_courses/', views.faculty_view_all_courses, name='faculty_view_all_courses'),
    path('faculty_view_a_course/<course_id>/',views.faculty_view_a_course,name="faculty_view_a_course"),
    # path('hod_view_all_courses/', views.hod_view_all_courses, name='faculty_view_all_courses'),
    # path('hod_view_a_course/<course_id>/',views.hod_view_a_course,name="faculty_view_a_course"),
    # path('course_proposal_form/', views.course_proposal_form, name='course_proposal_form'),
    # path('view_course_proposal_forms/', views.view_course_proposal_forms, name='view_course_proposal_forms'),
    path('head_view_a_course_proposal/<CourseProposal_id>/', views.head_view_a_course_proposal, name='head_view_a_course_proposal'),
    path('head_view_a_update_course_proposal/<UpdateCourseProposal_id>/', views.head_view_a_update_course_proposal, name='head_view_a_update_course_proposal'),
    
    path('forward_form/<CourseProposal_id>', views.forward_form, name='forward_form'),
    path('reject_form/<CourseProposal_id>', views.reject_form, name='reject_form'),
    path('approve_form/<CourseProposal_id>', views.approve_form, name='approve_form'),
    
    path('forward_update_form/<UpdateCourseProposal_id>/', views.forward_update_form, name='forward_update_form'),
    path('reject_update_form/<UpdateCourseProposal_id>', views.reject_update_form, name='reject_update_form'),
    path('approve_update_form/<UpdateCourseProposal_id>', views.approve_update_form, name='approve_update_form'),
    
    
    path('admin_view_course_proposal_forms/', views.admin_view_course_proposal_forms, name='admin_view_course_proposal_forms'),
    path('admin_view_a_course_proposal/<CourseProposal_id>/', views.admin_view_a_course_proposal, name='admin_view_a_course_proposal'),
    path('admin_view_a_update_course_proposal/<UpdateCourseProposal_id>/', views.admin_view_a_update_course_proposal, name='admin_view_a_update_course_proposal')
    
]
