# Generated by Django 2.2.15 on 2022-08-22 06:20

import ckeditor.fields
import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Image', 'Image'), ('Video', 'Video')], default=1, max_length=50)),
                ('file', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('intro', ckeditor.fields.RichTextField()),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('intro', models.TextField(max_length=300)),
                ('description', ckeditor.fields.RichTextField()),
                ('thumb', cloudinary.models.CloudinaryField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('album', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Album')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Country')),
                ('programs', models.ManyToManyField(blank=True, null=True, related_name='cases', to='gallery.Program')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Region')),
            ],
        ),
    ]
