# Generated by Django 2.1.4 on 2019-01-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('url', models.CharField(max_length=128, verbose_name='含正则的URL')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='角色昵称')),
                ('permission', models.ManyToManyField(blank=True, to='rbac.Permission', verbose_name='所拥有的权限')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('create_data', models.DateField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('password', models.CharField(max_length=16, verbose_name='密码')),
                ('role', models.ManyToManyField(to='rbac.Role', verbose_name='用户的角色')),
            ],
        ),
    ]
