from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from wishlist.models import BarangWishList

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishList.objects.all()
    context = {'list_barang': data_barang_wishlist, 'nama': 'Nayyara Airlangga Raharjo'}

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
