from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Publication, Project, People
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'blog/index.html', {})

def people_all(request):
    peoples = People.objects
    people_list = People.objects.all()
    paginator = Paginator(people_list, 4)
    page = request.GET.get('page')
    peopl = paginator.get_page(page)
    return render(request, 'blog/people_all.html', { 'peoples':peoples, 'peopl':peopl })

def people_alumni(request):
    peoples = People.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/people_alumni.html', { 'peoples':peoples })

def projects_all(request):
    projects = Project.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/projects_all.html', { 'projects':projects })

def projects_archive(request):
    projects = Project.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/projects_archive.html', { 'projects':projects })

def projects_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'blog/projects_detail.html', { 'project':project })

def publications_all(request):
    publications = Publication.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/publication_all.html', { 'publications':publications })

def publications_book(request):
    publications = Publication.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/publication_book.html', {'publications':publications})

def publications_patent(request):
    publications = Publication.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/publication_patent.html', {'publications':publications})

def publications_ic(request):
    publications = Publication.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/publication_ic.html', {'publications':publications})

def publications_dc(request):
    publications = Publication.objects.filter(created_date__lte=timezone.now())
    return render(request, 'blog/publication_dc.html', {'publications':publications})

# Create your views here.
