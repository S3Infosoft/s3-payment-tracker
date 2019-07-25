from django.db import models
import uuid
from django.utils import timezone
import datetime

class Guest(models.Model):
  
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	phone= models.CharField(max_length=12,blank=True,null=True)
	email=models.EmailField(max_length=30,blank=True)
	address=models.TextField(blank=True,null=True)
	unique_id=models.CharField(max_length=1000, blank=True,null=True, default=uuid.uuid4)
    #guest unique_id and CutstomUSer unique_id should be same ,in loyalty app and  payment tracker app it should naver cahnge

	def __str__(self):
		return f'{self.email }'

class Hotel(models.Model):

	name=models.CharField(max_length=50)
	image=models.ImageField(default='hotel.png')
	address=models.TextField()
	contact_p_name=models.CharField(max_length=50)
	contact_p_email=models.EmailField(max_length=30,blank=True)
	contact_p_phone=models.CharField(max_length=12)
	reward_ratio=models.FloatField(max_length=30)
	unique_id=models.CharField(max_length=1000, blank=True,null=True, unique=True, default=uuid.uuid4)

	def __str__(self):
		return f'{self.name }'


class RoomType(models.Model):

        name=models.CharField(max_length=50)
        description=models.CharField(max_length=300)

        def __str__(self):
                return f'{self.name }'

class Room(models.Model):

	room_name=models.CharField(max_length=50)
	description=models.CharField(max_length=300)
	room_type = models.ForeignKey(RoomType,on_delete=models.PROTECT,null=True)
	def __str__(self):
		return f'{self.room_name }'	

class MealPlan(models.Model):

	meal_name=models.CharField(max_length=50)
	description=models.CharField(max_length=300)

	def __str__(self):
		return f'{self.meal_name }'	

class RoomAllocation(models.Model):

	guest=models.ForeignKey(Guest,on_delete=models.PROTECT,null=True)
	meal_plan=models.ForeignKey(MealPlan,on_delete=models.PROTECT,null=True)
	room_allocated=models.ForeignKey(Room,on_delete=models.PROTECT,null=True)
	kids=models.IntegerField()
	adults=models.IntegerField()
	extra_beds=models.IntegerField()

	def __str__(self):
		return f'{self.guest }'	

class PaymentMode(models.Model):

	mode_name=models.CharField(max_length=50)
	description=models.CharField(max_length=300)

	def __str__(self):
		return f'{self.mode_name }'	


class PaymentType(models.Model):

	type_name=models.CharField(max_length=50)
	description=models.CharField(max_length=300)

	def __str__(self):
		return f'{self.type_name }'	

class Payment(models.Model):

	payment_mode=models.ForeignKey(PaymentMode,on_delete=models.PROTECT,null=True)
	payment_type=models.ForeignKey(PaymentType,on_delete=models.PROTECT,null=True)
	Amount=models.IntegerField()
	reference_number=models.CharField(max_length=300)
	comment=models.CharField(max_length=300)

	def __str__(self):
		return f'{self.payment_mode }'	



#every model can be accessible by this 1 Reservation models only
#Reservations.objects.all()[2].room_allocation_data.all().first().room_allocated.room_type.description
class Reservations(models.Model):

	guest=models.ForeignKey(Guest,on_delete=models.PROTECT)
	hotel=models.ForeignKey(Hotel,on_delete=models.PROTECT,null=True)
	payment=models.ForeignKey(Payment,on_delete=models.PROTECT)
	points_obtain=models.IntegerField()
	check_in=models.DateTimeField()
	check_out=models.DateTimeField()
	#many to many fields means it can contain many objects of RoomAllocation
	#Reservations.objects.all()[2].room_allocation_data.all()
	room_allocation_data=models.ManyToManyField(RoomAllocation)
	reference_number=models.CharField(max_length=1000, blank=True,unique=True,default=uuid.uuid4)
	#import uuid
	#print(str(uuid.uuid4())[:8]) while creating use this
	v_t_hotel=models.FloatField(max_length=30)#(by this reservation only)

	date=models.CharField(max_length=50,default=timezone.now)
	sync=models.BooleanField(default=False)
	unique_id=models.CharField(max_length=1000, blank=True,null=True, unique=True, default=uuid.uuid4)
	



	def __str__(self):
		return f'reservation of {self.guest }'

