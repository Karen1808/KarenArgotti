# Generated by Django 5.1.2 on 2024-11-19 18:46

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0003_yourmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='YourModel',
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=django_ckeditor_5.fields.CKEditor5Field(),
        ),
    ]
