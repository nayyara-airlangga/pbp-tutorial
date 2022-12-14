from django.urls import path
from wishlist.views import (
    create_wishlist_ajax,
    login_user,
    logout_user,
    register,
    show_wishlist,
    show_wishlist_xml,
    show_wishlist_json,
    show_wishlist_xml_by_id,
    show_wishlist_json_by_id,
    wishlist_ajax,
)

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_wishlist_xml, name='show_wishlist_xml'),
    path('json/', show_wishlist_json, name='show_wishlist_json'),
    path('xml/<int:id>/', show_wishlist_xml_by_id, name='show_wishlist_xml_by_id'),
    path('json/<int:id>/', show_wishlist_json_by_id, name='show_wishlist_json_by_id'),
    path('ajax', wishlist_ajax, name='wishlist_ajax'),
    path('ajax/submit', create_wishlist_ajax, name='create_wishlist_ajax'),
]
