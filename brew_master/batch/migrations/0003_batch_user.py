# Generated by Django 4.2.5 on 2023-09-23 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('batch', '0002_batch_is_selected'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
