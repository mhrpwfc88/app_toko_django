from django.shortcuts import render,redirect
<<<<<<< HEAD
from django.contrib.auth import authenticate ,logout as auth_logout,login as auth_login
from django.contrib.auth.decorators import login_required
=======
from django.contrib.auth import authenticate, login
>>>>>>> 7e7f4762ce18c0a4d5404da374cc7483f099ebb3
from django.contrib import messages
from .models import Kategori 


def home(request):
    context={
        'nama': 'index',
    }
    return render (request,'home.html',context)
@login_required
def kategori(request):
    lst_kategori = Kategori.objects.all()
    context = {'lst_kategori': lst_kategori}
    return render(request, 'kategori.html', context)
@login_required
def del_kategori(request,k_id):
    Kategori.objects.get(id = k_id ).delete()
    return redirect('kategori')
@login_required
def add_kategori(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        data = Kategori(nama_kategori = nama)
        data.save()
        return redirect('kategori')
    return render(request ,'form_kategori.html')
@login_required
def edit_kategori(request,k_id):
    data = Kategori.objects.get(id = k_id)
    if request.method == 'POST':
        data.nama_kategori = request.POST['nama']
        data.save()
        return redirect('kategori')
    context = {'data':data}
    return render(request ,'edit_kategori.html', context)
# def login(request):
#     if request.method == 'POST':
#         username = request.get['username']
#         password = request.get['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Username atau Password salah')
#             return redirect('login')
#     return render('request', 'login.html')
<<<<<<< HEAD
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Menggunakan auth_login untuk menghindari konflik nama
=======
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Menggunakan request.POST
        password = request.POST.get('password')  # Menggunakan request.POST
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Menggunakan auth_login untuk menghindari konflik nama
>>>>>>> 7e7f4762ce18c0a4d5404da374cc7483f099ebb3
            return redirect('home')
        else:
            messages.error(request, 'Username atau Password salah')
            return redirect('login')
<<<<<<< HEAD
    return render(request, 'login.html')
def user_logout(request):
    if request.method == 'GET':
        auth_logout(request) 
        messages.success(request, 'Anda telah berhasil logout.')
        return redirect('login') 

=======
    return render(request, 'login.html') 
>>>>>>> 7e7f4762ce18c0a4d5404da374cc7483f099ebb3
    