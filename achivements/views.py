from django.shortcuts import render

# Create your views here.
def achieve(req):
    context={'skill':'active'}
    return render(req, "achievements/achieve.html", context)