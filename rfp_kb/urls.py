from django.urls import path
from . import views

urlpatterns = [
    path('rfp_addrecord/', views.rfp_addrecord,name='rfp_addrecord'),
    path('rfp_qa_list/', views.rfp_qa_list, name='rfp_qa_list'),
    path('test/', views.test, name='test'),
    path('rfp_kb/<int:obj_id>', views.rfp_kb, name='rfp_kb'),
]
