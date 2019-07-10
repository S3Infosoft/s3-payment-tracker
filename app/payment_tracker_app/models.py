from django.db import models
import uuid
# Create your models here.

class Guest(models.Model):
  
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	phone= models.CharField(max_length=12,blank=True,null=True)
	email=models.EmailField(max_length=30,blank=True)
	unique_id=models.CharField(max_length=1000, blank=True,null=True)


	def __str__(self):
		return f'{self.email }'

class RoomType(models.Model):

        name=models.CharField(max_length=50)
        description=models.CharField(max_length=300)

        def __str__(self):
                return f'{self.name }'

class Room(models.Model):

	room_name=models.CharField(max_length=50)
	description=models.CharField(max_length=300)
	#room_type=models.CharField(max_length=50)
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

class Reservations(models.Model):

	guest=models.ForeignKey(Guest,on_delete=models.PROTECT)
	check_in=models.DateTimeField()
	check_out=models.DateTimeField()
	room_allocation_data=models.ManyToManyField(RoomAllocation)
	reference_number=models.CharField(max_length=1000, blank=True,unique=True,default=uuid.uuid4)
	booking_source=models.CharField(max_length=50)

	def __str__(self):
		return f'reservation of {self.guest }'

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
	reservation=models.ForeignKey(Reservations,on_delete=models.PROTECT,null=True)
	Amount=models.IntegerField()
	reference_number=models.CharField(max_length=300)
	comment=models.CharField(max_length=300)

	def __str__(self):
		return f'{self.reservation }'	

