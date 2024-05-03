"""
URL configuration for themagicmop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('UserApp.userurls')),
    path('', include('ManagerApp.managerurls'))
    # path('about/', views.about, name='about'),
    #
    # path('profile/', views.profile, name='profile'),
    # path('mybookings/', views.mybookings, name='mybookings'),
    # path('login', views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    #
    # path('profile/update/<int:user_id>/', views.update, name='update'),
    # path('profile/delete/<int:user_id>/', views.delete, name='delete'),
    #
    #
    #
    # path('viewdetails/<int:package_id>/', views.viewdetails, name='viewdetails'),
    # path('reviews/<int:package_id>', views.addreview, name='addreview'),
    # path('viewdetails/booknow/<int:package_id>/', views.booknow),
    # path('booking/confirm', views.confirm, name='confirm'),
    # path('add_review/', views.addreview, name='add_review'),
    #
    #
    #
    #
    #
    #
    #
    # path('enquiries', views.enquiries, name='enquiries'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
