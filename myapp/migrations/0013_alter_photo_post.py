# Generated by Django 4.1.7 on 2023-03-04 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0012_alter_post_likes_alter_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.post"
            ),
        ),
    ]
