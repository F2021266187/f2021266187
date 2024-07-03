from django.db import models

class Header(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    title_line = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
