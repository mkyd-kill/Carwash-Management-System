from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("token/", views.login_for_access_token, name="login-token"),
    path("logout/", views.logout_access_token, name="logout"),
    path("new-registration/", views.post_register_form, name="register-new"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("clients/", views.clients, name="clients"),
    path("reports/", views.report, name="reports"),
    path("sales/", views.sales, name="sales"),
    path("services/", views.services, name="services"),
    path("settings/", views.settings, name="settings"),
    path("staffs/", views.staffs, name="staffs"),
    path("staff-details/<int:id>/", views.get_one_staff, name="details"),
    path("update-staff/<int:id>/", views.update_staff, name="update"),
    path("transactions/", views.transactions, name="transactions")
]