# Generated by Django 2.0.4 on 2018-12-12 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('std_num', models.CharField(max_length=11, verbose_name='学号')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, verbose_name='电话')),
                ('qq', models.CharField(blank=True, max_length=11, null=True, verbose_name='qq')),
                ('std_grade', models.CharField(max_length=23, verbose_name='年级')),
                ('std_class', models.CharField(max_length=24, verbose_name='班级')),
            ],
            options={
                'verbose_name_plural': '学生信息表',
            },
        ),
    ]
