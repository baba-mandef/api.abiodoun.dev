from django.shortcuts import render
from henri.home.models import Experience


def home(request):
    exps = Experience.objects.all()
    context = {'exps': exps}
    return render(request, 'home.html', context)
