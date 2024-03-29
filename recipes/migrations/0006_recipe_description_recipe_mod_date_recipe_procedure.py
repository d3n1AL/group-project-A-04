# Generated by Django 4.0.3 on 2022-03-27 20:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='mod_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='procedure',
            field=models.TextField(blank=True),
        ),
    ]
