from django.shortcuts import render,redirect
from .models import Kategori 


def home(request):
    context={
        'nama': 'index',
    }
    return render (request,'home.html',context)

def kategori(request):
    lst_kategori = Kategori.objects.all()
    context = {'lst_kategori': lst_kategori}
    return render(request, 'kategori.html', context)
def del_kategori(request,k_id):
    Kategori.objects.get(id = k_id ).delete()
    return redirect('kategori')
def add_kategori(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        data = Kategori(nama_kategori = nama)
        data.save()
        return redirect('kategori')
    return render(request ,'form_kategori.html')
def edit_kategori(request,k_id):
    data = Kategori.objects.get(id = k_id)
    if request.method == 'POST':
        data.nama_kategori = request.POST['nama']
        data.save()
        return redirect('kategori')
    context = {'data':data}
    return render(request ,'edit_kategori.html', context)