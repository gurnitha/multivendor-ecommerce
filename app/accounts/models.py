# app/accounts/models.py

# Import django modules
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.

'''Model: UserManager
UserManager model tidak akan membuat kolom apa pun di dalam database.'''
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


""" 
Tentang AbstractBaseUser:
AbstractBaseUser ini akan memberi Anda kontrol penuh terhadap
Django User model. Anda boleh melakukan apa pun yang Anda maui.
"""

'''Model: User
User model akan membuat kolom di dalam database.'''
class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    """
    About Login field:
    Django uses username as a login field by default.
    But we want to use email as login filed, instead of username.
    So we have to override the username.

    We also define the required fields: username, first_name, and last_name.
    So the required field is username.
    Email is also required field, but we don't need to put that email inside the required
    fields list because username field itself is a required field.
    So that's why we don't need to put email here. username, first_name and last_name
    also be required fields. 
    """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # To tell django which class to use. In this case we use UserManager class.
    # In the settings.py file we have to define to using User model
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
         verbose_name = "User"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    """
    About has_module_perms bellow:
    We'll return True if the user is an active superuser or is an admin.
    And for inactive users it will be always return false.
    That means by default, only admin and superadmin can have access to this model.
    """
    def has_module_perms(self, app_label):
        return True


# Model: UserProfile
class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


"""
Well, the signals are the utilities or feature that helps us 
to connect the events with the actions.
So this simply means that signals are used to perform some actions 
on every modification or creation of a particular entry in the database.

So the most common use cases of using signal is to automatically 
creating a profile instance as soon as the user is created.
"""

"""
About Receiver and Sender:

Receiver is a function, in this case: post_save_create_profile_receiver, 
it takes 4 parameters:
- sender (User),
- instance (that is something created by User),
- created (a boolean value, will show up when something is created), and
- **kwargs.
Sender is the User model itself.
"""

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    '''
    So as soon as the user is created, 
    or as soon as we get the response of created equal to true, 
    then what we need to do, we need to actually create the user profile.

    Steps:
    1. Check created flag is being true or false.
    2. If it is true, then create UserProfile
    '''
    print(created) # print something if user is created (True or False).
    if created:
        UserProfile.objects.create(user=instance)
        print('User profile is created')
        ''' User profile is created.
        So now we have to create profile instance
        to be able to update userprofile
        '''
    else:
        '''
        1. If User profile was updated, then 'created' is false.
        2. Create userprofile and save it.
        3. Jika userprofile dihapus, kemudian user di-update, akan terjadi error.
        4. Gunakan try block untuk menghindari situasi ini (poin 3).
        '''
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            print('Profile was not exist, but I created one')
        print('User is updated') 

@receiver(pre_save, sender=User)
def post_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, 'this user is being saved')

'''Bellow is the way to connect with the receiver.
But we will use @ (decocator), see above''' 
# post_save.connect(post_save_create_profile_receiver, sender=User)