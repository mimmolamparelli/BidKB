from django.urls import path
from . import views

urlpatterns = [
    # path('',views.main_view,name='main_view'),
    path('',views.rfp_kb,name="rfp_kb"),
    path('tender/',views.rfp_kb,name="rfp_kb"),
    path("rfp_updaterecord/",views.rfp_updaterecord,name="rfp_updaterecord"),
    path("rfp_deleterecord/",views.rfp_deleterecord,name="rfp_deleterecord"),
    path('main_view/',views.main_view,name="main_view"),
    path('rfp_addrecord/', views.rfp_addrecord,name='rfp_addrecord'),
    path('rfp_qa_list/', views.rfp_qa_list, name='rfp_qa_list'),
    path('test/', views.test, name='test'),
    path('rfp_kb/<int:obj_id>', views.rfp_kb, name='rfp_kb'),
    path('prod_view/<int:obj_id>', views.prod_view, name='prod_view'),
    path('prod_search/',views.prod_search,name='prod_seatch'),
    path('product_add/',views.product_add,name='product_add'),
    path('product_delete/',views.product_delete,name='product_delete'),
    path('product_update/',views.product_update,name='product_update'),

]
