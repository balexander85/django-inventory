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

2. Add media_root and media_url to settings.py like this::

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    MEDIA_URL = '/media/'

3. Add following to urls.py::

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
    path('admin/', admin.site.urls),
    ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

4. Run `python manage.py migrate` to create the inventory models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create and manage inventory (you'll need the Admin app enabled).