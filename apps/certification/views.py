import decimal
from datetime import datetime
from http import HTTPStatus
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.template import loader
from apps.certification.models import Person, Business, Course, Programming


class Home(TemplateView):
    template_name = 'index.html'


def get_report(request):
    return render(request, 'certification/charts.html', {
    })


# lista de empleados
def get_employee_list(request):
    if request.method == 'GET':
        employee_set = Person.objects.all()
        my_date = datetime.now()
        date_now = my_date.strftime("%Y-%m")
        return render(request, 'certification/employee_list.html', {
            'date_now': date_now,
            'employee_set': employee_set,
        })


# abrir el formulario de registro
def get_employee_form(request):
    if request.method == 'GET':
        my_date = datetime.now()
        date_now = my_date.strftime("%Y-%m-%d")
        business_set = Business.objects.all()
        t = loader.get_template('certification/employee_form.html')
        c = ({
            'date_now': date_now,
            'type': Person._meta.get_field('type').choices,
            'business_set': business_set,
        })
        return JsonResponse({
            'form': t.render(c, request),
        })


#
# # registrar empleado
@csrf_exempt
def save_person(request):
    if request.method == 'POST':
        user_id = request.user.id
        user_obj = User.objects.get(id=int(user_id))
        _document = request.POST.get('document', '')
        _paternal_last_name = request.POST.get('paternal', '')
        _maternal_last_name = request.POST.get('maternal', '')
        _names = request.POST.get('names', '')
        _birth_date = request.POST.get('birth_date', '')
        _occupation = request.POST.get('occupation', '')
        _telephone = request.POST.get('telephone', '')
        _email = request.POST.get('email', '')
        _address = request.POST.get('address', '')
        _state = bool(request.POST.get('checkbox', ''))
        _business_id = request.POST.get('business', '')
        business_obj = Business.objects.get(id=int(_business_id))
        try:
            _photo = request.FILES['customFile']
        except Exception as e:
            _photo = 'person/employee0.jpg'

        person_obj = Person(
            document=_document,
            paternal_last_name=_paternal_last_name,
            maternal_last_name=_maternal_last_name,
            names=_names,
            birth_date=_birth_date,
            telephone=_telephone,
            email=_email,
            address=_address,
            type=_occupation,
            is_state=_state,
            photo=_photo,
            business=business_obj,
            user=user_obj,
        )
        person_obj.save()
        return JsonResponse({
            'message': True,
            'resp': 'Se registro exitosamente',
        }, status=HTTPStatus.OK)


#
# # renderizar datos del empleado
# def get_employee_by_id(request):
#     if request.method == 'GET':
#         pk = request.GET.get('pk', '')
#         employee_obj = Person.objects.get(id=pk)
#         subsidiary_set = Subsidiary.objects.all()
#         t = loader.get_template('hrm/employee_subsidiary.html')
#         c = ({
#             'employee_obj': employee_obj,
#             'subsidiary_set': subsidiary_set,
#         })
#         return JsonResponse({
#             'success': True,
#             'form': t.render(c, request),
#         })

#
# # actualizar sucursal del empleado
# @csrf_exempt
# def update_subsidiary_employee(request):
#     if request.method == 'POST':
#         _id = int(request.POST.get('pk', ''))
#         employee_obj = Employee.objects.get(id=_id)
#         _id_subsidiary = int(request.POST.get('subsidiary', ''))
#         subsidiary_obj = Subsidiary.objects.get(id=_id_subsidiary)
#         employee_obj.subsidiary = subsidiary_obj
#         employee_obj.save()
#         return JsonResponse({
#             'success': True,
#         }, status=HTTPStatus.OK)


# # renderizar datos para la creacion de trabajo-usuario
# def get_create_user(request):
#     if request.method == 'GET':
#         pk = request.GET.get('pk', '')
#         employee_obj = Employee.objects.get(id=pk)
#         my_date = datetime.now()
#         date_now = my_date.strftime("%Y-%m-%d")
#         t = loader.get_template('hrm/create_user.html')
#         c = ({
#             'employee_obj': employee_obj,
#             'date_now': date_now,
#         })
#         return JsonResponse({
#             'success': True,
#             'form': t.render(c, request),
#         })
#
#
# # renderizar datos para la actualizacion de trabajo-usuario
# def get_update_user(request):
#     if request.method == 'GET':
#         pk = int(request.GET.get('pk', ''))
#         user_obj = User.objects.get(id=pk)
#         employee_obj = Employee.objects.get(user=user_obj)
#         my_date = datetime.now()
#         date_now = my_date.strftime("%Y-%m-%d")
#         t = loader.get_template('hrm/update_user.html')
#         c = ({
#             'employee_obj': employee_obj,
#             'date_now': date_now,
#         })
#         return JsonResponse({
#             'success': True,
#             'form': t.render(c, request),
#         })
#
#
# renderizar datos para la actualizacion de trabajo-usuario
def get_employee_update_form(request):
    if request.method == 'GET':
        pk = int(request.GET.get('pk', ''))
        person_obj = Person.objects.get(id=pk)
        business_set = Business.objects.all()
        t = loader.get_template('certification/employee_update_form.html')
        c = ({
            'person_obj': person_obj,
            'type': Person._meta.get_field('type').choices,
            'business_set': business_set,
        })
        return JsonResponse({
            'success': True,
            'form': t.render(c, request),
        })


# Actualizacion persona
@csrf_exempt
def update_person(request):
    if request.method == 'POST':
        _id = int(request.POST.get('pk', ''))
        person_obj = Person.objects.get(id=_id)
        _document = request.POST.get('document', '')
        _paternal_last_name = request.POST.get('paternal', '')
        _maternal_last_name = request.POST.get('maternal', '')
        _names = request.POST.get('names', '')
        _birth_date = request.POST.get('birth_date', '')
        _occupation = request.POST.get('occupation', '')
        _telephone = request.POST.get('telephone', '')
        _email = request.POST.get('email', '')
        _address = request.POST.get('address', '')
        _business_id = request.POST.get('business', '')
        business_obj = Business.objects.get(id=int(_business_id))
        _photo = request.FILES.get('customFile', False)
        _state = bool(request.POST.get('checkbox', ''))

        person_obj.document = _document
        person_obj.birth_date = _birth_date
        person_obj.paternal_last_name = _paternal_last_name
        person_obj.maternal_last_name = _maternal_last_name
        person_obj.names = _names
        person_obj.type = _occupation
        person_obj.telephone = _telephone
        person_obj.email = _email
        person_obj.address = _address
        person_obj.business = business_obj
        if _photo is not False:
            person_obj.photo = _photo
        person_obj.is_state = _state
        person_obj.save()
        return JsonResponse({
            'success': True,
        }, status=HTTPStatus.OK)


# lista de cursos
def get_course_list(request):
    if request.method == 'GET':
        course_set = Course.objects.all()
        return render(request, 'certification/course_list.html', {
            'course_set': course_set,
        })


# abrir el formulario de registro
def get_course_form(request):
    if request.method == 'GET':
        t = loader.get_template('certification/register_course_form.html')
        c = ({
            'date_now': '-',
        })
        return JsonResponse({
            'form': t.render(c, request),
        })


@csrf_exempt
def save_course(request):
    if request.method == 'POST':
        _code = request.POST.get('id-code', '')
        _name = request.POST.get('id-name', '')
        _description = request.POST.get('id-description', '')
        _state = bool(request.POST.get('checkbox', ''))

        course_obj = Course(
            code=_code,
            name=_name,
            description=_description,
            is_state=_state,
        )
        course_obj.save()
        return JsonResponse({
            'message': True,
        }, status=HTTPStatus.OK)


@csrf_exempt
def update_course(request):
    if request.method == 'POST':
        pk = request.POST.get('id-pk', '')
        course_obj = Course.objects.get(id=int(pk))
        _code = request.POST.get('id-code', '')
        _name = request.POST.get('id-name', '')
        _description = request.POST.get('id-description', '')
        _state = bool(request.POST.get('checkbox', ''))
        course_obj.code = _code
        course_obj.name = _name
        course_obj.description = _description
        course_obj.is_state = _state
        course_obj.save()
        return JsonResponse({
            'success': True,
        }, status=HTTPStatus.OK)


def get_course_update_form(request):
    if request.method == 'GET':
        id_pk = int(request.GET.get('pk', ''))
        course_obj = Course.objects.get(id=id_pk)
        t = loader.get_template('certification/update_course_form.html')
        c = ({
            'course_obj': course_obj,
        })
        return JsonResponse({
            'success': True,
            'form': t.render(c, request),
        })


def get_programming_list(request):
    if request.method == 'GET':
        course_set = Course.objects.all()
        my_date = datetime.now()
        date_now = my_date.strftime("%Y-%m-%d")
        return render(request, 'certification/programming_list.html', {
            'course_set': course_set,
            'date_now': date_now,
        })


def get_programming_form(request):
    if request.method == 'GET':
        my_date = datetime.now()
        date_now = my_date.strftime("%Y-%m-%d")
        time_now = my_date.strftime("%H:%m")
        course_set = Course.objects.all()
        person_set = Person.objects.filter(type='2', is_state=True)
        t = loader.get_template('certification/register_programming.html')
        c = ({
            'person_set': person_set,
            'course_set': course_set,
            'date_now': date_now,
            'time_now': time_now,
            'state': Programming._meta.get_field('state').choices,
        })
        return JsonResponse({
            'success': True,
            'form': t.render(c, request),
        })


@csrf_exempt
def save_programming(request):
    if request.method == 'POST':
        _course_pk = request.POST.get('id-course-reg', '')
        course_obj = Course.objects.get(id=int(_course_pk))
        _person_pk = request.POST.get('id-person-reg', '')
        person_obj = Person.objects.get(id=int(_person_pk))
        _date_start = request.POST.get('id-start-date', '')
        _date_end = request.POST.get('id-end-date', '')
        _hour = int(request.POST.get('id-hour', ''))
        _price = decimal.Decimal(request.POST.get('id-price', ''))
        _quantity = int(request.POST.get('id-quantity', ''))
        _observation = request.POST.get('id-observation', '')
        _state = request.POST.get('id-state', '')

        programming_obj = Programming(
            course=course_obj,
            person=person_obj,
            start_date=_date_start,
            end_date=_date_end,
            course_price=_price,
            vacancies=_quantity,
            hours=_hour,
            observation=_observation,
            state=_state,
        )
        programming_obj.save()
        return JsonResponse({
            'message': True,
        }, status=HTTPStatus.OK)


def get_programming_grid_list(request):
    if request.method == 'GET':
        start_date = request.GET.get('start-date', '')
        end_date = request.GET.get('end-date', '')
        programming_set = Programming.objects.filter(create_at__date__range=(start_date, end_date))
        tpl = loader.get_template('certification/programming_grid_list.html')
        context = ({
            'programming_set': programming_set,
        })
        return JsonResponse({
            'success': True,
            'grid': tpl.render(context),
        }, status=HTTPStatus.OK)


def get_programming_grid_list_by_course(request):
    if request.method == 'GET':
        pk = request.GET.get('course_pk', '')
        course_obj = Course.objects.get(id=int(pk))
        try:
            programming_set = Programming.objects.filter(course=course_obj)
        except Programming.DoesNotExist:
            programming_set = {}

        tpl = loader.get_template('certification/programming_grid_list.html')
        context = ({
            'programming_set': programming_set,
        })
        return JsonResponse({
            'success': True,
            'grid': tpl.render(context),
        }, status=HTTPStatus.OK)
