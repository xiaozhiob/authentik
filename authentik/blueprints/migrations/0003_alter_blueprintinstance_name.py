# Generated by Django 4.1.7 on 2023-04-28 10:49

from django.db import migrations, models

from authentik.lib.migrations import fallback_names


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_blueprints", "0002_blueprintinstance_content"),
    ]

    operations = [
        migrations.RunPython(fallback_names("authentik_blueprints", "blueprintinstance", "name")),
        migrations.AlterField(
            model_name="blueprintinstance",
            name="name",
            field=models.TextField(unique=True),
        ),
    ]