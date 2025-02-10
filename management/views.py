from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Staff, SiteAdmin
from .forms import AdminForm

def index(request):
    return render(request, "login.html")

def login_for_access_token(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        staff = get_object_or_404(SiteAdmin, username=username)
        if not staff:
            messages.error("User Not Registered")
            return redirect("index")
        
        if check_password(password, staff.hashed_password):
            login(request, staff.username)
            return redirect("dashboard")
    return redirect("index")


def logout_access_token(request):
    pass

def post_register_form(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)

        if form.is_valid():
            if SiteAdmin.objects.filter(username=form['username'].value()).exists():
                messages.error(request, "Username already taken. Try using another one.")
                return redirect("index")
        
            if SiteAdmin.objects.filter(email=form['email'].value()).exists():
                messages.error(request, "Email already taken. Try using another one.")
                return redirect("index")
            
            username = form['username'].value()
            email = form["email"].value()
            hashed_password = make_password(form['hashed_password'].value())
            
            site_admin = SiteAdmin.objects.create(username=username, hashed_password=hashed_password, email=email)
            site_admin.is_active = False
            site_admin.save()
            messages.success(request, "Account Created Successfully!!!")
            return redirect("index")
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
        pass
    return render(request, "pages/services.html")

def settings(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/settings.html")

def staffs(request):
    if request.method == 'POST':
        name = request.POST["name"]
        national_id = request.POST["staff_id"]
        email = request.POST["email"]
        gender = request.POST["gender"]
        role = request.POST["role"]
        department = request.POST["department"]
        contact = request.POST["contact"]
        commission = request.POST["commission"]
        salary = request.POST["salary"]
        status = request.POST['status']

        created_item = Staff.objects.create(
            name=name,
            national_id=national_id,
            email=email,
            gender=gender,
            contact=contact,
            commission=commission,
            salary=salary,
            status=status,
            role=role,
            department=department
        )
        created_item.save()
        return redirect("staffs")
    get_all_staff = Staff.objects.all()
    context = {
        "staffs": get_all_staff
    }
    return render(request, "pages/staff.html", context)

def get_one_staff(request, id: int):
    staff = Staff.objects.get(pk=id)
    if not staff:
        messages.error(request, f"Staff with staff_id: {id} Not Found")
        return redirect("staffs")
    return render(request, "pages/details.html", {"staff": staff})

def update_staff(request, id: int):
    pass

def delete_staff(request, id: int):
    staff = Staff.objects.get(id=id)
    staff.delete()
    return redirect("staffs")

def transactions(request):
    return render(request, "pages/transactions.html")