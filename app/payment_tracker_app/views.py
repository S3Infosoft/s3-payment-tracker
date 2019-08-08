from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Reservations
import uuid
from django.contrib import messages


def redirect_to_index(request):

	return redirect("/reservations/")

def redirect_to_admin(request):

  return redirect("/admin/")

class ReservationsListView(LoginRequiredMixin,ListView):

    
    model = Reservations
    template_name = 'sync.html'  

    context_object_name = 'reservations'
    

    def get_queryset(self):
      r_objs=Reservations.objects.filter(sync=False)#.order_by('-date')
      if len(r_objs)!=0:
        return r_objs[::-1]
      else:
        return [0]
      


class AlreadySyncedListView(LoginRequiredMixin,ListView):


    model = Reservations
    template_name = 'synced.html'  

    context_object_name = 'reservations'
    

    def get_queryset(self):
      r_objs=Reservations.objects.filter(sync=True)#.order_by('-date')
      if len(r_objs)!=0:
        return r_objs[::-1]
      else:
        return [0]
      

def callapi(request):
  import requests
  import json
  print(request.POST)
  # for docker
  #BASE_URL='http://192.168.99.100:9000/'

  #locally
  BASE_URL='http://127.0.0.1:8000/'
  GUEST_END_POINT='guest/'
  HOTEL_END_POINT='hotel/'
  RESERVATION_END_POINT='reservation/'

  r_obj=Reservations.objects.get(unique_id=request.POST["reservation_unique_id"])
  

  data={
    'first_name':r_obj.guest.first_name,
    'last_name':r_obj.guest.last_name,
    'name':r_obj.guest.first_name + ' ' + r_obj.guest.last_name,
    'phone':r_obj.guest.phone,
    'email':r_obj.guest.email,
    'address':r_obj.guest.address,
    'unique_id':r_obj.guest.unique_id,
    }
  guest_request=requests.post(BASE_URL + 'api/' + GUEST_END_POINT , data=json.dumps(data) )
  loyalty_guest_unique_id = guest_request.json()['unique_id']
  print(guest_request.status_code)
  print(guest_request.json())

  if guest_request.status_code==404:
    messages.success(request, f'404 response from guest api...can not sync')
    return redirect('index')



  data={
    'name':r_obj.hotel.name,
    'address':r_obj.hotel.address,
    'contact_p_name':r_obj.hotel.contact_p_name,
    'contact_p_email':r_obj.hotel.contact_p_email,
    'contact_p_phone':r_obj.hotel.contact_p_phone,
    'reward_ratio':r_obj.hotel.reward_ratio,
    'unique_id':r_obj.hotel.unique_id,
    }
  hotel_request=requests.post(BASE_URL + 'api/' + HOTEL_END_POINT, data=json.dumps(data) )
  loyalty_hotel_unique_id = hotel_request.json()['unique_id']
  print()
  print(hotel_request.status_code)
  print(hotel_request.json())

  if hotel_request.status_code==404:
    messages.success(request, f'404 response from hotel api...can not sync')
    return redirect('index')
  #while creating reservation in loyalty ,i do not check whether that resrevation is alreday in loyalty app
  #or not by compairing unique_id
  
  data={
  
   'v_t_hotel':r_obj.v_t_hotel,
   'date':r_obj.date,
   'points_obtain':r_obj.points_obtain,
   
   'guest_unique_id':loyalty_guest_unique_id,
   'hotel_unique_id':loyalty_hotel_unique_id,

  }
  reservation_request=requests.post(BASE_URL + 'api/' + RESERVATION_END_POINT, data=json.dumps(data) )
  print()
  print(reservation_request.status_code)
  print(reservation_request.json())

  if reservation_request.status_code==404:
    messages.success(request, f'404 response from reservation api...can not sync')
    return redirect('index')



  if [guest_request.status_code, hotel_request.status_code,reservation_request.status_code ]==[201,201,201]:
    r_obj.sync=True
    r_obj.save()
    messages.success(request,f'{r_obj.guest.first_name} {r_obj.guest.last_name} has been synced')

  return redirect("/reservations/")