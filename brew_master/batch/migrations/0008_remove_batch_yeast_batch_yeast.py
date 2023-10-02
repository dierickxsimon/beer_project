# Generated by Django 4.2.5 on 2023-09-24 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0007_alter_batch_yeast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='yeast',
        ),
        migrations.AddField(
            model_name='batch',
            name='yeast',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='batch.yeast'),
        ),
    ]
