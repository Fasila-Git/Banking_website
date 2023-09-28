from django.urls import path
from . import views
app_name='Bank'

urlpatterns=[
    path('',views.home,name='home'),
    path('new/',views.new,name='new'),
    path('form/',views.bank_form,name='bank_form'),
    path('get-branches/', views.get_branches, name='get_branches'),
]