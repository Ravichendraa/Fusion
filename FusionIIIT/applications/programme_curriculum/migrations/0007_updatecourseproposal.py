# Generated by Django 3.1.5 on 2024-02-18 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programme_curriculum', '0006_auto_20240218_1339'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateCourseProposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=100)),
                ('faculty_code', models.CharField(max_length=10)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('credit', models.PositiveIntegerField(default=0)),
                ('lecture_hours', models.PositiveIntegerField(null=True)),
                ('tutorial_hours', models.PositiveIntegerField(null=True)),
                ('pratical_hours', models.PositiveIntegerField(null=True)),
                ('discussion_hours', models.PositiveIntegerField(null=True)),
                ('project_hours', models.PositiveIntegerField(null=True)),
                ('pre_requisits', models.TextField(blank=True, null=True)),
                ('syllabus', models.TextField()),
                ('percent_quiz_1', models.PositiveIntegerField(default=10)),
                ('percent_midsem', models.PositiveIntegerField(default=20)),
                ('percent_quiz_2', models.PositiveIntegerField(default=10)),
                ('percent_endsem', models.PositiveIntegerField(default=30)),
                ('percent_project', models.PositiveIntegerField(default=15)),
                ('percent_lab_evaluation', models.PositiveIntegerField(default=10)),
                ('percent_course_attendance', models.PositiveIntegerField(default=5)),
                ('ref_books', models.TextField()),
                ('working_course', models.BooleanField(default=True)),
                ('status', models.PositiveIntegerField(default=0)),
                ('disciplines', models.ManyToManyField(blank=True, to='programme_curriculum.Discipline')),
                ('pre_requisit_courses', models.ManyToManyField(blank=True, to='programme_curriculum.Course')),
            ],
            options={
                'unique_together': {('code', 'faculty_code')},
            },
        ),
    ]
