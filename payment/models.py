from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.db.models.signals import post_save
from cart import cart

class ShippingAddress(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	shipping_full_name = models.CharField(max_length=255)
	shipping_email = models.CharField(max_length=255)
	shipping_address1 = models.CharField(max_length=255)
	shipping_address2 = models.CharField(max_length=255, null=True, blank=True)
	shipping_city = models.CharField(max_length=255)
	shipping_state = models.CharField(max_length=255, null=True, blank=True)
	shipping_pincode = models.CharField(max_length=255, null=True, blank=True)
	shipping_country = models.CharField(max_length=255)

	# Don't pluralize address
	class Meta:
		verbose_name_plural = "Shipping Address"

	def __str__(self):
		return f'Shipping Address - {str(self.id)}'

# Create a user Shipping Address by default when user signs up
def create_shipping(sender, instance, created, **kwargs):
	if created:
		user_shipping = ShippingAddress(user=instance)
		user_shipping.save()

# Automate the profile thing
post_save.connect(create_shipping, sender=User)



# Create Order Model
class Order(models.Model):
	# Foreign Key
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	full_name = models.CharField(max_length=250)
	email = models.EmailField(max_length=250)
	shipping_address = models.TextField(max_length=15000)
	amount_paid = models.DecimalField(max_digits=7, decimal_places=2)
	date_ordered = models.DateTimeField(auto_now_add=True)
	shipped = models.BooleanField(default=False)	

	def __str__(self):
		return f'Order - {str(self.id)}'

# Create Order Items Model
class OrderItem(models.Model):
	# Foreign Keys
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	date_ordered = models.DateField(auto_now_add=True) 
	quantity = models.PositiveBigIntegerField(default=1)
	price = models.DecimalField(max_digits=7, decimal_places=2)
	amount_paid = models.DecimalField(max_digits=7, decimal_places=2, default=0)
	shipped = models.BooleanField(default=False)


	def __str__(self):
		return f'Order Item - {str(self.id)}'
	
class PaymentForm(models.Model):
	card_name = models.CharField(max_length=255)
	card_number  = models.CharField(max_length=255)
	card_exp_date = models.CharField(max_length=255)
	card_cvv_number = models.CharField(max_length=255, null=True, blank=True)
	card_address1 = models.CharField(max_length=255)
	card_address2 = models.CharField(max_length=255, null=True, blank=True)
	card_city= models.CharField(max_length=255, null=True, blank=True)
	card_state = models.CharField(max_length=255)
	card_pincode = models.CharField(max_length=255)
	card_country = models.CharField(max_length=255)


	def __str__(self):
		return self.card_name