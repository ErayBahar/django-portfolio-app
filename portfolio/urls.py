from django.urls import path

from . import views

urlpatterns = [
    path("",views.portfolio_list, name = "portfolio_list"),
    path("add/",views.add_investment,name= 'add_investment'),
    path('delete/<int:item_id>/',views.delete_investment,name = 'delete_investment'),
]
