from django.shortcuts import render, redirect
from .models import Student
# Create your views here.

def index(request):
    students = Student.objects.all()
    # name, email, birthday, age > Student 에 들어가야 할 것들입니다.
    return render(request, 'students/index.html', {'students':students})
    
def new(request):
    if request.method=='POST': # 직접 등록해야 실행된다 > POST 타입
        student=Student()
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.birthday = request.POST.get('birthday')
        student.age = request.POST.get('age')
        student.save()
        return redirect('/students/')
    else:
        return render(request, 'students/new.html')
    
# def create(request):
#     student=Student()
#     student.name = request.POST.get('name')
#     student.email = request.POST.get('email')
#     student.birthday = request.POST.get('birthday')
#     student.age = request.POST.get('age')
#     student.save()
#     return redirect('/students/')

def detail(request,pk):
    student=Student.objects.get(pk=pk)
    return render(request, 'students/detail.html',{'student':student})
    
def delete(request,pk):
    student=Student.objects.get(pk=pk)
    student.delete()
    return redirect('/students/')
