from django.db import models

# models.py
from django.db import models

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(upload_to='images', default='profile.png')

    def __str__(self):
        return self.name

class Hero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button1_text = models.CharField(max_length=50)
    button1_link = models.URLField()
    button2_text = models.CharField(max_length=50)
    button2_link = models.URLField()

    def __str__(self):
        return self.title




class AboutSection(models.Model):
    video_url = models.URLField()
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service(models.Model):
    icon_class = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Program(models.Model):
    image = models.ImageField(upload_to='program_images/')
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher_name = models.CharField(max_length=255)
    teacher_role = models.CharField(max_length=255)
    seats = models.IntegerField()
    lessons = models.IntegerField()
    hours = models.IntegerField()

    def __str__(self):
        return self.title

class Event(models.Model):
        image = models.ImageField(upload_to='event_images/')
        date = models.DateField()
        time = models.CharField(max_length=255)
        location = models.CharField(max_length=255)
        title = models.CharField(max_length=255)
        description = models.TextField()

        def __str__(self):
            return self.title

class Blog(models.Model):
    image = models.ImageField(upload_to='blog_images/')
    date = models.DateField()
    author_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    comments_count = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    image = models.ImageField(upload_to='team_images/')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonial_images/')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    rating = models.PositiveIntegerField()
    content = models.TextField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    eid = models.PositiveIntegerField (max_length=8)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)

    def __str__(self):
        return "%s " %(self.ename)
    class Meta:
        db_table = "employee"