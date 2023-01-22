# Generated by Django 3.2.16 on 2023-01-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulting', '0033_rename_hero_testimonias_cards_homeconsulting_hero_testimonials_cards'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_footer_company_name',
            field=models.CharField(default='', max_length=100, verbose_name='nombre compañia'),
        ),
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_footer_privacy_policy',
            field=models.CharField(default='', max_length=150, verbose_name='link politica de privacidad'),
        ),
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_footer_terms_conditions',
            field=models.CharField(default='', max_length=150, verbose_name='link terminos y condiciones'),
        ),
        migrations.AddField(
            model_name='homeconsulting',
            name='hero_footer_year',
            field=models.CharField(default='', max_length=4, verbose_name='año actual'),
        ),
    ]
