from django.shortcuts import render, HttpResponse,get_object_or_404,redirect
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
from .models import Contact,Appointment 

# Create your views here.
def index(request):
    return render(request,'index.html')

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')  # Use lowercase 'message'

        if not name or not email or not phone or not message:
            return JsonResponse({"errors": "All fields are required!"}, status=400)

        try:
            contact_instance = Contact(name=name, email=email, phone=phone, message=message)  # Use 'message'
            contact_instance.save()
            return JsonResponse({"message": "Contact submitted successfully!"})
        except Exception as e:
            return JsonResponse({"errors": str(e)}, status=400)

    return JsonResponse({"errors": "Invalid request method."}, status=400)


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()  
    return redirect('contact_list')  




def appointment_view(request):
    if request.method == 'POST':
        # Extract form data from request
        service = request.POST.get('service')
        date = request.POST.get('date')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Validate required fields
        if not service or not date or not first_name:
            return JsonResponse({"errors": "Service, Date, and First Name are required!"}, status=400)

        try:
            # Save the data in the database
            appointment = Appointment(
                service=service,
                date=date,
                first_name=first_name,
                last_name=last_name
            )
            appointment.save()
            return JsonResponse({"message": "Appointment created successfully!"})
        except Exception as e:
            return JsonResponse({"errors": str(e)}, status=400)

    return render(request, 'index.html')



def show_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})


def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.method == 'POST':
        appointment.service = request.POST.get('service')
        appointment.date = request.POST.get('date')
        appointment.first_name = request.POST.get('first_name')
        appointment.last_name = request.POST.get('last_name')
        appointment.save()

        return redirect('show_appointments')

    return render(request, 'edit_appointment.html', {'appointment': appointment})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()

    return redirect('show_appointments')
