from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email,username, firstname,lastname,password=None):
        if not email:
            raise ValueError("user must have an email")
        if not username:
            raise ValueError("must have an username")
        if not firstname:
            raise ValueError("must have a firstname")
        if not lastname:
            raise ValueError("must have a lastname")
        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username,firstname,lastname, password):
        user = self.create_user(
            email,
            password=password,
            username=username,
            firstname=firstname,
            lastname=lastname
        )
        user.staff = True
        user.admin = True
        user.superuser = True
        user.save(using=self._db)
        return user

class user(AbstractBaseUser):
    email=models.EmailField(verbose_name='email',max_length=80,unique=True)
    username=models.CharField(max_length=50,unique=True)
    firstname=models.CharField(max_length=50,unique=True)
    lastname=models.CharField(max_length=50,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','firstname','lastname'] 

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_firstname(self):
        return self.firstname

    def get_lastname(self):
        return self.lastname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True