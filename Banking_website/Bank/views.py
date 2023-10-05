from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import BankForm, AllDist, AllBranch
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def new(request):
    return render(request, 'New.html')


def bank_form(request):
    try:
        if request.method == 'POST':
            name = request.POST['name']
            dob = request.POST['DOB']
            age = request.POST['age']
            pn = request.POST['pn']
            address = request.POST['address']
            gender = request.POST['inlineRadioOptions']
            email = request.POST['email']
            dist = request.POST['dist']
            branch = request.POST['branch']
            material = request.POST['cc']
            errors = []
            if not (name or dob or age or pn or address or gender or email or dist or material):
                errors.append('All fields are empty. Please fill in at least one field.')

            if not name:
                errors.append('Name is required.')

            if not dob:
                errors.append('Date Of Birth is required.')

            if not age:
                errors.append('Age is required.')

            if not pn:
                errors.append('Phone number is required.')

            if not address:
                errors.append('Address is required.')

            if not gender:
                errors.append('gender is required.')

            if not email:
                errors.append('Email is required.')

            if not dist:
                errors.append('District is required.')

            if not branch:
                errors.append('Branch is required.')

            if not material:
                errors.append('Material provided is required.')
            if errors:
                return JsonResponse({'success': False, 'errors': errors})
            else:
                form_bank = BankForm(Name=name, DOB=dob, Age=age, Phone=pn, Address=address, Gender=gender, Email=email,
                                     District=dist, Branch=branch, Credit_card=material)
                form_bank.save()
                print('successfuy save')
                return JsonResponse({'success': True})
    except:
        messages.info(request,'All fields are required')
    return render(request, 'Form.html')


def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = AllBranch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse({'branches': list(branches)})
