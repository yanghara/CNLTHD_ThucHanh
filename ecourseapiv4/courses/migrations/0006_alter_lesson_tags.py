# Generated by Django 5.0.3 on 2024-03-28 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_options_alter_tag_options_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]
