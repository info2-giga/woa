from django.contrib import admin
from .models import User, ChatManager, Message, Room

admin.site.register(User)
admin.site.register(ChatManager)
admin.site.register(Message)
admin.site.register(Room)