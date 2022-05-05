from django.shortcuts import render
from .models import Project, Achievement, Certification

# HOME PAGE
def home_page(req):
    context={'home': 'active'}
    return render(req, "core/home.html", context)

# Education page
def education(req):
    context={'education':'active'}
    return render(req, "education/education.html", context)

# Projects page
def projects(req):
    data = Project.objects.all()
    return render(req, "projects/projects.html", {'projects':'active', 'data': data})

# Achievements page
def achieve(req):
    data = Achievement.objects.all()
    return render(req, "achievements/achieve.html", {'achievements':'active', 'data': data})

# Skills page
def skills(req):
    context={'skills':'active'}
    return render(req, "skills/skills.html", context)

# Certifications page
def certifications(req):
    data = Certification.objects.all()
    return render(req, "certifications/certifications.html", {'certifications':'active', 'data': data})