from django.conf.urls import url

from core.register.views import register

urlpatterns = [
    url('^register', register, name="register"),

]
