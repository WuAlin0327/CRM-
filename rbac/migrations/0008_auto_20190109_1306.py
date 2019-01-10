# Generated by Django 2.1.4 on 2019-01-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0007_permission_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='icon',
        ),
        migrations.AddField(
            model_name='permission',
            name='name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='URL的别名'),
        ),
    ]
