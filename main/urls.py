from django.urls import path
<<<<<<< HEAD
from main.views import show_main, show_xml, add_product, show_product, show_json, show_xml_by_id, show_json_by_id
=======
from main.views import show_main
>>>>>>> c41c600891abca760eaefccfc3f1c61fbed42336

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
<<<<<<< HEAD
    path('add-product/', add_product , name='add_product'),
    path('product/<int:id>/', show_product, name='show_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
=======
>>>>>>> c41c600891abca760eaefccfc3f1c61fbed42336
]