from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactTable
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail
import logging


# Create your views here.
def imbuto(request):
    return render(request, '../../acg/templates/imbuto.html', {'imbuto': imbuto})

def imishwi(request):
    return render(request, '../../acg/templates/imishwi.html',{'imishwi': imishwi})

def ifumbire(request):
    return render(request, '../../acg/templates/ifumbire.html',{'ifumbire': ifumbire})

def contact(request):
    return render(request, '../../acg/templates/contact.html',{'contact':contact})

# # def contact(request):
#     return render(request, '../../acg/templates/contact.html',{'contact':contact})  
def contact_us(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('email') and request.POST.get('message'):
            post = ContactForm()
            post.firstname = request.POST.get('firstname')
            post.email = request.POST.get('email')
            post.message = request.POST.get('message')
            post.save()

            return render(request, '../../acg/templates/contact.html',{'contact':post})

        else:
            return render(request, '../../acg/templates/contact.html',{'contact':post})
        
#         # create a form instance and populate it with data from the request:
#         form = ContactForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#                 form.firstname = form.cleaned_data['first_name']
#                 form.email = form.cleaned_data['email']
#                 form.message = form.cleaned_data['message']
#                 form.save()
                            
               
#                 # redirect to accounts page:
#                 return HttpResponseRedirect('../../acg/templates/contact.html')

#    # No post data availabe, let's just show the page.
#     else:
#         form = ContactForm()

#     return render(request, '../../acg/templates/contact.html', {'form': form})


    # form= ContactForm(request.POST or None)
    # if form.is_valid():
    #     firstname= form.cleaned_data.get("firstname")
    #     email= form.cleaned_data.get("email")
    #     message=form.cleaned_data.get("message")

    #     # if request.user.is_authenticated():
    #     #     subject= str(request.user) + "'s Comment"
    #     # else:
    #     #     subject= "A Visitor's Comment"

    #     # message= firstname + " with the email, " + email + ", sent the following message:\n\n" + message
    #     # send_mail(subject, message, 'dlhylton@gmail.com', [email])

    #     context= {'form': form}
    #     return render(request, '../../acg/templates/contact.html', context)

    # else:
    #     context= {'form': form}
    #     return render(request, '../../acg/templates/contact.html', context)