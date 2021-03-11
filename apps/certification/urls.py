from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('employee_list/', login_required(get_employee_list), name='employee_list'),
    path('get_employee_form/', login_required(get_employee_form), name='get_employee_form'),
    path('get_employee_update_form/', login_required(get_employee_update_form), name='get_employee_update_form'),
    path('save_person/', login_required(save_person), name='save_person'),
    path('update_person/', login_required(update_person), name='update_person'),
    # report
    path('report/', login_required(get_report), name='report'),
    # course
    path('course_list/', login_required(get_course_list), name='course_list'),
    path('get_course_form/', login_required(get_course_form), name='get_course_form'),
    path('save_course/', login_required(save_course), name='save_course'),
    path('update_course/', login_required(update_course), name='update_course'),
    path('get_course_update_form/', login_required(get_course_update_form), name='get_course_update_form'),
    # programming
    path('programming_list/', login_required(get_programming_list), name='programming_list'),
    path('programming_form/', login_required(get_programming_form), name='programming_form'),
    path('save_programming/', login_required(save_programming), name='save_programming'),
    path('programming_grid_list/', login_required(get_programming_grid_list), name='programming_grid_list'),
    path('programming_grid_list_by_course/', login_required(get_programming_grid_list_by_course),
         name='programming_grid_list_by_course'),
    path('get_modal_programming_add/', login_required(get_modal_programming_add), name='get_modal_programming_add'),
    path('add_programming_detail/', login_required(add_programming_detail), name='add_programming_detail'),
    path('get_programming_update_form/', login_required(get_programming_update_form),
         name='get_programming_update_form'),
    path('update_programming/', login_required(update_programming), name='update_programming'),
    path('delete_programming_detail/', login_required(delete_programming_detail), name='delete_programming_detail'),
    # certification
    path('certification_list/', login_required(get_certification_list), name='certification_list'),
]
