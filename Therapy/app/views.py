from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
from .models import Contact  # Ensure this matches your app structure

# Create your views here.
def index(request):
    return render(request,'index.html')


# def contact(request):

# View to handle form submission and save contact info

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
