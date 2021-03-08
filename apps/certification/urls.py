from django.urls import path, include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('employee_list/', login_required(get_employee_list), name='employee_list'),
    path('get_employee_form/', login_required(get_employee_form), name='get_employee_form'),
    path('get_employee_update_form/', login_required(get_employee_update_form), name='get_employee_update_form'),
    path('save_person/', login_required(save_person), name='save_person'),
    path('update_person/', login_required(update_person), name='update_person'),
    # path('get_employee_by_id/', login_required(get_employee_by_id), name='get_employee_by_id'),
    # path('update_subsidiary_employee/', login_required(update_subsidiary_employee), name='update_subsidiary_employee'),
    # # user
    # path('get_create_user/', login_required(get_create_user), name='get_create_user'),
    # path('get_update_user/', login_required(get_update_user), name='get_update_user'),
    # chart
    path('report/', login_required(get_report), name='report'),
    # course
    path('course_list/', login_required(get_course_list), name='course_list'),
    path('get_course_form/', login_required(get_course_form), name='get_course_form'),
]