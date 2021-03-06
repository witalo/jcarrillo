# Generated by Django 3.0.5 on 2021-03-09 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruc', models.CharField(max_length=11)),
                ('business_name', models.CharField(blank=True, max_length=45, null=True, verbose_name='Razón social')),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=45, null=True)),
                ('legal_representative_name', models.CharField(blank=True, max_length=100, null=True)),
                ('legal_representative_dni', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=45, null=True, verbose_name='Codigo')),
                ('name', models.CharField(blank=True, max_length=45, null=True, verbose_name='Razón social')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('is_state', models.BooleanField(default=False, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.CharField(blank=True, max_length=15, null=True)),
                ('paternal_last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('maternal_last_name', models.CharField(blank=True, max_length=40, null=True)),
                ('names', models.CharField(blank=True, max_length=40, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('telephone', models.CharField(blank=True, max_length=9, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('photo', models.ImageField(blank=True, default='person/employee0.jpg', upload_to='person/')),
                ('type', models.CharField(choices=[('1', 'Estudiante'), ('2', 'Docente'), ('3', 'Administrador')], default='1', max_length=50, verbose_name='Tipo')),
                ('is_state', models.BooleanField(default=False, verbose_name='Estado')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certification.Business')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Programming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('course_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio del curso')),
                ('vacancies', models.IntegerField(default=0, verbose_name='Cantidad')),
                ('hours', models.IntegerField(default=0, verbose_name='Horas')),
                ('observation', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(choices=[('P', 'Programado'), ('F', 'Finalizado'), ('A', 'Anulado')], default='P', max_length=1, verbose_name='Estado')),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certification.Course')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certification.Person')),
            ],
            options={
                'verbose_name': 'Programacion',
                'verbose_name_plural': 'Programaciones',
            },
        ),
        migrations.CreateModel(
            name='DetailProgramming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_state', models.BooleanField(default=False, verbose_name='Estado')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certification.Person')),
                ('programing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='certification.Programming')),
            ],
            options={
                'verbose_name': 'Detalle Programacion',
                'verbose_name_plural': 'Detalle Programaciones',
            },
        ),
    ]
