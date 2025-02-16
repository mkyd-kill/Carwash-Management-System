from django.urls import path
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    # auth paths
    path('accounts/login/', auth.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path("new-registration/", views.post_register_form, name="register-new"),
    path('logout/', auth.LogoutView.as_view(), name='logout'),

    # cms paths
    path("dashboard/", views.dashboard, name="dashboard"),
    path("clients/", views.clients, name="clients"),
    path("reports/", views.report, name="reports"),
    path("sales/", views.sales, name="sales"),
    path("services/", views.services, name="services"),
    path("accounts/profile/", views.settings, name="settings"),
    path("staffs/", views.staffs, name="staffs"),
    path("staff-details/<int:id>/", views.get_one_staff, name="details"),
    path("update-staff/<int:id>/", views.update_staff, name="update"),
    path("transactions/", views.transactions, name="transactions")
]