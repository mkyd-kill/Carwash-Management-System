from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Staff, Services
from .forms import StaffForm, ServiceForm, AdminCreationForm

def post_register_form(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)

        if form.is_valid():
            staff = form.save()
            if staff:
                return redirect("login")
    else:
        form = AdminCreationForm()
    return render(request, 'auth/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, "pages/dashboard.html")

@login_required
def clients(request):
    return render(request, "pages/clients.html")

@login_required
def report(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/reports.html")

@login_required
def sales(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/sales.html")

@login_required
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

@login_required
def settings(request):
    if request.method == 'POST':
        pass
    return render(request, "pages/settings.html")

@login_required
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

@login_required
def get_one_staff(request, id: int):
    staff = Staff.objects.get(pk=id)
    return render(request, "pages/details.html", {"staff": staff})

@login_required
def update_staff(request, id: int):
    pass

@login_required
def transactions(request):
    return render(request, "pages/transactions.html")