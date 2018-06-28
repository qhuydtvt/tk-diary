# Generated by Django 2.0.6 on 2018-06-28 07:33

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('teacher', models.CharField(blank=True, max_length=255)),
                ('support', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField(default=datetime.datetime.now)),
                ('note_summary', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='NotePrecise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_student', models.CharField(max_length=255)),
                ('note', ckeditor.fields.RichTextField()),
                ('diary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_precise', to='note.Diary')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('headline', models.CharField(choices=[('Teacher', 'Teacher'), ('Supporter', 'Supporter')], default=('Teacher', 'Teacher'), max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='diary',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='diary',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diary', to='note.Class'),
        ),
    ]
