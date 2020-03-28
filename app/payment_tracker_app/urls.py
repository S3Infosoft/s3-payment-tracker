from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [


    path('myadmin', views.redirect_to_admin, name="myadmin"),
    path("reservations/", views.ReservationsListView.as_view(), name="index"),
    path("already_synced/", views.AlreadySyncedListView.as_view(), name="already_synced"),
    path("", views.redirect_to_index, name="redirect_to_index"),
    path("callapi/",views.callapi,name="callapi"),
    #path('paymentapi/<string: from>/<string: to>',views.PaymentApi,name="paymentapi"),

]
