from django.contrib import admin
from django.urls import path
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('people/', views.people_all, name="people_all"),
    path('people/alumni/', views.people_alumni, name="people_alumni"),
    path('projects', views.projects_all, name="projects_all"),
    path('projects/archive/', views.projects_archive, name="projects_archive"),
    path('projects/<int:pk>/', views.projects_detail, name="projects_detail"),
    path('publications/', views.publications_all, name="publications_all"),
    path('publications/patent/', views.publications_patent, name="publications_patent"),
    path('publications/book/', views.publications_book, name="publications_book"),
    path('publications/ic/', views.publications_ic, name="publications_ic"),
    path('publications/dc/', views.publications_dc, name="publications_dc"), 
 
]