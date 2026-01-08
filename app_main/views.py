
# Create your views here.
from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    q=request.GET.get('q')
    employees=Employee.objects.all()
    if q:
        employees=employees.filter(name__icontains=q)
    return render(request,'list.html',{'employees':employees})

def employee_create(request):
    form=EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'form.html',{'form':form})

def employee_update(request,id):
    p=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST or None,instance=p)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'form.html',{'form':form})

def employee_delete(request,id):
    Employee.objects.get(id=id).delete()
    return redirect('/')

