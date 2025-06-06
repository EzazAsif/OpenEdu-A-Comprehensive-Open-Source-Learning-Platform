# Generated by Django 5.1.7 on 2025-03-27 01:05

import django.db.models.deletion
import lms.contentUploadStratagy
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(default='images/department/default.jpg', null=True, upload_to='images/department/')),
                ('description', models.TextField(default='The Department fosters innovative research and interdisciplinary collaboration, focusing on conceptual exploration and advanced academic problem-solving techniques.', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=6, unique=True)),
                ('course_name', models.CharField(max_length=50)),
                ('course_description', models.TextField(default='This course provides a comprehensive overview of essential topics, methodologies, and concepts. Further details will be provided.')),
                ('image', models.ImageField(default='images/course/default.jpg', null=True, upload_to='images/course/')),
                ('admins', models.ManyToManyField(blank=True, related_name='courses_administered', to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='lms.department')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='images/faculty/default.jpg', null=True, upload_to='images/faculty/')),
                ('position', models.CharField(max_length=100)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Faculty', to='lms.course')),
                ('moderators', models.ManyToManyField(blank=True, related_name='faculty_moderated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to=lms.contentUploadStratagy.NoteUploadStrategy.get_upload_to)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='lms.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to=lms.contentUploadStratagy.SlideUploadStrategy.get_upload_to)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slides', to='lms.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='temp_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to=lms.contentUploadStratagy.TempNoteUploadStrategy.get_upload_to)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('real', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp_versions', to='lms.note')),
            ],
        ),
        migrations.CreateModel(
            name='temp_Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to=lms.contentUploadStratagy.TempSlideUploadStrategy.get_upload_to)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('real', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp_versions', to='lms.slide')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to=lms.contentUploadStratagy.VideoUploadStrategy.get_upload_to)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='lms.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='temp_Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.FileField(upload_to=lms.contentUploadStratagy.TempVideoUploadStrategy.get_upload_to)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('real', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temp_versions', to='lms.video')),
            ],
        ),
    ]
