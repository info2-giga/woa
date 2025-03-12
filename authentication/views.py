from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .models import CustomUser
from post.models import Post


# Create your views here.

def landing_page(request):
    posts = Post.objects.all().order_by('-created_at')

    # Kontext mit den Beiträgen
    context = {
        'posts': posts,
    }

    return render(request, 'landing_page.html', context)


# Registrierung
def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Benutzer und Passwort automatisch speichern
            login(request, user)  # Benutzer einloggen
            return redirect("/")  # Nach der Registrierung zur Startseite weiterleiten
    else:
        form = UserRegistrationForm()

    return render(request, "auth/register.html", {"form": form})


# Login
def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = UserLoginForm()

    return render(request, "auth/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("/")


def dashboard_view(request):
    # from ChatGPT
    if request.user.is_authenticated:
        suggested_users = CustomUser.objects.exclude(id=request.user.id).order_by('?')[:8]
    else:
        suggested_users = []
    return render(request, 'assets/base.html', {'suggested_users': suggested_users})


@login_required
def profile_view(req, username):
    user_profile = get_object_or_404(CustomUser, username=username)
    is_following = user_profile.followers.filter(id=req.user.id).exists()
    created_at = user_profile.date_joined
    following_count = user_profile.following.count()
    posts = Post.objects.filter(author=user_profile).order_by('-created_at')

    return render(req, 'auth/profile.html', {
        'user_profile': user_profile,
        'is_following': is_following,
        'created_at': created_at,
        'following_count': following_count,
        'posts': posts,
    })


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Save edited profile")
            return redirect('profile_view', username=request.user.username)
        else:
            print(form.errors)
            messages.error(request, "A error appeared, try again.")
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'auth/edit_profile.html', {'form': form})


@login_required
def follow_user(req, username):
    sigma = get_object_or_404(CustomUser, username=username)
    req.user.following.add(sigma)
    return redirect('profile_view', username=username)


@login_required
def unfollow_user(req, username):
    unsigma = get_object_or_404(CustomUser, username=username)
    req.user.following.remove(unsigma)
    return redirect('profile_view', username=username)
