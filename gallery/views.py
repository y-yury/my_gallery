from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from .models import Photo, Email
from .forms import ContactForm


class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photos'
    queryset = Photo.objects.all()
    template_name = 'gallery/base.html'


def mail_archive(request):
    all_mail = Email.objects.all()
    return render(request, 'archive/mail_archive.html',
                  {'all_mail': all_mail})


@login_required
def submit_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()

            try:
                send_mail(subject, message, 'admin@myblog.com', ['y.sapozhkov@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Sorry, invalid header was submitted.')

            return HttpResponse('Thank you for the mail submitted!')

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})