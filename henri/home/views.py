from django.shortcuts import render
from henri.home.models import Experience
from henri.blog.models import Post
from henri.home.forms import Contact
from django.core.mail import send_mail
from root.settings import EMAIL_HOST_USER


def home(request):
    exps = Experience.objects.all()
    latest = Post.objects.filter(published=True)
    lasts = latest.order_by('created_at')[:-3]
    if request.method == 'GET':
        form = Contact()
    else:
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['mail_subject']
            email = form.cleaned_data['author_mail']
            message1 = form.cleaned_data['mail_content']
            message = message1+'\n by :  '+email
            send_mail(subject, message, email, [EMAIL_HOST_USER])
    context = {'exps': exps, 'lasts': lasts, 'form': form}
    return render(request, 'home.html', context)
