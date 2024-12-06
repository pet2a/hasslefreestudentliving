from enum import member

from django.shortcuts import render, redirect
from django.template.context_processors import request

from myapp.models import Appointment, Contact, Member, ImageModel
from myapp.forms import AppoitmentForm,ImageUpLoadForms


# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']
            ).exists():
                 members= Member.objects.get(
                    username=request.POST['username'],
                    password=request.POST['password']
                 )
                 return render(request, 'index.html', {'members' :members})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')






def services(request):
    return render(request, 'services.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def myservices(request):
    return render(request, 'myservices.html')

def doctors(request):
    return render(request, 'doctors.html')

def departments(request):
    return render(request, 'departments.html')

def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/wow')
    else:
        return render(request, 'contact.html')

def appointment(request):
    if request.method == "POST":
        myappointment=Appointment(
            name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            date=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        )
        myappointment.save()
        return redirect('/show')
    else:
        return render(request, 'appointment.html')

def show(request):
    allappointments = Appointment.objects.all()
    return render(request, 'show.html', {'appointment' :allappointments})

def delete(request,id):
    appoint=Appointment.objects.get(id=id)
    appoint.delete()
    return redirect('/show')

def wow(request):
    cont= Contact.objects.all()
    return render(request, 'wow.html', {'contact' :cont})

def dele(request,id):
    conts=Contact.objects.get(id=id)
    conts.delete()
    return redirect('/wow')

def edit(request,id):
    editapppointment=Appointment.objects.get(id=id)
    return render(request, 'edit.html', {'appointment':editapppointment})

def update(request,id):
    updateinfo=Appointment.objects.get(id=id)
    form = AppoitmentForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        members=Member(
            name=request.POST['name'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')


