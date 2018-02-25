from custom_user.models import AbstractEmailUser
from django.db import models



class CustomUserRole(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

# Create your models here.
class UserModel(AbstractEmailUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    full_name = models.CharField(max_length=30)

    #  Default action
    active = models.BooleanField(default=False)
    # role
    role = models.ForeignKey('CustomUserRole', related_name='user_role', on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return "%s" % self.full_name

    def return_role(self):
        return self.role.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.full_name = '{} {}'.format(self.first_name, self.last_name)
        super(UserModel, self).save(force_insert, force_update)


class UserDetails(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)

    #  Description of user
    avatar = models.ImageField(upload_to='user_avatar')

    #  Default action
    active = models.BooleanField(default=False)

    user = models.ForeignKey('UserModel', related_name='user_detail', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return "%s" % self.user.full_name
