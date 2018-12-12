from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    '''
    用户信息表
    '''
    nid =models.AutoField(primary_key=True)
    telephone=models.CharField(max_length=11,null=True,blank=True,unique=True,verbose_name='电话号码')
    avatar=models.FileField(upload_to='static/imgs/',default='static/imgs/default.png',verbose_name='用户头像')
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    class Meta:
        verbose_name_plural='用户信息表'
    def __str__(self):
        return self.username

class Student(models.Model):
    '''
    学生信息表
    '''
    nid=models.AutoField(primary_key=True)
    std_num=models.CharField(max_length=11,verbose_name='学号')
    name=models.CharField(max_length=64,verbose_name='姓名')
    telephone=models.CharField(max_length=11,verbose_name='电话',blank=True,null=True)
    qq=models.CharField(max_length=11,verbose_name='qq',null=True,blank=True)
    std_grade=models.CharField(max_length=23,verbose_name='年级')
    std_class=models.CharField(max_length=24,verbose_name='班级')
    class Meta:
        verbose_name_plural='学生信息表'
    def __str__(self):
        return self.name

class StdExcel(models.Model):
    '''
    学生excel文件
    '''
    nid=models.AutoField(primary_key=True)
    stdfile=models.FileField(upload_to='static/stdfiles/',verbose_name='学生excel文件路径')
    upload_time=models.DateTimeField(auto_now_add=True,verbose_name='上传文件时间')