from django.shortcuts import render

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
    context={'projects':'active'}
    return render(req, "projects/projects.html", context)

# Achievements page
def achieve(req):
    context={'achievements':'active'}
    return render(req, "achievements/achieve.html", context)

# Skills page
def skills(req):
    context={'skills':'active'}
    return render(req, "skills/skills.html", context)

# Certifications page
def certifications(req):
    context={'certifications':'active'}
    return render(req, "certifications/certifications.html", context)