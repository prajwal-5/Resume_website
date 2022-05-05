from django.contrib import admin
from .models import Project, Achievement, Certification
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tools', 'link', 'glimpse']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'link']


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'link']