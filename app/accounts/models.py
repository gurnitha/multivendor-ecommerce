# app/accounts/models.py

# Import django modules
from django.db import models
from django.contrib.auth.models import BaseUserManager

# Create your models here.

# Model: UserManager
class UserManager(BaseUserManager):

    '''create_user method, menggunakan 5 parameter:
    yaitu:first_name, last_name, username, email, dan password'''
    def create_user(self, first_name, last_name, username, email, password=None):
        # Email dan nama pengguna diperlukan
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        '''Jika semua field terpenuhi, simpan data ke dalam variabel user
        dan normalais karakter yang ada dalam email'''
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        # Simpan data ke dalam default db
        user.set_password(password)
        user.save(using=self._db)
        return user


    '''create_superuser method menggunakan 5 parameter:
    yaitu:first_name, last_name, username, email, dan password.
    ke-5 parameter ini diambil dari create_user method di atas.'''
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        # Simpan data ke dalam default db
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user