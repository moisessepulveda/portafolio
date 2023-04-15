# Generated by Django 3.2.16 on 2023-04-15 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0024_index_image_file_hash'),
        ('consulting', '0050_accounttype_bank_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Colaborador', 'verbose_name_plural': 'Colaboradores'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='account_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Numero de cuenta'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='account_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='consulting.accounttype', verbose_name='Tipo de cuenta'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='bank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='consulting.bank', verbose_name='Banco'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='father_last_name',
            field=models.CharField(max_length=100, verbose_name='Apellido paterno'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen de perfil'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mother_last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido materno'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='second_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Segundo nombre'),
        ),
    ]