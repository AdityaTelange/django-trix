django-trix
===========

[Trix rich text editor](http://trix-editor.org) widget for Django, using
[Trix 1.2.3](https://github.com/basecamp/trix/releases/tag/1.2.3).

Installation
------------

1. From [PyPI](https://pypi.org/project/django-trix-fork/):

    `pip install django-trix-fork`

2. Install `trix` as app in django Add to *INSTALLED\_APPS*:

    ```
   INSTALLED_APPS = (
        ...
        'trix',
        ...
    )
   ```

3. Add route to *urls.py*:

    ```
    urlpatterns = [
        ...
        url(r'^trix/', include('trix.urls')),
        ...
    ]
   ```

4. Add *django-trix* variables to your `app/settings.py`:
    ```
    ...
    # valid file extentions for attachment 
    TRIX_EXTENSIONS = ['.jpg', '.png'] 

    # folder where attachments will be saved
    TRIX_URI = 'trix' 
    ...
    ```

5. Set-Up trix-django tables:
    ```shell script
    python manage.py makemigrations trix
    python manage.py migrate
   ```
 Done

How to use django-trix
-----------------

django-trix includes a form widget, a model field, and a model admin
mixin that enables the rich text editor. You can use any of these
methods, but you do not need to use all.

### Model

To enable the editor in the Django admin (or any form) via the model
field, use the Trix model field *TrixField* which inherits from
django.db.models.TextField:

    from django.db import models
    from trix.fields import TrixField

    class Post(models.Model):
        content = TrixField('Content')

### Admin

To enable the editor in the Django admin, inherit from TrixAdmin and set
the *trix\_fields* attribute to a list of the fields that use an editor:

    from myawesomeblogapp.models import Post
    from trix.admin import TrixAdmin

    @admin.register(Post)
    class PostAdmin(TrixAdmin, admin.ModelAdmin):
        trix_fields = ('content',)

### Forms and Templates

The editor can be used in forms and templates by adding the *TrixEditor*
widget to a form field:

    from django import forms
    from trix.widgets import TrixEditor

    class EditorForm(forms.Form):
        content = forms.CharField(widget=TrixEditor)

In the template, just use the form as you normally would, but be sure to
include the associated media:

    <!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>Trix Editor Test</title>
            {{ form.media.css }}
        </head>
        <body>
            <form>
                {{ form }}
            </form>
            {{ form.media.js }}
        </body>
    </html>

CSS in head, JS at end of body, because you are a responsible developer.


What Works
------------
Basically Everything :) from Rich Text formatting to Uploading Attachments  !
