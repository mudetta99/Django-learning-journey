from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

# def trainee_list(request):
#     trainees = [
#         {"id":1, "first_name": "Mohamed", "last_name": "Emad", "email": "mohamed@gmail.com", "phone": "01111111111", "age": 25, "joined_date": "2024-03-01"},
#         {"id":2, "first_name": "Annabella", "last_name": "Ismaeel", "email": "annabella@gmail.com", "phone": "010000000000", "age": 22, "joined_date": "2024-02-15"},
#         {"id":3, "first_name": "Karolina", "last_name": "Aziz", "email": "karolina@gmail.com", "phone": "01222222222", "age": 30, "joined_date": "2024-01-20"},
#     ]
#     return render(request, 'trainee/trainee_list.html', {"trainees":trainees})

def trainee_list(request):
    # trainees = Trainee.objects.all()
    trainees = Trainee.objects.filter(activate=True)
    return render(request, 'trainee/trainee_list.html', {"trainees":trainees})

def trainee_form(request):

    if (request.method == 'POST'):
        Trainee.objects.create(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            age = request.POST.get('age'),
            joined_date = request.POST.get('joined_date'),
        )

    return render(request, 'trainee/trainee_form.html')


def trainee_update(request, trainee_id):
    trainee = get_object_or_404(Trainee, id=trainee_id)

    if request.method == 'POST':
        trainee.first_name = request.POST.get('first_name', trainee.first_name)
        trainee.last_name = request.POST.get('last_name', trainee.last_name)
        trainee.email = request.POST.get('email', trainee.email)
        trainee.phone = request.POST.get('phone', trainee.phone)
        trainee.age = request.POST.get('age', trainee.age)
        trainee.joined_date = request.POST.get('joined_date', trainee.joined_date)

        trainee.save()
        return redirect('trainee')    
    
    return render(request, 'trainee/update.html', {"trainee": trainee})



def trainee_delete(request, trainee_id):
    Trainee.objects.filter(id=trainee_id).update(activate=False)
    return redirect('trainee')
    
