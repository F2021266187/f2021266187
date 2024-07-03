from django.shortcuts import render, redirect
from .models import Header, Education, Skill, Project, Contact
from .forms import ContactForm

def index(request):
    header = Header.objects.first()
    education_list = Education.objects.all()
    skills_list = Skill.objects.all()
    projects_list = Project.objects.all()
    return render(request, 'portfolio/index.html', {
        'header': header,
        'education_list': education_list,
        'skills_list': skills_list,
        'projects_list': projects_list
    })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'portfolio/contact.html', {'form': form})
