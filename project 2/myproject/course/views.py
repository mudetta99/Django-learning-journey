from django.shortcuts import render, get_object_or_404, redirect
from .models import *

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# def course_list(request):
#     courses = [
#         {"id": 1, "name": "Python", "duration": "3 months", "level": "Beginner"},
#         {"id": 2, "name": "Django", "duration": "2 months", "level": "Intermediate"},
#         {"id": 3, "name": "JavaScript", "duration": "3 months", "level": "Beginner"},
#         {"id": 4, "name": "React.js", "duration": "2 months", "level": "Intermediate"},
#         {"id": 5, "name": "Machine Learning", "duration": "4 months", "level": "Advanced"},
#         {"id": 6, "name": "Cybersecurity", "duration": "3 months", "level": "Intermediate"},
#     ]

#     return render(request, 'course/course_list.html', {"courses":courses})

def course_list(request):
    # courses = Course.objects.all()
    courses = Course.objects.filter(activate=True)
    return render(request, 'course/course_list.html', {'courses':courses})

@csrf_exempt
def course_form(request):
    if request.method == 'POST':
        Course.objects.create(
            name=request.POST.get('name'), 
            duration=request.POST.get('duration'), 
            level=request.POST.get('level'),
            image=request.FILES.get('image') 
        )

    return render(request, "course/course_form.html")


def course_update(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.name = request.POST.get('name', course.name)
        course.duration = request.POST.get('duration', course.duration)
        course.level = request.POST.get('level', course.level)
        
        if request.FILES.get('image'):
            course.image = request.FILES.get("image")

        course.save()
        return redirect('courses')
    
    return render(request, 'course/update.html', {"course":course})



def course_delete(request, course_id):
    Course.objects.filter(id=course_id).update(activate=False)
    return redirect('courses')




