from django.contrib import admin
from .models import Header, Education, Skill, Project, Contact

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'title_line')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
