# Generated by Django 5.1 on 2024-12-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GradeWireapp', '0003_alter_student_register_id_alter_teacher_teacher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='register_id',
            field=models.CharField(max_length=20),
        ),
    ]
