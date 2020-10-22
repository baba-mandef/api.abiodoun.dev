from django.shortcuts import render
from henri.home.models import Experience
from henri.blog.models import Post


def home(request):
    exps = Experience.objects.all()
    lasts = Post.objects.order_by('created_at')[:3]
    context = {'exps': exps, 'lasts': lasts}
    return render(request, 'home.html', context)
