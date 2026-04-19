import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gyan_uday.settings')
django.setup()

try:
    from accounts import urls
    print("Importing accounts.urls: SUCCESS")
except Exception as e:
    print(f"Importing accounts.urls: FAILED")
    import traceback
    traceback.print_exc()
