# Generated by Django 4.1.7 on 2023-02-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_rename_age_userprofile_image"),
    ]

    operations = [
        migrations.RemoveField(model_name="userprofile", name="image",),
        migrations.AddField(
            model_name="userprofile",
            name="icon",
            field=models.ImageField(
                blank=True, null=True, upload_to="icons/% Y/% m/% d/"
            ),
        ),
    ]
