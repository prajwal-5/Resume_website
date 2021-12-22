from django.shortcuts import render

# Create your views here.
def home_page(req):
    context={'home': 'active'}
    return render(req, "core/home.html", context)

def contact(req):
    context={'contact': 'active'}
    return render(req, "contact/contact.html", context)