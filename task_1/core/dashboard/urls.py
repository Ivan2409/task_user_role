from django.conf.urls import url

from core.dashboard.views import dashboard

urlpatterns = [
    url(r'^dashboard', dashboard, name="dashboard")
]