from django.urls import path,include
from ManagerApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('manager/', views.manager, name='manager'),

    path('viewpackages', views.viewpackages, name='viewpackages'),
    path('addpackage', views.addpackage, name='addpackage'),
    path('update_packages/<int:package_id>', views.update_packages, name='update_packages'),
    path('delete_packages/<int:package_id>', views.delete_packages, name='delete_packages'),

    path('viewbookings', views.viewbookings, name='viewbookings'),

    path('viewusers', views.viewusers, name='viewusers'),
    path('viewusers/update_users/<int:user_id>', views.update_users, name='update_users'),
    path('viewusers/delete_users/<int:user_id>/', views.delete_users, name='delete_users'),








    # path('viewusers/deleteusers/<int:user_id>/', views.deleteusers, name='deleteusers'),
    # path('addpackages/', views.addpackages, name='addpackages'),
    # path('managerprofile/', views.managerprofile, name='managerprofile'),
    #
    # path('bookings/', views.bookings, name='bookings'),
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
