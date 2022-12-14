from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from wishlist.forms import CreateBarangWishlistForm
from wishlist.models import BarangWishList

import datetime
import json

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(
                reverse("wishlist:show_wishlist")
            )  # membuat response
            response.set_cookie(
                'last_login', str(datetime.datetime.now())
            )  # membuat cookie last_login dan menambahkannya ke dalam response

            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('wishlist:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/wishlist/login')
def wishlist_ajax(request):
    form = CreateBarangWishlistForm()

    context = {'form': form}
    return render(request, 'wishlist_ajax.html', context)


@login_required(login_url='/wishlist/login')
def create_wishlist_ajax(request):
    if request.method == "POST":
        data = json.loads(request.body)

        BarangWishList.objects.create(
            nama_barang=data["nama_barang"],
            deskripsi=data["deskripsi"],
            harga_barang=data["harga_barang"],
        )

        return HttpResponse("Item created")

    return HttpResponseNotAllowed('Incorrect method')


@login_required(login_url='/wishlist/login')
def show_wishlist(request):
    data_barang_wishlist = BarangWishList.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Nayyara Airlangga Raharjo',
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, 'wishlist.html', context)


def show_wishlist_xml(request):
    data = BarangWishList.objects.all()

    return HttpResponse(
        serializers.serialize('xml', data), content_type='application/xml'
    )


def show_wishlist_json(request):
    data = BarangWishList.objects.all()

    return HttpResponse(
        serializers.serialize('json', data), content_type='application/json'
    )


def show_wishlist_xml_by_id(request, id):
    data = BarangWishList.objects.filter(pk=id)

    return HttpResponse(
        serializers.serialize('xml', data), content_type='application/xml'
    )


def show_wishlist_json_by_id(request, id):
    data = BarangWishList.objects.filter(pk=id)

    return HttpResponse(
        serializers.serialize('json', data), content_type='application/json'
    )
