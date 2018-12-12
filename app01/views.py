from django.shortcuts import render,HttpResponse,redirect
from app01 import models
import json
import os
import uuid
from utility.deal_1 import ExcelDeal
# Create your views here.
def register(request):
    '''
    注册用户
    :param request:
    :return:
    '''
    if request.method=='GET':
        return render(request,'register.html')
    if request.method=='POST':
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            avatar=request.POST.get('avatar')
            models.UserInfo.objects.create(username=username,password=password,avatar=avatar)
        except Exception as e:
            print(e)
            return HttpResponse('注册失败')
        return  redirect('/index/')
def img_iframe(request):
    '''
    处理注册用户的头像
    :param request:
    :return:
    '''
    ret={'status':True,'error':None,'data':None}
    try:
        avatar=request.FILES.get('avatar')
        img_name=str(uuid.uuid4())+'.'+avatar.name.rsplit('.',maxsplit=1)[1]
        img_path=os.path.join('static','imgs',img_name)
        with open(img_path,'wb') as f:
            for line in avatar.chunks():
                f.write(line)
        ret['data']=img_path
    except Exception as e:
        ret['status']=False
        ret['error']='上传失败'
    return HttpResponse(json.dumps(ret))

def index(request):
    '''
    excel 文件导入系统首页
    :param request:
    :return:
    '''
    student_list=models.Student.objects.all()
    return render(request,'index.html',locals())

def std_excel_upload(request):
    '''
    处理上传 student excel 文件
    :param request:
    :return:
    '''
    ret = {'status': True, 'error': None, 'data': None}
    try:
        std_excel=request.FILES.get('stu_excel')
        std_file_name = str(uuid.uuid4()) + '.' + std_excel.name.rsplit('.', maxsplit=1)[1]
        std_file_path = os.path.join('static', 'stdfiles', std_file_name)
        with open(std_file_path,'wb') as f:
            for line in std_excel.chunks():
                f.write(line)
        models.StdExcel.objects.create(stdfile=std_file_path)
        ret['data']=std_file_path
        std_excel_obj=ExcelDeal(std_file_path)
        std_excel_obj.excel_deal()
        return redirect('/index/')
    except Exception as e :
        ret['error']='上传失败'
        return HttpResponse(json.dumps(ret))