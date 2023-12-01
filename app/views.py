from django.shortcuts import render
from .models import ContactMessage, Hero, AboutSection, Event, Blog, TeamMember, Testimonial, Service
from django.shortcuts import get_object_or_404, redirect
from .models import Child


def index(request):
    # Retrieve data for each section
    hero_data = Hero.objects.first() if Hero.objects.exists() else None
    about_data = AboutSection.objects.first() if AboutSection.objects.exists() else None
    events_data = Event.objects.all()[:3]
    blog_data = Blog.objects.all()[:3]
    team_data = TeamMember.objects.all()[:4]
    testimonials_data = Testimonial.objects.all()[:3]
    services_data = Service.objects.all()

    # Additional context data, if needed
    context = {
        'navbar': 'index',
        'hero_data': hero_data,
        'about_data': about_data,
        'events_data': events_data,
        'blog_data': blog_data,
        'team_data': team_data,
        'testimonials_data': testimonials_data,
    }

    return render(request, 'index.html', context)


from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'form.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})


def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
def about(request):
    abouts = About.objects.all()
    context = {'navbar': 'about'}
    return render(request, 'about.html', context)

def blog(request):
    blogs = Blog.objects.all()
    context = {'navbar': 'blog'}
    return render(request, 'blog.html', context)

def contact(request):
    data = ContactMessage.objects.all()
    context = {'navbar': 'contact'}
    return render(request, 'contact.html', context)

def event(request):
    events = Event.objects.all()
    context = {'navbar': 'event'}
    return render(request, 'event.html', context)

def program(request):
    programs = Program.objects.all()
    context = {'navbar': 'program'}
    return render(request, 'program.html', context)

def service(request):
    services = Service.objects.all()
    context = {'navbar': 'service'}
    return render(request, 'service.html', context)

def insertdata(request):
    if request.method == 'POST':
        name = request.POST.get('first name')
        last_name = request.POST.get('last name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        image = request.FILES['image']

        room = Student(name=name, email=email, age=age, image=image)
        room.save()
        messages.success(request, 'data entered successfully')
        return redirect("/viewdata")

    return redirect("/viewdata")


def team(request):
    teams = TeamMember.objects.all()
    context = {'navbar': 'team'}
    return render(request, 'team.html', context)

def testimonial(request):
    testimonials = Testimonial.objects.all()
    context = {'navbar': 'testimonial'}
    return render(request, 'testimonial.html', context)

