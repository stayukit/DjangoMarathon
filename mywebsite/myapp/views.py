from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from django.urls import reverse_lazy, reverse
from .models import Staff, Product, CustomerForm

def Homepage(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'myapp/home.html', context)

def About(request):
    return render(request, 'myapp/about.html')

def Products(request):
    return render(request, 'myapp/products.html')

def Services(request):
    return render(request, 'myapp/services.html')

def Contact(request):
    namelist = Staff.objects.all()
    context = {'namelist':namelist}
    if request.method == 'POST':
        data = request.POST.copy()
        print('Data', data)
        name = data.get('name')
        title = data.get('title')
        email = data.get('email')
        detail = data.get('detail')
        new_case = CustomerForm()
        new_case.name = name
        new_case.title = title
        new_case.email = email
        new_case.detail = detail
        print('test', name, title, email, detail)
        new_case.save()
        context['alert'] = 'success'
    
    return render(request, 'myapp/contact.html', context)