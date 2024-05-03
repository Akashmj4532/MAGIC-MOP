from django.urls import path,include
from UserApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('profile/', views.profile, name='profile'),
    path('mybookings/', views.mybookings, name='mybookings'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('profile/update/<int:user_id>/', views.update, name='update'),
    path('profile/delete/<int:user_id>/', views.delete, name='delete'),



    path('viewdetails/<int:package_id>/', views.viewdetails, name='viewdetails'),
    path('reviews/<int:package_id>', views.addreview, name='addreview'),
    path('viewdetails/booknow/<int:package_id>/', views.booknow),
    path('booking/confirm', views.confirm, name='confirm'),
    path('add_review/', views.addreview, name='add_review'),







    path('enquiries', views.enquiries, name='enquiries'),




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
