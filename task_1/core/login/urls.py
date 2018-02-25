from django.conf.urls import url

from core.login.views import login, logout

urlpatterns = [
    url('^login', login, name="login"),
    url('logout', logout, name="logout"),
]