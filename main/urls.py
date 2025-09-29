from django.urls import path
from main.views import show_main, show_xml, add_product, show_product, show_json, show_xml_by_id, show_json_by_id
from main.views import register

from main.views import login_user
from main.views import logout_user

from main.views import edit_product
from main.views import delete_product
from main.views import about

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product , name='add_product'),
    path('product/<int:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    path('product/<int:id>/edit', edit_product, name='edit_product'),
    path('product/<int:id>/delete', delete_product, name='delete_product'),

    path('about/', about, name='about'),
]