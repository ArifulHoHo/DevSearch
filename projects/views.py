from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . models import Project, Tag
from .forms import ProjectForm, ReviewForm
from django.contrib import messages
from .utils import searchProject, paginateProjects
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def projects(request):

    projects, search_query = searchProject(request)

    custom_range, projects = paginateProjects(request, projects)
    context = {'projects': projects,'custom_range':custom_range, 'search_query':search_query}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()


        projectObj.getVoteCount
        # update project vote count
        
        messages.success(request, 'Review Saved!')
        return redirect('project',pk)

    return render(request,'projects/single-project.html',{'project':projectObj,'form':form})


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')

    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def updateProject(request,pk):
    # we need to specify which project we want to edit so we take pk
    # find the project object
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    # set the instance to that project
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form':form}
    return render(request,'projects/project_form.html',context)

@login_required(login_url='login')
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context={'object':project}
    return render(request,'delete_template.html',context)