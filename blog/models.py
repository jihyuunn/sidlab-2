from django.db import models
from django.utils import timezone

# Create your models here.
class Publication(models.Model):
    author = models.CharField(max_length=200)
    title = models.TextField()
    issue = models.TextField()
    award = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    YEAR = (
        (2016, '2016'), (2017, '2017'), (2018, '2018'),
        (2019, '2019'), (2020, '2020'), (2021, '2021'),( 2022, '2022')
    )
    year = models.IntegerField(
        choices=YEAR,
        default=2019,
    )
    Books = 'Books&Magazines'
    Patent = 'Patent'
    International = 'International Conference'
    Domestic = 'Domestic Conference'
    SORT = (
        (Books, 'Books&Magazines'), (Patent,'Patent'),
        (International, 'International Conference'),
        (Domestic, 'Domestic Conference')
    )
    publication_sort = models.CharField(
        max_length=30,
        choices=SORT,
        default=International,
    )

    def __str__(self):
        return self.title

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_text = models.TextField()
    photo = models.ImageField(blank=True)
    finished = models.BooleanField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.project_name

class People(models.Model):
    people_name = models.CharField(max_length=200)
    people_status = models.CharField(max_length=200)
    blog = models.CharField(max_length=400, null=True)
    profile = models.ImageField(upload_to='people', blank=True)
    graduated = models.BooleanField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.people_name
