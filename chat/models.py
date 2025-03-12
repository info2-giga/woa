# chat/models.py
from django.db import models
from datetime import datetime


class User(models.Model):
    """
    Represents a user in the chat system.

    Attributes:
        userId (str): Unique identifier for the user
    """
    userId = models.CharField(max_length=50)


class ChatManager(models.Model):
    """
    Manages the chat session between users while keeping track of the chat attributes.

    Attributes:
        chatId (str): Unique identifier for the chat session
        sender (ForeignKey): Link to the message sender
        receiver (ForeignKey): Link to the message receiver
        isBlocked (bool): Indicates if the chat is blocked
        createdAt (DateTime): Timestamp when chat was created
    """
    chatId = models.CharField(max_length=50)
    sender = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='chatSender',
    )
    receiver = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='chatReceiver',
    )
    isBlocked = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']

class Room(models.Model):
    name = models.CharField(max_length=1000)
    isBlocked = models.BooleanField(default=False)
class Message(models.Model):
    value = models.CharField(max_length=1000000, default='wazzap')
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000, default='defaultuser')
    room = models.CharField(max_length=1000000, default='roomforall')