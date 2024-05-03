from django.shortcuts import render, redirect
from UserApp.models import *
from ManagerApp.models import *

def manager(request):
        return render(request,'managerhome.html')



def managerlogin(request):
    if request.method == 'POST':
        managername = request.POST.get('managername')
        password = request.POST.get('password')
        manager_data = Manager.objects.filter(manager_name=managername, password=password).first()

        if manager_data:
            request.session['manager_data'] = manager_data.user_id
            return redirect('manager/')
        else:
            return redirect('/login')
    return render(request, 'managerlogin.html')

#
# def managerlogin(request):
#     return render(request, 'login.html')
#
#
# def manager(request):
#     if 'manager_id' in request.session:
#         manager_id = request.session['manageer_id']
#         manager_data = Manager.objects.filter(manager_id=manager_id)
#         return render(request,'managerhome.html', {'manager_id': manager_data})
#     else:
#         return redirect('managerlogin/')


def addpackage(request):
    if request.method == 'POST':
        package_name = request.POST.get('packagename')
        short_description = request.POST.get('short_description')
        long_description = request.POST.get('long_description')
        area_covers = request.POST.get('area_covers')
        package_image = request.FILES['package_image']

        add_packages = Packages()
        add_packages.package_name = package_name
        add_packages.short_description = short_description
        add_packages.full_description = long_description
        add_packages.area_covers = area_covers
        add_packages.package_image = package_image
        add_packages.save()
        return redirect('viewpackages')

    return render(request,'addpackage.html')
def update_packages(request,package_id):
    package = Packages.objects.filter(package_id=package_id)
    if request.method == 'POST':
        update_package = Packages()
        update_package.package_name = request.POST.get('new_package_name')
        update_package.short_description = request.POST.get('new_short_description')
        update_package.full_description = request.POST.get('new_full_description')
        update_package.area_covers = request.POST.get('new_area_covers')
        update_package.package_image = request.FILES['package_image']
        update_package.save()
        return redirect('viewppackages')

    return render(request, 'updatepackage.html', {'package_data':package})

def delete_packages(request,package_id):
    package = Packages.objects.filter(package_id=package_id)
    package.delete()
    return redirect('viewpackages')
def viewbookings(request):
    bookings = Booking.objects.all()
    return render(request, 'viewbookings.html', {'bookings': bookings})

def viewusers(request):
    users = User.objects.all()
    return render(request, 'viewusers.html', {'users': users})

def update_users(request, user_id):
    users = User.objects.filter(user_id=user_id)
    if request.method == 'POST':
        update_user = User.objects.get(user_id=user_id)
        update_user.user_name = request.POST.get('user_name')
        update_user.age = request.POST.get('age')
        update_user.address = request.POST.get('address')
        update_user.phone = request.POST.get('phone')
        update_user.email = request.POST.get('email')
        update_user.password = request.POST.get('password')
        update_user.save()
        return redirect('viewusers')
    return render(request, 'updateuser.html', {'user_data': users})

def delete_users(request,user_id):
    data = User.objects.filter(user_id=user_id)
    data.delete()
    return redirect('viewusers')

def viewpackages(request):
    packages = Packages.objects.all()
    return render(request, 'managerviewpackages.html', {'packages': packages})


