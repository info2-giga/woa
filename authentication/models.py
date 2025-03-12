from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    """Custom user model class that supports the forms,
     addtionally we want to extend a profile image
     and if the user is a moderator
    """
    # https://medium.com/@engr.tanveersultan53/abstractuser-vs-abstractbaseuser-in-django-7f231a276988
    profile_image = models.ImageField(
        upload_to="uploads/profiles/", blank=True, null=True,
        default="uploads/profiles/gigachad.jpg"
    )
    is_moderator = models.BooleanField(default=False)

    bio = models.TextField(blank=True, null=True)  # Assume user wants to add a description like in reddit or instagram
    # https://docs.djangoproject.com/en/3.1/ref/models/fields/#django.db.models.ManyToManyField.symmetrical
    followers = models.ManyToManyField('self', related_name='following', symmetrical=False)

    def __str__(self):
        return self.username
