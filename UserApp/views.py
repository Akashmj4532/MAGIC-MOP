from django.shortcuts import render, HttpResponse, redirect
from .models import *
from ManagerApp.models import *
from django.db.models import Q


def home(request):
    packages = Packages.objects.all()
    searchitem = request.POST.get('searchitem')
    if searchitem:
        packages = packages.filter(Q(package_name__icontains=searchitem))
    return render(request, 'home.html', {'packages': packages, 'searchitem': searchitem})


def about(request):
    return render(request, 'about.html')

def enquiries(request):
    if request.method == 'POST':
        user = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        user_enquire = UserEnquieries()
        user_enquire.name = user
        user_enquire.address = address
        user_enquire.phone_number = phone
        user_enquire.email = email
        user_enquire.save()

        return redirect('about/')
    return render(request, 'enquiries.html')



def viewdetails(request, package_id):
    packages = Packages.objects.filter(package_id=package_id)
    reviews = Review.objects.filter(package_id=package_id)
    return render(request, 'viewdetails.html', {'packages': packages, 'reviews': reviews})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        user = User.objects.filter(user_name=username, password=password).first()

        if user:
            request.session['user_id'] = user.user_id
            return redirect('profile/')
        else:
            return redirect('/login')
    return render(request, 'login.html')


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')


def profile(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_data = User.objects.filter(user_id=user_id)
        booking_data = Booking.objects.filter(user_id=user_id)
        return render(request, 'profile.html', {'userdata': user_data,'booking_data': booking_data})
    else:
        return redirect('/login')


def update(request, user_id):
    data = User.objects.filter(user_id=user_id)
    if request.method == 'POST':
        # print(request.method)

        name = request.POST.get('new_user_name')
        age = request.POST.get('new_age')
        address = request.POST.get('new_address')
        email = request.POST.get('new_email')
        phone = request.POST.get('new_phone')
        password = request.POST.get('password')

        # Retrieve the user object from the database

        # print('user')

        # Update the fields
        user = User.objects.get(user_id=user_id)
        user.user_name = name
        user.address = address
        user.email = email
        user.phone = phone
        user.password = password
        user.age = age
        # Save the updated user object
        user.save()

        return redirect('/profile')

    return render(request, 'update.html', {'user_data': data})


def delete(request, user_id):
    data = User.objects.filter(user_id=user_id)
    data.delete()
    return redirect('/')


def booknow(request, package_id):
    # print('book now called')
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_data = User.objects.filter(user_id=user_id)

        package_data = Packages.objects.filter(package_id=package_id)
        # print(package_data)
        # print(user_id)
        # print(user_data)

        return render(request, 'booking.html', {'package': package_data, 'user': user_data})
    else:
        return redirect('/login')


def confirm(request):
    # print('confirm is called ')
    # print(request.method)
    if request.method == 'POST':
        # print(request.method)
        user_id = User.objects.get(user_id=request.POST.get('user_id'))
        package_id = Packages.objects.get(package_id=request.POST.get('package_id'))
        date = request.POST.get('date')

        user = Booking()
        user.user_id = user_id
        user.package_id = package_id
        user.booking_date = date
        user.save()
        return redirect('/')
    else:
        return HttpResponse('error')

def addreview(request,package_id):
    packages = Packages.objects.filter(package_id=package_id)
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        bookings = Booking.objects.get(user_id=user_id, package_id=package_id)
        if bookings:
            if request.method == 'POST':
                review = request.POST.get('review')
                user_id = bookings.user_id
                package_id = bookings.package_id

                usereview = Review()
                usereview.user_id = user_id
                usereview.package_id = package_id
                usereview.review_description = review
                usereview.save()
                return redirect('/')

            return render(request, 'review.html', {'package': packages})
        else:
            return HttpResponse('error')
    else:
        return redirect('login/')

def mybookings(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        user_data = User.objects.filter(user_id=user_id)
        booking_data = Booking.objects.filter(user_id=user_id)
        if booking_data:
            return render(request, 'mybookings.html', {'mybookings': booking_data, 'user_data': user_data})
        else:
            return HttpResponse('no bookings')










