from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from course.models import Course  


def trainee_list(request):
    # trainees = Trainee.objects.filter(activate=True)
    trainees = Trainee.objects.select_related('course').filter(activate=True)  
    return render(request, 'trainee/trainee_list.html', {"trainees":trainees})

def trainee_form(request):
    if request.method == 'POST':
        course_id = request.POST.get('course') 
        course = Course.objects.get(id=course_id) if course_id else None 

        Trainee.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            age=request.POST.get('age'),
            joined_date=request.POST.get('joined_date'),
            course=course 
        )

    courses = Course.objects.all() 
    return render(request, 'trainee/trainee_form.html', {'courses': courses})


def trainee_update(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)
    courses = Course.objects.filter(activate=True)

    if request.method == 'POST':
        trainee.first_name = request.POST.get('first_name', trainee.first_name)
        trainee.last_name = request.POST.get('last_name', trainee.last_name)
        trainee.email = request.POST.get('email', trainee.email)
        trainee.phone = request.POST.get('phone', trainee.phone)
        trainee.age = request.POST.get('age', trainee.age)
        trainee.joined_date = request.POST.get('joined_date', trainee.joined_date)
        trainee.course_id = request.POST.get('course', trainee.course_id)  

        trainee.save()
        return redirect('trainee')    
    
    return render(request, 'trainee/update.html', {"trainee": trainee, "courses": courses})



def trainee_delete(request, trainee_id):
    Trainee.objects.filter(id=trainee_id).update(activate=False)
    return redirect('trainee')
    
