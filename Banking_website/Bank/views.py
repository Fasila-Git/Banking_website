from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import BankForm,AllDist,AllBranch
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request, 'Home.html')


def new(request):
    return render(request, 'New.html')


def bank_form(request):
    if request.method == 'POST':
        try:
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
            form_bank = BankForm(Name=name, DOB=dob, Age=age, Phone=pn, Address=address, Gender=gender, Email=email,
                                 District=dist, Branch=branch, Credit_card=material)
            form_bank.save()
            messages.info(request, "Successfully submitted")
        except:
            messages.info(request, "All fields are required")
    return render(request, 'Form.html')




def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = AllBranch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse({'branches': list(branches)})


