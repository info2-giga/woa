"""
URL configuration for woa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import landing_page, login_user, register_user, logout_user, profile_view, edit_profile, follow_user, unfollow_user
from chat.views import ChatRoom
from trip.views import TripListView
from post.views import create_post, comment_post, like_post, post_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", landing_page, name="landing_page"),
    # User Authentication, GET, EDIT & Follow/Unfollow
    path("login/", login_user, name="login"),
    path("register/", register_user, name="register"),
    path("/", logout_user, name="logout"),
    path('profile/<str:username>', profile_view, name='profile_view'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/follow/<str:username>', follow_user, name='follow_user'),
    path('profile/unfollow/<str:username>', unfollow_user, name='unfollow_user'),
    # Further features
    # TODO: Work on those features
    path("plan-trip", TripListView.as_view(), name="plan_trip"),
    # POSTS ENTRY
    path("post/create/", create_post, name="create_post"),
    path("post/<int:post_id>/comment/", comment_post, name="comment_post"),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('post/<int:pk>/', post_detail, name='post_detail'),  # Detailansicht
    path('', include('chat.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
