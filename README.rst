=========
Inventory
=========

Simple web app to view personal inventory that could be used for personal
property insurance records. As of now there is no front end. Everything is
done using django admin page.

Developed using python 3.7 and django 2.1

Quick start
-----------

1. Add "inventory" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'inventory',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('inventory/', include('inventory.urls')),

3. Run `python manage.py migrate` to create the inventory models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create and manage inventory (you'll need the Admin app enabled).