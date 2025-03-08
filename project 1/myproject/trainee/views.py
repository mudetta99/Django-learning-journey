from django.shortcuts import render

# Create your views here.

def trainee_list(request):
    trainees = [
        {"id":1, "first_name": "Mohamed", "last_name": "Emad", "email": "mohamed@gmail.com", "phone": "01111111111", "age": 25, "joined_date": "2024-03-01"},
        {"id":2, "first_name": "Annabella", "last_name": "Ismaeel", "email": "annabella@gmail.com", "phone": "010000000000", "age": 22, "joined_date": "2024-02-15"},
        {"id":3, "first_name": "Karolina", "last_name": "Aziz", "email": "karolina@gmail.com", "phone": "01222222222", "age": 30, "joined_date": "2024-01-20"},
    ]
    return render(request, 'trainee/trainee_list.html', {"trainees":trainees})


def trainee_form(request):
    return render(request, 'trainee/trainee_form.html')