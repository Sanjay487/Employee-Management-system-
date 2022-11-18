from django.shortcuts import render, HttpResponse
from .models import Employees, Role, Department
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employees.objects.all()
    context ={
        'emps' :emps
    }
    print(context)
    return render(request, 'view_all_emp.html',context)


def add_emp(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        
        last_name = request.POST['last_name']
        
        Dept_name = request.POST['Dept_name']
        
        joining_date  = request.POST['joining_date']
        
        salary = int(request.POST['salary'])
        
        role = request.POST['role']
        
        phone = int(request.POST['phone'])

        dept_instance = Department.objects.get(name=Dept_name.lower())
        role_instance = Role.objects.get(name=role.lower())

        new_emp=Employees(first_name=first_name,last_name=last_name,Dept_name=dept_instance,joining_date=joining_date,salary=salary,role=role_instance,
                  phone=phone)
        new_emp.save()
        return HttpResponse('Employee added Successfully. <br><br> <a href="/" >Go to Homepage</a> <br><br> <a href="/add_emp" >Add more Employees</a><br><br> <a href="/all_emp" >View all Employees</a>')

    context = {
        "departments": Department.objects.all(),
        "roles": Role.objects.all()
    }

    return render(request, 'add_emp.html', context)

def remove_emp(request):
    if request.method =='POST':
        emp_id=request.POST['Emp_id']
        Employees.objects.get(pk=emp_id).delete()
        return HttpResponse('Employee removed Successfully. <br><br> <a href="/" >Go to Homepage</a> <br><br> <a href="/add_emp" >Add more Employees</a><br><br> <a href="/all_emp" >View all Employees</a>')
    return render(request, 'remove_emp.html')


def filter_emp(request):
    if request.method == 'POST':
        department = request.POST['department']
        dept_instance = Department.objects.get(name=department.lower())
        
        emps = Employees.objects.filter(Dept_name=dept_instance)
        context ={
            'emps' :emps,
            'show_emps': True
        } 
        return render(request, 'filter_emp.html', context)

    return render(request, 'filter_emp.html', {"show_emps": False})
