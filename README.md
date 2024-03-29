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

#### [02.7. Testing - Modifikasi .gitignore dan readme file](https://github.com/gurnitha/multivendor-ecommerce/commit/1eb73f3635082add48e4bce80ca1a4aac8cf048c)

        modified:   .gitignore
        modified:   README.md


## 03. Membuat Proyek Django 


#### 03.0. Pendahuluan
                pass


#### [03.1. Membuat virtual environment](https://github.com/gurnitha/multivendor-ecommerce/commit/9cca05374dd053af7fe2f6644bb8a81a7d72261b)

        modified:   README.md


#### [03.2. Menginstal django](https://github.com/gurnitha/multivendor-ecommerce/commit/5e9181f863ccb55599836a5839347e4b9c0b8950)

       modified:   README.md

       NOTE:

       Tiga langkah untuk menginstal django:

       1. Membuat virtual environment
       2. Mengaktifkan virtual environment
       3. Menginstal django  


#### [03.3. Membuat proyek django](https://github.com/gurnitha/multivendor-ecommerce/commit/046ba7546d07780712c6069ada65408717e0c87a)

        Perintah untuk membuat proyek django dengan nama 'config'
        (venv3932) λ django-admin startproject config .

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### [03.4. Hello World!](https://github.com/gurnitha/multivendor-ecommerce/commit/a824ec117fb0323e4c534128969f482ee20a75fb)

        modified:   README.md
        modified:   config/urls.py
        new file:   config/views.py

        Testing :   Start server dan buka browser http://127.0.0.1:8000/
        Hasil   :   Hallo World!


## 04. Django Urls, Views dan Templates


#### 04.0. Pendahuluan
        pass


#### [04.1. Aktifasi django templates](https://github.com/gurnitha/multivendor-ecommerce/commit/d96c55d100f702cf3ea4f1b7550edac4bc43182a)

        modified:   README.md
        modified:   config/settings.py


#### [04.2. Membuat homepage](https://github.com/gurnitha/multivendor-ecommerce/commit/a601e22f79cdcc2a4da27300eab939ebe064bf0c)

        modified:   README.md
        modified:   config/views.py
        new file:   templates/home.html


#### [04.3. Mengisi html template untuk homepage](https://github.com/gurnitha/multivendor-ecommerce/commit/bda202ca2b7d6ac7405de0d4fec579494333f179)

        modified:   README.md
        modified:   templates/home.html


#### [04.4. Konfigurasi file statis](https://github.com/gurnitha/multivendor-ecommerce/commit/8c07244a9073afcbfc0de86723ec2830d0ec5f2b)

        modified:   README.md
        modified:   config/settings.py


#### [04.5. Loading file statis](https://github.com/gurnitha/multivendor-ecommerce/commit/6c42836b20f8a045de2c31b09e1557c39f35cdf1)

        modified:   .gitignore
        modified:   README.md
        modified:   templates/home.html

        Aktivitas:

        1. Menambahkan assets pada static folder
        2. Loading static files: {% load statci %} {% static 'assets/....' %}
        3. Testing: start local server dan buka browser
        4. Hasil: ok


#### [04.6. Template inheritance basic](https://github.com/gurnitha/multivendor-ecommerce/commit/35ff800e472a0ae266edd2de48b5d892f8a7cc54)

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


#### [04.7. Partials dan include](https://github.com/gurnitha/multivendor-ecommerce/commit/675e15c28b129b8993d1d4a61748859b0625cde2)

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



## 05. Database


#### 05.1. Membuat Progres database

        modified:   README.md

        Aktivitas:

        1. Mengaktifkan postgres server
        2. Membuat database
        3. Testing: Database berhasil dibuat
        4. Hasil: ok


#### 05.2. Menghubungan Postgres dan Django 

        (venv3932) λ pip install psycopg2

        modified:   README.md
        modified:   config/settings.py

        Aktivitas:

        1. Menginstal db posgres driver: pip install psycopg2
        2. Menghubungkan proyek dgn db dgn embuat konfigurasi db pada settings.py
        3. Testing: Jalankan server
        4. Hasil: ok


#### 05.3. Melindungi sensitif file

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


#### 05.4. Testing

        Menjalankan server. 
        Hasil Ok


#### 05.5. Github

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
        pass


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
        pass


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


## 10. Registrasi User Sebagai Customer


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


#### 10.5 Register user - Part 5: Loading form instan dari register_user views pada laman register-user

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


#### 10.8 Register user - Part 8: Mendefinisikan user role

        modified:   README.md
        modified:   app/accounts/models.py
        modified:   app/accounts/views.py

        Aktivitas:

        1. Mendefinisikan fungsi get_role User model
        2. Mendefinisikan role sebagai Customer pada register_user() view method
        3. Testing: register user baru
        4. Hasil: test berhasil

        NOTE:

        1. Walaupun registrasi berhasil, namun format password yang dihasilkan
           tidak standar:  Invalid password format or unknown hashing algorithm.

        NEXT: Hash password


#### 10.9 Register user - Part 9: Hash password

        modified:   README.md
        modified:   app/accounts/views.py

        Aktivitas:

        1. Menambahkan logik pada register_user() untuk hash password.
        2. Testing: register user baru.
        3. Hasil: user baru dan profilnya berhasil disimpan di dalam db dengan hash password

        NOTE:

        1. Kita telah berhasil meregistrasi user dengan menggunakan form method.
        2. Kita belum mencoba meregistrasi user dengan menggunakan create_user method.

        NEXT:

        Meregistrasi user dengan menggunakan create_user method.


#### 10.10 Register user - Part 10: Meregistrasi user menggunakan create_user method

        modified:   README.md
        modified:   app/accounts/views.py

        Aktivitas:

        1. Memodifikasi register_user() view functions, menggunakan create_user() method.
        2. Testing: Membuat user baru.
        3. Hasil: ok

        NOTE: Data pada form tetap tinggal setelah submit the form 

        NEXT: Menghapus data pada form setelah form disubmit


#### 10.11 Register user - Part 11: Final membersihkan form dari data input

        modified:   README.md
        modified:   app/accounts/views.py

        Aktivitas:

        1. Modifikasi register_user() method dengan menambahkan: return redirect('accounts:register_user')
        2. Testing: register user baru
        3. Hasil: Ok

        NOTE: Bila terjadi kesalahan registrasi, tidak ada tanda alert atau error yang diperlihatkan.

        NEXT: Memperlihatkan error


## 11. Showing Errors: Field and Non Field Error


#### 11.1. Pendahuluan

        FIELD ERROR

        In simple words, any errors that are associated with your model fields are called field errors.

        NONE FIELD ERROR

        These non field errors are the errors that are not associated with your model field, but they are associated
        with your form's clean method where you raise your own custom validation errors from the form level
        itself without attaching these fields into your model.
        So that's what we call the non field errors.

        The best example for this non field error is actually the confirm password.
        So in our case, if I type a different password in this password and confirm password fields, then
        this should actually give us an error saying password password do not match.

        So this password has to be same.
        Then we will be allowed to submit this form, otherwise we will get an error.
        So that kind of error is called the non field error.


#### 11.2. Showing field error pada terminal menggunakan existing email dan username

        modified:   README.md
        modified:   app/accounts/views.py

        Aktivitas:

        1. Modifikasi register_user() view function dengan menambahkan ini:

                else:
                        print('invalid form')
                        print(form.errors)

        2. Testing: Register user yang sudah ada di dalam database
        3. Hasil: 

        invalid form
        User with this Username already exists.
        User with this Email already exists.

        NOTE: 

        1. Error diperlihatkan pada terminal.
        2. Idealnya, error bisa diperlihatkan pada form.

        NEXT: Memperlihatkan error pada form


#### 11.3. Showing field error pada form menggunakan existing email dan username

        modified:   README.md
        modified:   templates/app/accounts/register-user.html

        Aktivitas:

        1. Looping error pada laman register-user, spt di bawah ini:

                <ul class="errorlist">
                    {% for field in form %}
                        {% if field.errors %}
                            {% for error in field.errors %}
                                <li style="color: red;">{{error}}</li>
                            {% endfor %}
                        {% endif %}
                    {% endfor %}
                </ul>

        2. Testing: Register user yang sudah ada di dalam db.
        3. Hasil: Error diperlihatkan pada laman form.

        NOTE:

        1. Data yang diinput seharusnya dibersihkan terlebih dahulu sebelum disimpan di dalam db.
        2. Django memiliki module CLEAN METHOD untuk membersihkan data input.

        NEXT: Membersihkan data input menggunakan Django CLEAN METHOD.


#### 11.4. Showing NON field error 

        modified:   README.md
        modified:   app/accounts/forms.py
        modified:   templates/app/accounts/register-user.html

        Aktivitas:

        1. Konfigur CLEAN METHOD pada UserRegistrationForm()
        2. Tambahkan error list pada form:  <li style="color: red;">{{form.non_field_errors}}</li>
        3. Testing: Membuat user baru dgn password yang berbeda dan password yang sama.
        4. Hasil: password beda, ada peringatan dan register gagal. Sedangkan password sama, ok.

        NEXT: Menggunakan Django Messages


## 12. Django Messages


#### 12.1. Pendahuluan

        We need to actually check if we have a message or not message
        If messages.
        If messages and we'll be wondering how this messages is available in this register user
        dot HTML because if you see this view we are not passing anything except form to this HTML.
        But still we are able to access these messages. So that because of this context processors
        in the settings.py file (inside the TEMPLATES).

        So this context processor is something. It's kind of a function.
        And when you write or when you return something inside the context processor, those module
        will be available in all of your HTML files.


#### 12.2. Setup django messages in views and register page

        modified:   README.md
        modified:   app/accounts/views.py
        modified:   templates/app/accounts/register-user.html

        Aktivitas:

        1. Konfigur django massages pada register_user() view method.
        2. Konfigur (loop) message pada register-user page, spt ini:

            <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
                {% if messages %}
                    {% for message in messages %}
                        <div class="alert alert-success" role="alert">
                            {{ message }}
                        </div>
                    {% endfor %}
                {% endif %}
            </div>

        3. Testing: Buat user baru
        4. Hasil: Bila password tidak sama, ada peringatan. Sebaliknya ada pesan sukses.

        NOTE:

        1. Agar massage bisa digunakan pada laman-laman lain, sebaiknya dibuat file khusus untuk massage.

        NEXT: Buat file khusus untuk massage.


#### 12.3. Using template inheritance (include) to show messages

        modified:   README.md
        modified:   templates/app/accounts/register-user.html
        new file:   templates/partials/alerts.html

        Aktivitas:

        1. Membuat file baru alerts: templates/partials/alerts.html
        2. Memindahkan django massage dari laman register_user ke alerts.html
        3. Include alerts.html pada laman register_user
        4. Testing: membuat user baru
        5. Hasil: Sama seperti sebelumnya, bila password tidak sama, ada peringatan. 
           Sebaliknya ada pesan sukses.

        NOTE:

        1. Massage tidak bisa di-close karena tidak ada tombol untuk menutupnya.

        NEXT: Menambahkan close button pada massage


#### 12.4. Menambahkan close button page alert message

        modified:   README.md
        modified:   templates/partials/alerts.html

        Aktivitas:

        1. Menambahkan close button pada alerts.html
        2. Testing: membuat user baru
        3. Hasil: Sama seperti sebelumnya, bila password tidak sama, ada peringatan. 
           Sebaliknya ada pesan sukses.

        NOTE: 

        1. Alert massage sangat statis.
        2. Agar lebih menarik, buat alert massage dinamis.

        NEXT: Animasi alerts massage


## 13. Animasi Messages


#### 13.1. Animate alert message dengan CSS

        modified:   README.md
        modified:   templates/base.html
        modified:   templates/partials/alerts.html

        Aktivitas:

        1. Membuat file custom.css
        2. Tambahkan pada file tsb css untuk animasi
        3. Load custom.css pada base.html
        4. Buat class show-notification pada alerts.html
        5. Testing: buat user baru
        6. Hasil: Animasi alert bekerja setelah sukses register user baru

        NOTE:

        Animasi alert dapat ditampilkan dengan menggunakan Django Tag

        NEXT: Gunakan Django Tag untuk animasi alert


#### 13.2. Display alert menggunakan Django message tag

        modified:   README.md
        modified:   config/settings.py
        modified:   templates/partials/alerts.html

        Aktivitas:

        1. Registrasi django tag massage pada settings.py
        2. Konfigur klass alert pada alerts.html
        3. Testing: membuat user baru
        4. Hasil: berhasil


#### Modified Readme file - forgot to save in 13.2

        modified:   README.md


## 14. Vendor


#### 14.0. Pendahuluan
        pass


#### 14.1. Membuat vendor app

        modified:   README.md
        new file:   app/vendor/__init__.py
        new file:   app/vendor/admin.py
        new file:   app/vendor/apps.py
        new file:   app/vendor/migrations/__init__.py
        new file:   app/vendor/models.py
        new file:   app/vendor/tests.py
        new file:   app/vendor/views.py
        modified:   config/settings.py

        Aktivitas:

        1. Membuat folder baru: app/vendor
        2. Membuat django app 'vendor'
        3. Delete registered vendor app in settings.py 
           (forgot to delete it when removed the vendor app)


#### 14.2. Register vendor app pada settings.py

        modified:   README.md
        modified:   app/vendor/apps.py
        modified:   config/settings.py

        Aktivitas:

        1. Konfigur appname pada apps.py: 
           dari:  name = 'vendor'
           menjadi: name = 'app.vendor'
        2. Register vendor app pada settings.py

        NEXT: Membuat Vendor model


#### 14.3. Membuat Vendor model

        modified:   app/vendor/admin.py
        new file:   app/vendor/migrations/0001_initial.py
        modified:   app/vendor/models.py

        Aktivitas:

        1. Membuat Vendor model
        2. Menjalankan migrasi
        3. Register Vendor model pada admin.py
        4. Testing: jalankan server dan login admin
        5. Hasil: Vendor model berhsil

        NEXT: Register vendor

        
#### 14.4. Register vendor: urls, views, templates

        modified:   README.md
        modified:   app/accounts/urls.py
        modified:   app/accounts/views.py
        new file:   templates/app/accounts/register-vendor.html

        Aktivitas:

        1. Membuat path
        2. Membuat register_vendor() view function
        3. Membuat file baru: templates/app/accounts/register-vendor.html
        4. Menambahkan text Register Vendor pada laman register-vendor
        5. Testing: buka browser: http://127.0.0.1:8000/accounts/register-vendor/
        6. Hasil: laman register-vendor berhasil ditampilkan

        NEXT: Mengisi template laman register-vendor


#### 14.5. Mengisi register-vendor dengan html template
 
        modified:   README.md
        modified:   templates/app/accounts/register-vendor.html

        Aktivitas:

        1. Mengisi tempate

        NEXT:

        Membuat VendorRegistrationForm class


#### 14.6. Membuat VendorRegistrationForm class

        modified:   README.md
        new file:   app/vendor/forms.py

        Aktivitas:

        1. Membuat file baru: app/vendor/forms.py
        2. Membuat VendorRegistrationForm class

        NEXT: Use VendorRegistrationForm class pada register_vendor() view function


#### 14.7 Kombiansi data form vendor dan customer - create user  

        modified:   README.md
        modified:   app/accounts/admin.py
        modified:   app/accounts/forms.py
        modified:   app/accounts/models.py
        modified:   app/accounts/signals.py
        modified:   app/accounts/views.py
        modified:   app/vendor/forms.py
        modified:   templates/app/accounts/register-user.html
        modified:   templates/app/accounts/register-vendor.html

        Aktivitas:

        1. Menyamakan posisi git repo dengan multivendor_food_online (07.3.2)
        2. Menghapus/memperbarui semua files
        3. Testing: membuat user baru
        4. Hasil: 
           - user baru berhasil sebagai user biasa 
           - user baru belum bisa membedakan as vendor atau as user biasa

        NEXT: Create Vendor


#### 14.7 Kombiansi data form vendor dan customer - create vendor

        modified:   README.md
        modified:   app/accounts/views.py
        ...
        new file:   media/vendor/license/cat-3.png

        Aktivitas:

        1. Mengupdate views
        2. Testing: register vendor
        3. Hasil: Kadang berhasil, kadang tidak berhasil

        NOTE:

        1. Display vendor pada admin panel hanya memperlihatkan alamat email.
        2. Perlu konfigurasi vendor pada admin

        NEXT: Konfigur admin panel untuk vendor


#### 14.8 Register Vendor model to admin and configure list_display


#### 14.9 Changed the database, run and apply migrations and created admin, customer, and vendor


        modified:   app/accounts/migrations/0001_initial.py
        modified:   app/vendor/migrations/0001_initial.py
        new file:   media/vendor/license/cat-1_KCkmQQY.png


#### 14.10 Modified readme file

        modified:   README.md


#### 14.11 Login - urls, views, templates

        modified:   README.md
        modified:   app/accounts/urls.py
        modified:   app/accounts/views.py
        new file:   templates/app/accounts/login.html


#### 14.12 Login - Adding template to login page

        modified:   README.md
        modified:   templates/app/accounts/login.html 


#### 14.13 Login - Adding logic to login view and redirect logged in user to home

        modified:   README.md
        modified:   app/accounts/views.py

        NOTE: logged in user successfully redirected to home page


#### 14.14 Logout - urls, views, templates

        modified:   README.md
        modified:   app/accounts/urls.py (create path)
        modified:   app/accounts/views.py (added logic)
        new file:   templates/app/accounts/logout.html
        modified:   templates/partials/header.html (added links)


#### 14.15 Creating Dashboard page

        modified:   README.md
        modified:   app/accounts/urls.py
        modified:   app/accounts/views.py
        new file:   templates/app/accounts/dashboard.html

        NOTE: 

        Logged in with correct credentials, but the message
        said, invalid credentials


#### 14.16 Adding conditionals to navbar 

        modified:   README.md
        modified:   app/accounts/views.py
        modified:   templates/partials/header.html


#### 14.17 Restrict Loggedin Users From Accessing Loginpage And Register Page - Restricting logged in user

        modified:   README.md
        modified:   app/accounts/views.py

        We will try to restrict this signing page and restaurant page for the logged in users.
        That means if the user is already logged in, then he should not be able to see this
        or to log in again and to try to register as user again.


        STEPS:

        1. We will handle the logged in user not to login again. 
        We will give the logged in user a warning if he try to log in again. 

        So in the login view, we first need to check if the user is already logged in or not.

        if request.user.is_authenticated:
                messages.warning(request, 'You are already logged in!')
                return redirect('accounts:dashboard')

        - modified:   README.md
        - modified:   app/accounts/views.py
        - Testing: berhasil
        - Git commit

        NOTE: 
        1. You must activate users in admin panel. 
        2. Otherwise you will not be able to log in and you will
           get the alert message 'invalid credentials ..' 


#### 14.18 Restricting logged in user to access register-user page

        modified:   README.md
        modified:   app/accounts/views.py

        Situation:

        Logged in user still showing the registration page, so that should not happen.

        STEPS:

        1. We will handle the logged in user not to login again. DONE ABOVE.
        2. Restric the logged in user from registeruser page. If the logged in
        user try to do this, we will give him a warning.

        We will do this:

        if request.user.is_authenticated:
                messages.warning(request, 'You are already logged in!')
                return redirect('accounts:dashboard')

        - modified:   README.md
        - modified:   app/accounts/views.py
        - Testing: berhasil, namun logged in user masih bisa akses laman registervendor


#### 14.19 Restricting logged in user to access register-vendor page

        modified:   README.md
        modified:   app/accounts/views.py

        Situation:

        Logged in user still showing the registervendor page, so that should not happen.

        STEPS:

        1. We will handle the logged in user not to login again. DONE ABOVE.
        2. Restrict the logged in user from registeruser page. If the logged in
        user try to do this, we will give him a warning.  DONE ABOVE.
        2. Restricting logged in user to access registervendor page.

        We will do this:

        if request.user.is_authenticated:
                messages.warning(request, 'You are already logged in!')
                return redirect('accounts:dashboard')

        - modified:   README.md
        - modified:   app/accounts/views.py
        - Testing: berhasil, namun masih ada restriksi lain yg harus dilakukan.
        Kita akan handel masalah ini satu per satu.
        - Git commit


#### 14.20 Detect User And Redirect Him To Respective Dashboard - Showing logge in as customer or vendor

        modified:   README.md
        modified:   app/accounts/models.py
        modified:   templates/app/accounts/dashboard.html

        Situation:

        1. Logged in customer, can access dashboard page. 
        2. Logged in vendor, also can access dashboard page.
        3. Ideally, each of them should go to their respective dashboard page.

        To see the above situation, open browser incognito you will see it.

        We need to actually send the logged in vendor to the vendor dashboard.
        And to do the same to logged in customer: to send logged in customer
        to customer dashboard.

        In this case, who is going to decide whether the user is a customer or a vendor?
        For that, we need a separate function.
        That function will actually take care of redirecting the user to his dashboard.
        We will call that function as my account.

        We also will make a custom function to get the role.
        We will make customize function in the app/accounts/models.py page.

        The next step is to decide whether the logged in user is a vendor or a customer.
        This is what we will do now.


        We have created this get_role function.
        This get_role function is under the class CustomeUser.
        This get_role function can be accessed as a field name.
        So this is actually not a field name.
        It is a function under the class CustomeUser.
        But still you can you can actually access this as its field.
        So that's why I'm accessing like user.get_role (user dot get_role).
        So this will work and I will refresh.

            def get_role(self):
                if self.role == 1:
                    user_role = 'Vendor'
                elif self.role == 2:
                    user_role = 'Customer'
                return user_role

        - modified:   README.md
        - modified:   app/accounts/models.p.
        - modified:   templates/app/accounts/dashboard.html
        - Testing: berhasil membedakan logged in user sebagai customer dan vendor,
        - Git commit


#### 14.21 Creating utilities to redirect user based on its own role

        # app/accounts/utils.py

        def detect_user(user):

            if user.role == 1:
                redirectUrl = 'vendor_dashboard'
                # redirectUrl = 'vendor_dashboard' # this did not work because of i used: app/accounts
                redirectUrl = '../vendor_dashboard' # this works
                return redirectUrl

            elif user.role == 2:
                redirectUrl = 'custumer_dashboard'
                # redirectUrl = 'custDashboard'   # this did not work because of i used: app/accounts
                redirectUrl = '../custumer_dashboard'  # this works
                return redirectUrl

            elif user.role == None and user.is_superadmin:
                redirectUrl = '/admin'

        modified:   README.md
        new file:   app/accounts/utils.py
        modified:   templates/partials/header.html


#### 14.22 Defining Customer Dashboard

        modified:   README.md
        1. modified:   app/accounts/urls.py (setup customer path)

                path('myaccount/', views.my_account, name='my_account'),
                path('customer-dashboard/', views.customer_dashboard, name='customer_dashboard'),

        2. modified:   app/accounts/utils.py (correcting typos)

                # app/accounts/utils.py

                def detect_user(user):

                    if user.role == 1:
                        redirectUrl = 'vendor-dashboard'
                        # redirectUrl = 'vendor-dashboard' # this did not work because of i used: app/accounts
                        redirectUrl = '../vendor-dashboard' # this works
                        return redirectUrl

                    elif user.role == 2:
                        redirectUrl = 'customer-dashboard'
                        # redirectUrl = 'customer-dashboard'   # this did not work because of i used: app/accounts
                        redirectUrl = '../customer-dashboard'  # this works
                        return redirectUrl

                    elif user.role == None and user.is_superadmin:
                        redirectUrl = '/admin'

        3. modified:   app/accounts/views.py 

                def my_account(request):
                    user = request.user
                    redirectUrl = detect_user(user)
                    return redirect(redirectUrl)


                def customer_dashboard(request):
                    return render(request, 'app/accounts/customer-dashboard.html')

        4. new file:   templates/app/accounts/customer-dashboard.html

                <!-- templates/app/accounts/customer-dashboard.html -->
                {% extends 'base.html' %}
                {% block content %}

                <h4>Welcome to CUSTOMER DASHBORD <span style="color:red;">{{user.username}}</span></h4>
                <p>Your role or logged in is as: <span style="color:red;">{{user.get_role}}</span></p>

                {% include 'partials/alerts.html' %}

                {% endblock content %}

        NOTE:

        1. I tried to login as customer
        2. It redirected me to customer dashboard

        DONE :) 


#### 14.23 Defining Vendor Dashboard

        modified:   README.md
        modified:   app/accounts/urls.py (defined path)
        modified:   app/accounts/views.py (defined: vendor_dashboard)
        new file:   templates/app/accounts/vendor-dashboard.html (defined: vendor dashboard page)

        NOTE:

        1. I tried to login as vendor
        2. It redirected me to vendor dashboard

        DONE :) 

        IMPORTANT!!!!

        1. Any not logged in user can access customer and vendor dashboar.
        2. In real world, only logged in user, either as customer or vendor
           can accesses its own dashboard.


#### 14.24 Protecting my-account, vendor-dashboard, and customer-dashboard from un-logged in user 

        modified:   README.md
        modified:   app/accounts/views.py

        from django.contrib.auth.decorators import login_required

        ...

        @login_required(login_url='accounts:login')
        def customer_dashboard(request):
            return render(request, 'app/accounts/customer-dashboard.html')


        @login_required(login_url='accounts:login')
        def vendor_dashboard(request):
            return render(request, 'app/accounts/vendor-dashboard.html')


        NOTE: 

        Un-logged in user CAN NOT access customer and vendor dashboard

        DONE :)

        IMPORTANT!!!!

        1. Logged in vendor can access customer dashboard.
        2. Logged in customer can access vendor dashboard.

        Either customer or vendor MUST ONLY can access its own dashboard.


#### 14.25 Protecting customer from accessing vendor dashboard or vice versa

        modified:   README.md
        modified:   app/accounts/views.py

        ...
        from django.contrib.auth.decorators import login_required, user_passes_test
        from django.core.exceptions import PermissionDenied

        ...

        # Restrict the vendor from accessing the customer page
        def check_role_vendor(user):
            if user.role == 1:
                return True
            else:
                raise PermissionDenied


        # Restrict the customer from accessing the vendor page
        def check_role_customer(user):
            if user.role == 2:
                return True
            else:
                raise PermissionDenied


        NOTE:

        1. Now logged in customer can not access vendor dasboard and vice versa.
        2. But it does not show error if made mistakes ....


#### 14.26 Adding user_passes_test to customer_dashboard and vendor_dashboar views

        1. modified:   README.md
        2. modified:   app/accounts/views.py

        @login_required(login_url='accounts:login')
        @user_passes_test(check_role_customer)
        def customer_dashboard(request):
            return render(request, 'app/accounts/customer-dashboard.html')

        @login_required(login_url='accounts:login')
        @user_passes_test(check_role_vendor)
        def vendor_dashboard(request):
            return render(request, 'app/accounts/vendor-dashboard.html')

        3. new file:   templates/403.html (Create template)
        
        4. modified:   templates/partials/header.html

                href="{% url 'accounts:my_account' %}">My Account</a>

        NOTE:

        1. When logged in as admin from login page, it created error.
        2. The error is like this:

        TypeError at /accounts/myaccount/
        argument of type 'NoneType' is not iterable


#### 14.27 FIXING ISSUE in 14.26: Adding user_passes_test to customer_dashboard and vendor_dashboar views

        
        NOTE:

        Sebenarnanya tidak ditemui issue setelah:
        
        1. Ganti db (karena db mengalami error).
        2. Jalankan migrasi.
        3. Membuat superuser
        4. Membuat user sebagai vendor dari admin dashboard:
           - dengan role vendor,
           - is_admin (check),
           - is_staff (check),
           _ is_active (check).
        5. Membuat user sebagai customer dari admin dashboard:
           - dengan role customer,
           _ is_active (check).

        LOGIN:

        1. vendor login dari laman depan dan admin dashboard: sukses
        2. customer login dari laman depan sukses.
           TETAPI tdk bisa login dari admin dashboard krn:
           - is_admin (tidak check),
           - is_staff (tidak check),

        Overall: :) 

        modified:   README.md
        renamed:    app/vendor/migrations/0001_initial.py -> app/vendor/migrations/0001_initial_ori.py
        modified:   config/settings.py


#### HOUSE KEEPING PART 1 - Adding link to Github repo

        modified:   README.md


#### 14.28 FIXING ISSUE - vendor_register dan user_register view
        
        NOTE:

        Pada 14.27, terjadi:

        1. User sebagai customer bisa register.
        2. Tapi Register a vendor tidak bisa.

        Setelah fixing vendor_register view, user sdh bisa 
        register sebagai vendor (register restauran)

        modified:   README.md
        modified:   app/accounts/views.py
        new file:   media/vendor/license/darling.PNG
        new file:   media/vendor/license/denah_jalan_ke_lokasi.PNG
        new file:   media/vendor/license/denah_jalan_ke_lokasi_1ZvhdEp.PNG


#### 14.29 FIXING ISSUE - showing alert message
        
        NOTE ISSUE:

        1. Alert login dan log out menumpuk krn
           pada login page tidak bersisi / di-include-kan alertnya.

        Fixing issue:

        1. Add this to login page
        <!-- Load message from templates/includes/alert.html -->
        {% include '../../partials/alerts.html' %}

        modified:   app/accounts/views.py
        modified:   templates/app/accounts/login.html