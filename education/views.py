from django.shortcuts import render

# Create your views here.

def education(req):
    context={'education':'active'}
    return render(req, "education/education.html", context)