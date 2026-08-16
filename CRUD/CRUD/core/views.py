from django.views import View
from django.shortcuts import render, redirect
from .models import Student
from .forms import AddStudentForm


class Home(View):
    def get(self, request):
        stu_data = Student.objects.all()
        return render(request, 'core/home.html', {'studata': stu_data})

class Edit_Student(View):
    def get(self, request, id):
        studata = Student.objects.get(id=id)
        fm = AddStudentForm(instance=studata)
        return render(request, 'core/edit-student.html', {'form': fm, 'student': studata})

    def post(self, request, id):
        studata = Student.objects.get(id=id)
        fm = AddStudentForm(request.POST, instance=studata)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        return render(request, 'core/edit-student.html', {'form': fm, 'student': studata})


class Delete_Student(View):
    def post(self, request):
        id = request.POST.get('id')
        studata = Student.objects.get(id=id)
        studata.delete()
        return redirect('/')


class Add_Student(View):
    def get(self, request):
        fm = AddStudentForm()
        return render(request, 'core/add-student.html', {'form': fm})
    
    def post(self, request):
        fm = AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        return render(request, 'core/add-student.html', {'form': fm})
    
    

