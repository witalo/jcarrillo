from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust


class Person(models.Model):
    TYPE_CHOICES = (('1', 'Estudiante'), ('2', 'Docente'), ('3', 'Administrador'))
    id = models.AutoField(primary_key=True)
    document = models.CharField(max_length=15, null=True, blank=True)
    paternal_last_name = models.CharField(max_length=40, null=True, blank=True)
    maternal_last_name = models.CharField(max_length=40, null=True, blank=True)
    names = models.CharField(max_length=40, null=True, blank=True)
    birth_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    telephone = models.CharField(max_length=9, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    address = models.CharField('Direccion', max_length=200, null=True, blank=True)
    business = models.ForeignKey('Business', on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='person/',
                              default='person/employee0.jpg', blank=True)
    photo_thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1), ResizeToFill(
        100, 100)], source='photo', format='JPEG', options={'quality': 90})
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField('Tipo', max_length=50, choices=TYPE_CHOICES, default='1', )
    is_state = models.BooleanField('Estado', default=False)

    def _str_(self):
        return str(self.names)

    def full_name(self):
        return '{} {} {}'.format(self.names, self.paternal_last_name, self.maternal_last_name)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class Business(models.Model):
    id = models.AutoField(primary_key=True)
    ruc = models.CharField(max_length=11)
    business_name = models.CharField('Razón social', max_length=45, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=45, null=True, blank=True)
    legal_representative_name = models.CharField(max_length=100, null=True, blank=True)
    legal_representative_dni = models.CharField(max_length=45, null=True, blank=True)

    def __str__(self):
        return self.business_name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField('Codigo', max_length=45, null=True, blank=True)
    name = models.CharField('Razón social', max_length=45, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateTimeField(auto_now=True)
    is_state = models.BooleanField('Estado', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Programming(models.Model):
    STATE_CHOICES = (('P', 'Programado'), ('F', 'Finalizado'), ('A', 'Anulado'))
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True, blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    end_date = models.DateField('Fecha de nacimiento', null=True, blank=True)
    course_price = models.DecimalField('Precio del curso', max_digits=10, decimal_places=2, default=0)
    vacancies = models.IntegerField('Cantidad', default=0)
    hours = models.IntegerField('Horas', default=0)
    observation = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField('Estado', max_length=1, choices=STATE_CHOICES, default='P')
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.course.name)

    class Meta:
        verbose_name = 'Programacion'
        verbose_name_plural = 'Programaciones'


class DetailProgramming(models.Model):
    id = models.AutoField(primary_key=True)
    programing = models.ForeignKey('Programming', on_delete=models.CASCADE, null=True, blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE, null=True, blank=True)
    is_state = models.BooleanField('Estado', default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Detalle Programacion'
        verbose_name_plural = 'Detalle Programaciones'
