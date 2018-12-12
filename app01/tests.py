from django.test import TestCase
from  app01 import  models
# Create your tests here.
import xlrd
std_file=xlrd.open_workbook(r'C:\Users\sakula_he\PycharmProjects\2018-0903\myexcel\static\stdfiles\学生信息数据.xlsx',)
sheet0 = std_file.sheet_by_index(0)
std_list=[]
for i in range(1,sheet0.nrows):
    # std_num=sheet0.row_values(i)[0]
    # name=sheet0.row_values(i)[1]
    # telephone=sheet0.row_values(i)[2]
    # qq=sheet0.row_values(i)[3]
    # std_grade=sheet0.row_values(i)[4]
    # std_class=sheet0.row_values(i)[5]
    std_list.append(models.Student(
        std_num=sheet0.row_values(i)[0],
        name=sheet0.row_values(i)[1],
        telephone=sheet0.row_values(i)[2],
        qq=sheet0.row_values(i)[3],
        std_grade=sheet0.row_values(i)[4],
        std_class=sheet0.row_values(i)[5]))
models.Student.objects.bulk_create(std_list)