from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, email, last_name, first_name, telephone, gender, birthdate, password=None):
        if not email:
            raise ValueError('Le champ email doit être sélectionné.')

        user = self.model(
            email=self.normalize_email(email),
            last_name=last_name,
            first_name=first_name,
            telephone=telephone,
            gender=gender,
            birthdate=birthdate
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, last_name, first_name, telephone, gender, birthdate, password=None, ):
        """
        Creates and saves a superuser with the given email, email and password.
        """
        user = self.create_user(
            email,
            password=password,
            last_name=last_name,
            first_name=first_name,
            telephone=telephone,
            gender=gender,
            birthdate=birthdate,
        )

        user.is_admin = True
        user.is_active = True
        # user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user


class Shopper(AbstractBaseUser):
    email = models.EmailField(unique=True)
    last_name = models.CharField("Nom", max_length=30)
    first_name = models.CharField("Prénoms", max_length=100)
    telephone = PhoneNumberField()
    gender = models.CharField(max_length=10)
    birthdate = models.DateField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'last_name',
        'first_name',
        'telephone',
        'gender',
        'birthdate'
    ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
