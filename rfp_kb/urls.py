from django.urls import path
from . import views

urlpatterns = [
    # path('',views.main_view,name='main_view'),
    path('',views.rfp_kb,name="rfp_kb"),
    path("rfp_updaterecord/",views.rfp_updaterecord,name="rfp_updaterecord"),
    path("rfp_deleterecord/",views.rfp_deleterecord,name="rfp_deleterecord"),
    path('main_view/',views.main_view,name="main_view"),
    path('rfp_addrecord/', views.rfp_addrecord,name='rfp_addrecord'),
    path('rfp_qa_list/', views.rfp_qa_list, name='rfp_qa_list'),
    path('test/', views.test, name='test'),
    path('rfp_kb/<int:obj_id>', views.rfp_kb, name='rfp_kb'),
]
