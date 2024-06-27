## Settings:

   - Setup for Template and static files for project base integration without app in settings.py

   - **Templates:**

   ```python
   TEMPLATES = [
      {
         "BACKEND": "django.template.backends.django.DjangoTemplates",
         "DIRS": ["templates"],
         "APP_DIRS": True,
         "OPTIONS": {
               "context_processors": [
                  "django.template.context_processors.debug",
                  "django.template.context_processors.request",
                  "django.contrib.auth.context_processors.auth",
                  "django.contrib.messages.context_processors.messages",
               ],
         },
      },
   ]
   ```

   - **Static and Media:**

   ```python
   STATIC_URL = "static/"
   MEDIA_URL = "media/"

   STATIC_ROOT = BASE_DIR / "assets"
   MEDIA_ROOT = BASE_DIR / "media"

   STATICFILES_DIRS = [BASE_DIR / "static"]STATICFILES_DIRS = [
         os.path.join(BASE_DIR,'static')
      ]
   ```

## Urls:

   - **Static and Media:**

   ```python
   from django.urls import re_path
   from django.views.static import serve

   urlpatterns = [
      re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
      re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
   ]
   ```