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