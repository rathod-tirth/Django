## Settings:

   - Setup for Template and static files in settings.py

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
## Email:

   - Setup for email with secure smtp settings in settings.py
   - create `.env` file in the base project dir

   ```text
   DJANGO_SECRET_KEY=your_secret_key
   DJANGO_DEBUG=True
   EMAIL_HOST=smtp.example.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your_email@example.com
   EMAIL_HOST_PASSWORD=your_password
   ```

   ```python
   # settings.py
   import environ

   env = environ.Env(
      # set casting, default value
      DEBUG=(bool, False)
   )

   # reading .env file
   environ.Env.read_env()

   EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
   EMAIL_USE_TLS = True
   EMAIL_HOST = env("EMAIL_HOST")
   EMAIL_PORT = env("EMAIL_PORT")
   EMAIL_HOST_USER = env("EMAIL_HOST_USER")
   EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
   ```

