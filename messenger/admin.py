from django.contrib import admin

# Register your models here.
from messenger.models import Message, Thread

admin.site.register(Message)
admin.site.register(Thread)
