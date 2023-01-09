## multivendor-ecommerce
Membuat aplikasi multivendor online food


## 02. Persiapan

#### 02.0. Pendahuluan
#### 02.1. Menginstal Python
#### 02.2. Menginstall pip dan virtualenv
#### 02.3. Menginstal Text Editor
#### 02.4. Menginstal PostgreSQL
#### 02.5. Membuat Github repositori
#### 02.6. Clone Github repositori
#### 02.7. Testing - Modifikasi .gitignore dan readme file

        modified:   .gitignore
        modified:   README.md


## 03. Membuat Proyek Django 

#### 03.0. Pendahuluan
		pass

#### 03.1. Membuat virtual environment

        modified:   README.md

#### 03.2. Menginstal django

       modified:   README.md

       NOTE:

       Tiga langkah untuk menginstal django:

       1. Membuat virtual environment
       2. Mengaktifkan virtual environment
       3. Menginstal django  

#### 03.3. Membuat proyek django

        Perintah untuk membuat proyek django dengan nama 'config'
        (venv3932) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

#### 03.4. Hello World!

        modified:   README.md
        modified:   config/urls.py
        new file:   config/views.py

        Testing :   Start server dan buka browser http://127.0.0.1:8000/
        Hasil   :   Hallo World!


## 04. Django Urls, Views dan Templates

#### 04.0. Pendahuluan
        pass

#### 04.1. Aktifasi django templates

        modified:   README.md
        modified:   config/settings.py

#### 04.2. Membuat homepage

        modified:   README.md
        modified:   config/views.py
        new file:   templates/home.html

#### 04.3. Mengisi html template untuk homepage

        modified:   README.md
        modified:   templates/home.html

#### 04.4. Konfigurasi file statis

        modified:   README.md
        modified:   config/settings.py

#### 04.5. Loading file statis

        modified:   .gitignore
        modified:   README.md
        modified:   templates/home.html

        Aktivitas:

        1. Menambahkan assets pada static folder
        2. Loading static files: {% load statci %} {% static 'assets/....' %}
        3. Testing: start local server dan buka browser
        4. Hasil: ok

#### 04.6. Template inheritance basic

        modified:   README.md
        new file:   templates/base.html
        modified:   templates/home.html

        Aktivitas:

        1. Pada templates folder membuat base.html
        2. Memindahkan seluruh html template pada home.html ke base.html
        3. Pada home.html membuat block tag: extends base.html, load static, dan block content
        4. Memindahkan bagian main section pada base.html ke home.html
        5. Membuat block tag: block content pada main section pada base.html
        6. Testing: start local server dan buka browser
        7. Hasil: ok

#### 04.7. Partials dan include

        modified:   README.md
        new file:   TOC-MODIFIED-COPY
        modified:   templates/base.html
        new file:   templates/partials/footer.html
        new file:   templates/partials/header.html

        Aktivitas:

        1. Dalam templates membuat folder partials: templates/partials
        2. Membuat 2 files pada folder partials: header.html dan footer.html
        3. Memindahkan bagian header pada base.html ke header.html
        4. Memindahkan bagian footer pada base.html ke footer.html
        5. Meng-include header.html dan footer.html pada base.html
        6. Testing: start local server dan buka browser
        7. Hasil: ok

#### 04.8. Testing
        
        Ok
        
#### 04.9. Github

        (venv3932) λ git push origin
        Enter passphrase for key '/c/Users/hp/.ssh/id_rsa':



## 04. Database
================

#### 04.1. Membuat Progres database

        modified:   README.md

        Aktivitas:

        1. Mengaktifkan postgres server
        2. Membuat database
        3. Testing: Database berhasil dibuat
        4. Hasil: ok

#### 04.2. Menghubungan Postgres dan Django 

        (venv3932) λ pip install psycopg2

        modified:   README.md
        modified:   config/settings.py

        Aktivitas:

        1. Menginstal db posgres driver: pip install psycopg2
        2. Menghubungkan proyek dgn db dgn embuat konfigurasi db pada settings.py
        3. Testing: Jalankan server
        4. Hasil: ok

#### 04.3. Melindungi sensitif file

        (venv3932) λ pip install django-decouple

        new file:   .env-example
        modified:   README.md
        modified:   config/settings.py

        Aktivitas:

        1. Menginstal django-decouple: pip install django-decouple
        2. Membuat file: .env dan .env-exampel
        3. Membuat konfigurasi db pada .env file
        4. Mengafilikasikan konfigurasi db pada settings.py
        5. Testing: Jalankan server
        6. Hasil: ok

#### 04.4. Testing

        Menjalankan server. 
        Hasil Ok

#### 04.5. Github

        (venv3932) λ git push origin
        Enter passphrase for key '/c/Users/hp/.ssh/id_rsa':
        modified:   README.md

#### Modifikasi file

        modified:   TOC-MODIFIED-COPY

#### House cleaning

        modified:   README.md
        deleted:    TOC-MODIFIED-COPY


## 06. Membuat Django App

#### 06.0. Pendahuluan

        pass 

#### 06.1. Membuat django app

        (venv3932) λ mkdir app\accounts
        (venv3932) λ django-admin startapp accounts app\accounts

        modified:   README.md
        new file:   app/accounts/__init__.py
        new file:   app/accounts/admin.py
        new file:   app/accounts/apps.py
        new file:   app/accounts/migrations/__init__.py
        new file:   app/accounts/models.py
        new file:   app/accounts/tests.py
        new file:   app/accounts/views.py

        Aktivitas:

        1. Membuat folder di dalam root proyek: app/accounts
        2. Membuat django app dengan nama accounts

        NOTE:

        Semua django app akan ditempatkan di dalam satu folder app 

#### 06.2. Register django app

        modified:   README.md
        modified:   app/accounts/apps.py
        modified:   config/settings.py

        Aktivitas:

        1. Merubah nama app pada apps.py
        2. Register accounts app pada settings.py
        3. Testing: jalankan server
        4. Hasil: ok



## 07. Django Custom User Model

#### 07.0. Pendahuluan
#### 07.1. Membuat model UserManager

        modified:   README.md
        modified:   app/accounts/models.py

        Aktivitas:

        1. Membuat UserManager
        2. Testing: jalankan server
        3. Hasil: ok

#### 07.2. Membuat custom model User

        modified:   README.md
        modified:   app/accounts/models.py

        Aktivitas:

        1. Membuat custom User model
        2. Testing: jalankan server
        3. Hasil: ok

#### 07.3. Registrasi custom User

        Aktivitas:

        1. Meregistrasi cutom User model pada settings.py: AUTH_USER_MODEL = 'accounts.User'
        2. Testing: jalankan server
        3. Hasil: warning 'ValueError: Dependency on app with no migrations: accounts'
        
        modified:   README.md
        modified:   config/settings.py

        NEXT:

        Menjalankan migrasi

#### 07.4. Menjalankan migrasi

        modified:   README.md
        new file:   app/accounts/migrations/0001_initial.py

        Aktivitas:

        1. Menjalankan migrasi

        NEXT: Membuat superuser

#### 07.5. Membuat superuser

        modified:   README.md

        Aktivitas:

        1. Membuat superuser

        NEXT: Konfigurasi file media

#### 07.6. Testing
#### 07.7. Github


## 08. Django Admin

#### 08.0. Pendahuluan
#### 08.1. Konfigurasi file media

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py

        Aktivitas:

        1. Konfigurasi file media pada settings.py dan urls.py

        NEXT: menambahkan gambar untuk superuser

#### 08.2. Admin login 

        modified:   README.md
        modified:   app/accounts/admin.py

        Aktivitas:

        1. Register model User pada admin.py
        2. Admin login
        3. Testing: admin login
        4. Hasil: berhasil, tapi password masih bisa diedit.

        NEXT: Membuat password tidak bisa diedit.

#### 08.3. Membuat password tidak bisa diedit

        modified:   README.md
        modified:   app/accounts/admin.py

#### 08.4. Konfigur User fields pada admin panel

        class UserAdmin(UserAdmin):

            list_display = (
                'email', 'first_name', 
                'last_name', 'username', 'role', 'is_active')
            ordering = ('-date_joined',)    

            filter_horizontal = ()
            list_filter = ()
            fieldsets = ()

        admin.site.register(User, UserAdmin)

        modified:   README.md
        modified:   app/accounts/admin.py

        Aktivitas:

        1. Customise class UserAdmin
        2. Testing: refresh admin panel
        3. Hasil: ok

        NEXT: Membuat Django Signals

#### 08.5. Testing
#### 08.6. Github



## 09. Django Signals

#### 09.0. Pendahuluan
        pass

#### 09.1. Tentang user profile
        pass

#### 09.2. Membuat model UserProfile

        modified:   README.md
        modified:   app/accounts/admin.py
        new file:   app/accounts/migrations/0002_userprofile.py
        modified:   app/accounts/models.py

        Aktivitas:

        1. Membuat model UserProfile
        2. Menjalankan migrasi
        3. Registrasi model UserProfile pada accounts/admin.py
        4. Login dan add User profile dari superuser
        5. Testing: add profile untuk superuser
        6. Hasil: ok

        NOTE:

        1. Idealnya userprofile bisa secara otomatis dibuat ketika
           ada user baru yang melakukan registrasi.
        2. Hal pada poin 1 bisa dilakukan dengan menggunakan Django Signals

        NEXT:

        Membuat Django Signals

#### 09.3. Membuat Django Signals

        modified:   README.md
        modified:   app/accounts/models.py

        Aktivitas:

        1. Membuat Django Signals
        2. Testing: Membuat user baru
        3. Hasil: User baru berhasil dibuat dan userprofile juga berhasil dibuat secara otomatis.

        NOTE:

        1. Bila existing user diupdate, maka userprofile tidak ikut terupdate.
        2. Bila existing userprofile diupdate, maka existing user tsb ikut terupdate.
        3. Bila userprofile dihapus, user tidak ikut terhapus.
        4. Bila existing user diupdate, maka profilenya juga ikut terupdate scr otomatis.

        NEXT:

        Setup file media

        modified:   README.md
        modified:   app/accounts/models.py

#### 09.4. Mensetup file media

        modified:   README.md
        new file:   media/users/cover_photos/ing.jfif
        new file:   media/users/profile_pictures/ing.jfif

        Aktivitas:

        1. Add image untuk superuser
        2. Tesing: menambahkan gambar
        3. Hasil: gambar berhasil diupload dan folder media/users/cover_photos dan 
           media/users/profile_pictures
           
        NOTE:

        File media telah disetup pada: 08.1. Konfigurasi file media


#### 09.5. Django signals and ready() function

        modified:   README.md
        modified:   app/accounts/apps.py
        modified:   app/accounts/models.py
        new file:   app/accounts/signals.py

        Aktivitas:

        1. Membuat file baru: accounts/signals.py
        2. Pindahkan semua code signal dari account/models.py ke file signals.py
        3. Hapus semua kode signals pada models.py
        4. Pindahkan modules post_save, pre_save dan receiver ke signals.py
           dari models.py dan hapus mudul itu dari models.py
        5. Buat ready() function pada accounts/apps.py
        6. Testing: buat user baru
        7. Hasil: user baru dan profile user baru juga terbuat.

        NOTE: So far, so good.

        NEXT: Registrasi user

#### 09.6. Testing
#### 09.7. Github



## 10. Registrasi User Django Messages, dan Error

#### 10.0. Pendahuluan

        Penjelasan flow dari cara kerja Multi Vendor Food Online
        1. In comming random user (registered or not register user)
        2. If not register, he can register as customer or vendor

        REGISTER AS VENDOR

        3. Let say he will register as vendor
        4. A register form will be comes up
        5. Once he registered, the admin will verify it (give him a certificate) and give the approval or reject it
        6. Once admin approved, then he, as the vendor can login to our marketplace (note: the can distinguished vendor or customer)
        7. If he loged in as vendor, he will be redirect to vendor dashboard
        8. In the vendor dasboard, vendor can do CRUD operation for his: profile, location and restaurant timing
        9. Vendor create or build menu and publish it to the marketplace (here is the critical part of the app)

        REGISTER AS CUSTOMER

        10. Register as customer
        11. Log in as customer
        12. Once he loged in, he can visit the marketplace or Customer dashboard
        13. If he go to customer dashboar, he will be able to: update profile, check order, sign out    
        14. If he go to the marketplace, he can order the food
        15. In the marketplace, customer can search restaurant by location (near by location) or key words (by rest name, for example)
        16. Once he happy with the search, he will be able to order, showed the cart, and make payment
        17. If the payment is failed, the the app will show him again the cart
        18. Once the payment is success, the app will deduct it for the admin commision (some percentage of the amount) 
        19. Admin will receive the commision, then clear the cart and send emil to the customer (we have take care the order)
        20. At the same time, we will send email to the restauran that he got a new order
        21. Once the restaurant owner open the email, the transaction can be procceded: except or reject the order

#### 10.1. Register user - Part 1: urls, views with HttpResponse

        modified:   README.md
        new file:   app/accounts/urls.py
        modified:   app/accounts/views.py
        modified:   config/urls.py

        Aktifitas:

        1. Membuat path register-user pada: app/accounts/urls.py
        2. Include app/accounts/urls.py pada: config/urls.py
        3. Membuat register-user views pada: app/accounts/views.py.
           views.py menampilkan: return HttpResponse('Register user here ..')
        4. Testing: buka browser, http://127.0.0.1:8000/accounts/register-user
        5. Hasil: ok

        NEXT: Template untuk user register  


#### 10.2. Register user - Part 2: Urls, Views, Templates

        modified:   README.md
        modified:   app/accounts/views.py
        new file:   templates/app/accounts/register-user.html

        Aktifitas:

        1. Modifikasi app/accounts/views.py: return render(request, 'app/accounts/register-user.html')
        2. Pada templates, membuat: templates/app/accounts/register-user.html
        3. Mengisi text <h1>Register User</h1> pada register-user.html
        4. Testing: refresh browser
        5. Hasil: ok

        NEXT: Mengisi form template pada register-user.html


#### 10.3. Register user - Part 3: Mengisi form template pada laman register

        modified:   README.md
        modified:   templates/app/accounts/register-user.html

        Aktifitas:

        1. Mengisi form template pada laman register-user
        2. Testing: refresh browser
        3. Hasil: ok

        NEXT: Django form


#### 10.4. Register user - Part 4: Menggunakan Django Model Forms untuk membuat form fields

        modified:   README.md
        new file:   app/accounts/forms.py
        modified:   app/accounts/views.py
        modified:   templates/app/accounts/register-user.html

        Aktifitas:

        1. Membuat file baru: app/accounts/forms.py
        2. Menggunakan django ModelForm untuk membuat form

                from django import forms

                # Local
                from app.accounts.models import User

                class UserRegistrationForm(forms.ModelForm):
                        class Meta:
                                model = User
                                fields = [
                                        'first_name', 'last_name', 
                                        'username', 'email', 'phone_number', 'password'
                                ]

        3. Menggukan model UserRegistrationForm pada views
        4. Menampilkan form instan pada register-user
        5. Tesing: refresh browser
        6. Hasil: ok

        NOTE:

        1. Form tidak berisi input untuk konfirm password.
        2. Form juga tidak berisi widget untuk styling

        NEXT: Menambahkan field password dan confirm password dan form widget pada UserRegistrationForm


### 10.5 Register user - Part 5: Loading form instan dari register_user views pada laman register-user

        modified:   README.md
        modified:   app/accounts/forms.py
        modified:   templates/app/accounts/register-user.html

        Aktivitas:

        1. Menambahkan form field pada UserRegistrationForm model
        2. Loading form instan pada laman register-user
        3. Testing: refresh browser
        4. Hasil: ok

        NOTE: 

        Form belum bisa dipakai untuk register user karena belum ada logiknya pada register_user() view function

        NEXT:

        Membuat logik pada register_user() view function


#### 10.6 Register user - Part 6: Membuat basik logik pada register_user() view function

        modified:   README.md
        modified:   app/accounts/views.py
        modified:   templates/app/accounts/register-user.html

        Aktivitas:

        1. Membuat basik logik pada register_user()
        2. Menambahkan path action pada register-user form
        3. Testing: register a user
        4. Hasil: error, namun data yang diinput pada form berhasil ditangkap pada terminal

        NOTE: Tujuan pada basik logik adalah untuk menangkap form input pada terminal

        NEXT: Memodifikasi basik logik pada register_user()


#### 10.7 Register user - Part 7: Membuat detail register_user() logik pada views

        modified:   README.md
        modified:   app/accounts/views.py

        Aktivitas:

        1. Membuat detail register user logik pada register_user() logik pada views
        2. Testing: register a new user
        3. Hasil: user baru dan profilnya berhasil disimpan di dalam db

        NOTE: 

        1. User yang diregister bersifat any user, tidak memiliki role.
        2. Karena any user, maka tidak bisa dibedakan apakah rolenya sbg Customer atau Vendor

        NEXT: 

        Mendefinisikan user role


