from django.contrib import admin

# Register your models here.
from .models import Guest,Hotel,RoomType,Room,MealPlan,RoomAllocation,Reservations,PaymentMode,PaymentType,Payment



admin.site.register(Guest)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(MealPlan)
admin.site.register(RoomAllocation)
admin.site.register(Reservations)
admin.site.register(PaymentMode)
admin.site.register(PaymentType)
admin.site.register(Payment)
admin.site.register(Hotel)
