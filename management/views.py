from django.shortcuts import render, redirect
from .forms import DataForm

def index(request):
    return render(request, "login.html")

def login_for_access_token(request):
    pass

def logout_access_token(request):
    pass

def post_register_form(request):
    if request.method == 'POST':
        form = DataForm(request.POST)

def dashboard(request):
    return render(request, "pages/dashboard.html")

def clients(request):
    return render(request, "pages/clients.html")

def report(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/reports.html")

def sales(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/sales.html")

def services(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/services.html")

def settings(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/settings.html")

def staffs(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/staff.html")

def get_one_staff(request, id: int):
    return render(request, "pages/details.html")

def transactions(request):
    return render(request, "pages/transactions.html")