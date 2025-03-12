from django import forms
from .models import Post, Media, Comment, Tag

class PostForm(forms.ModelForm):
    """
    A form to create or edit a post, including media upload.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 text-black bg-white border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Enter the title of your post'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 text-black bg-white border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none',
                'placeholder': 'Write something...',
                'rows': 5
            }),
            'tags': forms.SelectMultiple(attrs={
                'class': 'w-full px-4 py-2 text-black bg-white border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none',
            }),
        }

class MediaForm(forms.ModelForm):
    """
    A form to upload media (images or videos).
    """
    class Meta:
        model = Media
        fields = ['image', 'video']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 text-black bg-white border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none',
            }),
            'video': forms.ClearableFileInput(attrs={
                'class': 'w-full px-4 py-2 text-black bg-white border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:outline-none',
            }),
        }

class CommentForm(forms.ModelForm):
    """
    A form to create a comment on a post.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Add a comment...',
                'rows': 3
            }),
        }
