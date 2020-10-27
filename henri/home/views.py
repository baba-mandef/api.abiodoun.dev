from django.shortcuts import render
from henri.home.models import Experience
from henri.blog.models import Post


def home(request):
    exps = Experience.objects.all()
    latest = Post.objects.filter(published=True)
    lasts = latest.order_by('created_at')[:3]
    context = {'exps': exps, 'lasts': lasts}
    return render(request, 'home.html', context)
