from django.db import models
from authentication.models import CustomUser


# Create your models here.
class Tag(models.Model):
    """
    A Tag class, if the user wants to add more tags,
    it should be unique (not "travel" twice for example) - irene
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name





class Media(models.Model):
    """
    A class to upload videos or images
    """
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='media'
    )
    image = models.ImageField(upload_to='uploads/posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='uploads/posts/videos/', blank=True,
                             null=True)

    def __str__(self):
        return f"Media for post ID {self.post.id}"


class Like(models.Model):
    """
    A Like class, if a user liked a post/entry
    forgot to add it in the class diagram
    """
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='liked'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked this post {self.post.id}"


class Comment(models.Model):
    """
    A comment class, if a user wants to comment on a post,
    forgot to add it in the class diagram
    """
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"


class Post(models.Model):
    """ A Post class to store medias (images or videos), title, content, likeCount and comments
    in the database.
    """
    author = models.ForeignKey(
        CustomUser,  # User
        on_delete=models.CASCADE,  # If user delete post, everything will be deleted from the column
        related_name="posts"
    )
    title = models.CharField(max_length=256)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
