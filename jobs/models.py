from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    requirements = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)


class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    skills = models.TextField()
    resume = models.FileField(upload_to='resumes/')
    applied_jobs = models.ManyToManyField(Job, related_name='applicants', blank=True)

    def __str__(self):
        return self.name
