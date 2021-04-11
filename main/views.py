from django.shortcuts import render,redirect
from .models import Skill ,Portfolio,Contact
from .forms import ContactForm
# Create your views here.


def home(request):
    
    skills=Skill.objects.all()
    portfolios=Portfolio.objects.all()

    new_message = None
    # Comment posted
    if request.method == 'POST':
        message_form = ContactForm(data=request.POST)
        if message_form.is_valid():

            # Create Comment object but don't save to database yet
            new_message = message_form.save(commit=False)
            # Assign the current post to the comment
            # Save the comment to the database
            new_message.save()
    return render(request,'main/index.html',{'skills':skills,'portfolios':portfolios,'form':ContactForm()})


