# Generated by Django 5.1.6 on 2025-03-06 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_name', models.CharField(max_length=255, verbose_name='Name of User')),
                ('user_email', models.EmailField(max_length=255, verbose_name='Email of User')),
                ('user_cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF User')),
                ('password', models.CharField(max_length=255, verbose_name='Password of User')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active?')),
                ('is_trusty', models.BooleanField(default=True, verbose_name='Trusty?')),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_permissions', to='auth.permission')),
            ],
            options={
                'db_table': 'autentication_module',
                'constraints': [models.UniqueConstraint(fields=('user_cpf',), name='unique_cpf'), models.UniqueConstraint(fields=('user_email',), name='unique_email')],
            },
        ),
    ]
