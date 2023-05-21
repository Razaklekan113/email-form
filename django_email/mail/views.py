from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import EmailForm
from django.template.loader import render_to_string


def index(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            

            html = render_to_string('mail/emails/mailform.html', {
                'name': name,
                'email': email,
                'content': content
            }) 

            print("The form was valid")

            send_mail("The mail form subject", "This is the message", "noreply@razaklekan11.com", ['razaklekan11@gmail.com'], html_message=html)
            return redirect('index')
    else:
        form = EmailForm()

    return render(request, 'mail/index.html', {'form': form})
