from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Staff, SiteAdmin, Services
from .forms import AdminForm, StaffForm, ServiceForm

def index(request):
    return render(request, "login.html")

def login_for_access_token(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        staff = SiteAdmin.objects.filter(username=username).first()
        if staff and staff.password and staff.check_password(password):
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("dashboard")
            messages.error(request, "Invalid Credentials")
        else:
            messages.error(request, "Incorrect Username or Password")
    return redirect("index")


def logout_access_token(request):
    logout(request)
    return redirect("index")


def post_register_form(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect("index")
        else:
            for error in form.errors.values():
                messages.error(request, error)
    return redirect("index")

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
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("services")
        else:
            for error in form.errors.values():
                messages.error(request, error)
        
        if 'delete' in request.POST:
            get_object_or_404(Services, pk=request.POST.get("delete")).delete()
            return redirect("services")

    context = {
        "data": Services.objects.all(),
        "form": ServiceForm()
    }
    return render(request, "pages/services.html", context)

def settings(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/settings.html")

def staffs(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staffs")
        else:
            for error in form.errors.values():
                messages.error(request, error)
        
        if 'delete' in request.POST:
            get_object_or_404(Staff, pk=request.POST.get("delete")).delete()
            return redirect("staffs")
        
    context = {
        "data": Staff.objects.all(),
        "form": StaffForm()
    }
    return render(request, "pages/staff.html", context)

def get_one_staff(request, id: int):
    staff = Staff.objects.get(pk=id)
    return render(request, "pages/details.html", {"staff": staff})

def update_staff(request, id: int):
    pass

def transactions(request):
    return render(request, "pages/transactions.html")