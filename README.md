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

   - **Static:**

   ```python
   import os

   STATICFILES_DIR = [
      os.path.join(BASE_DIR,'static')
   ]
   ```