from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
# Create your views here.
def main(request):
    return render(request,'main.html')
def register(request):
    if request.method=="POST":
            user=User.objects.filter(username=request.POST['username'])
            if user.exists():
                  messages.info(request,'User already exist')
                  return redirect(reverse('register'))

            form=RegistrationForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect(reverse('loginview'))
    f=RegistrationForm()           
    return render(request,'reg.html',context={'form':f})

def loginview(request):
    if request.method=='POST':
            form=LoginForm(request.POST)
            if form.is_valid():
                user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
                if user:
                      login(request,user)
                      return redirect(reverse('home'))
                else:
                      messages.error(request,'Invalid username or password')
                      return redirect(reverse('loginview'))
    else:
        f=LoginForm()
    return render(request,'signin.html',context={'form':f})

@login_required(login_url='login')
def home(request):
    data=Course.objects.all()
    return render(request,'home.html',{'data': data})

@login_required(login_url='login')
def add_to_cart(request, course_id):
    course = Course.objects.get(id=course_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, course=course)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect(reverse('cart'))

@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_amount = sum(item.course.price * item.quantity for item in cart_items)
    # total_amount = 0
    # for item in cart_items:
    #     total_amount += item.course.price * item.quantity
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})

@login_required(login_url='login')
def remove_from_cart(request, cart_id):
    cart_item = Cart.objects.get(id=cart_id, user=request.user)
    cart_item.delete()
    messages.success(request, 'Course removed from cart successfully.')
    return redirect(reverse('cart'))

@login_required(login_url='login')
def delete_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    if request.method == "POST":
        for item in cart_items:
            item.delete()
        messages.success(request, 'All courses removed from cart.')
        return redirect(reverse('home'))

    return render(request, 'delete.html', {'cart_items': cart_items})
def courses(request):
    data=Course.objects.all()
    return render(request,'courses.html',{'data':data})

@login_required(login_url='login')
def profile(request):
    user=request.user
    return render(request,'profile.html',{'user':user})

@login_required(login_url='login')
def logoutview(request):
    logout(request)
    return redirect('loginview')

@login_required(login_url='login')
def search_item(request):
    data=request.GET['search']
    # if data:
    course=Course.objects.filter(title__icontains=data)
    course=Course.objects.filter(author__icontains=data)

    # else:
        # course=Course.objects.none()
        # print("no such item exists")
        # messages.error(request, 'no such item exists')
    return render(request,'search.html',{'course':course})


