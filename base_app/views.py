from django.shortcuts import render

# Create your views here.
def SuperAdmin_index(request):
    return render(request,'SuperAdmin_index.html')

def SuperAdmin_personal_trainer(request):
    return render(request,'SuperAdmin_personal_trainer.html')

def SuperAdmin_active_trainers(request):
    return render(request,'SuperAdmin_active_trainers.html')

def SuperAdmin_resigned_trainers(request):
    return render(request,'SuperAdmin_resigned_trainers.html')

def SuperAdmin_activetrainer_update(request):
    return render(request,'SuperAdmin_activetrainer_update.html')

def SuperAdmin_resignedtrainer_update(request):
    return render(request,'SuperAdmin_resignedtrainer_update.html')


def User_index(request):
    return render(request,'User_index.html')

def User_payment_history(request):
    return render(request,'User_payment_history.html')


