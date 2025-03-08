from django.shortcuts import render

# Create your views here.

def course_list(request):
    courses = [
        {"id": 1, "name": "Python", "duration": "3 months", "level": "Beginner"},
        {"id": 2, "name": "Django", "duration": "2 months", "level": "Intermediate"},
        {"id": 3, "name": "JavaScript", "duration": "3 months", "level": "Beginner"},
        {"id": 4, "name": "React.js", "duration": "2 months", "level": "Intermediate"},
        {"id": 5, "name": "Machine Learning", "duration": "4 months", "level": "Advanced"},
        {"id": 6, "name": "Cybersecurity", "duration": "3 months", "level": "Intermediate"},
    ]

    return render(request, 'course/course_list.html', {"courses":courses})


def course_form(request):
    return render(request, "course/course_form.html")