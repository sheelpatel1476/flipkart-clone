# Flipkart Clone - Django Project

A minimal e-commerce clone with Mobiles and Fashion categories.

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create superuser:
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Access the site at http://127.0.0.1:8000/
6. Access admin panel at http://127.0.0.1:8000/admin/

## Features

- Home page with category links
- Mobiles section with product listing and detail pages
- Fashion section with product listing and detail pages
- Admin panel to manage products
