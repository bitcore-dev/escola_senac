from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def home(request):
    return render(request, 'home.html')

@login_required
def field_student(request):
    return render(request, 'field_student.html')

@login_required
def activity(request):
    return render(request, 'activity.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
@user_passes_test[lambda user: user.is_staff]
def teacher(request):
    return render(request, 'teacher.html')

