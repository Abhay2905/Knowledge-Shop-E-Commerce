from store.models import Product, Profile, BsProduct, TwoProduct
# from store.models import OneProduct

class Cart():
	def __init__(self, request):
		self.session = request.session
		# Get request
		self.request = request
		# Get the current session key if it exists
		cart = self.session.get('session_key')

		# If the user is new, no session key!  Create one!
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}


		# Make sure cart is available on all pages of site
		self.cart = cart

	def home(self, request):
		self.session = request.session
		# Get request
		self.request = request
		# Get the current session key if it exists
		cart = self.session.get('session_key')

		# If the user is new, no session key!  Create one!
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}


		# Make sure cart is available on all pages of site
		self.cart = cart

	def db_add(self, product, quantity):
		product_id = str(product)
		product_qty = str(quantity)
		# Logic
		if product_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


	def add(self, product, quantity):
		product_id = str(product.id)
		product_qty = str(quantity)
		
		# Logic
		if product_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[product_id] = int(product_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))

	def cart_total(self):
		# Get product IDS
		product_ids = self.cart.keys()
		# lookup those keys in our products database model
		products = Product.objects.filter(id__in=product_ids)
		# Get quantities
		quantities = self.cart
		# Start counting at 0
		total = 0
		
		for key, value in quantities.items():
			# Convert key string into into so we can do math
			key = int(key)
			for product in products:
				if product.id == key:
					if product.is_sale:
						total = total + (product.sale_price * value)
					else:
						total = total + (product.price * value)
		return total


	def __len__(self):
		return len(self.cart)

	def get_prods(self):
		# Get ids from cart
		product_ids = self.cart.keys()
		# Use ids to lookup products in database model
		products = Product.objects.filter(id__in=product_ids)

		# Return those looked up products
		return products

	def get_quants(self):
		quantities = self.cart
		return quantities

	def update(self, product, quantity):
		product_id = str(product)
		product_qty = int(quantity)

		# Get cart
		ourcart = self.cart
		# Update Dictionary/cart
		ourcart[product_id] = product_qty

		self.session.modified = True
	

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


		thing = self.cart
		return thing

	def delete(self, product):
		product_id = str(product)
		# Delete from dictionary/cart
		if product_id in self.cart:
			del self.cart[product_id]

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))



#----------------------------------------------------Best Seller page-----------------------------------------------------------------------


	def db_add(self, bsproduct, quantity):
		bsproduct_id = str(bsproduct)
		bsproduct_qty = str(quantity)
		# Logic
		if bsproduct_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[bsproduct_id] = int(bsproduct_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


	def add_bs(self, bsproduct, quantity):
		bsproduct_id = str(bsproduct.id)
		bsproduct_qty = str(quantity)
		# Logic
		if bsproduct_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[bsproduct_id] = int(bsproduct_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))

	def cart_total_bs(self):
		# Get product IDS
		bsproduct_ids = self.cart.keys()
		# lookup those keys in our products database model
		bsproducts = BsProduct.objects.filter(id__in=bsproduct_ids)
		# Get quantities
		quantities = self.cart
		# Start counting at 0
		total = 0
		
		for key, value in quantities.items():
			# Convert key string into into so we can do math
			key = int(key)
			for bsproduct in bsproducts:
				if bsproduct.id == key:
					if bsproduct.is_sale:
						total = total + (bsproduct.sale_price * value)
					else:
						total = total + (bsproduct.price * value)
		return total
	
	def __len__(self):
		return len(self.cart)


	def get_prods_bs(self):
		# Get ids from cart
		bsproduct_ids = self.cart.keys()
		# Use ids to lookup products in database model
		bsproducts = BsProduct.objects.filter(id__in=bsproduct_ids)

		# Return those looked up products
		return bsproducts
	
	def get_quants_bs(self):
		quantities = self.cart
		return quantities
	
	def update_bs(self, bsproduct, quantity):
		bsproduct_id = str(bsproduct)
		bsproduct_qty = int(quantity)

		# Get cart
		ourcart = self.cart
		# Update Dictionary/cart
		ourcart[bsproduct_id] = bsproduct_qty

		self.session.modified = True
	

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


		thing = self.cart
		return thing	
	
	def delete_bs(self, bsproduct):
		bsproduct_id = str(bsproduct)
		# Delete from dictionary/cart
		if bsproduct_id in self.cart:
			del self.cart[bsproduct_id]

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))	



#--------------------------------------------------------------------------Deal Pages-----------------------------------------------------------------------


	def db_add_two(self, twoproduct, quantity):
		twoproduct_id = str(twoproduct)
		twoproduct_qty = str(quantity)
		# Logic
		if twoproduct_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[twoproduct_id] = int(twoproduct_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


	def add_two(self, twoproduct, quantity):
		twoproduct_id = str(twoproduct.id)
		twoproduct_qty = str(quantity)
		
		# Logic
		if twoproduct_id in self.cart:
			pass
		else:
			#self.cart[product_id] = {'price': str(product.price)}
			self.cart[twoproduct_id] = int(twoproduct_qty)

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))

	def cart_total_two(self):
		# Get product IDS
		twoproduct_ids = self.cart.keys()
		# lookup those keys in our products database model
		twoproducts = TwoProduct.objects.filter(id__in=twoproduct_ids)
		# Get quantities
		quantities = self.cart
		# Start counting at 0
		total = 0
		
		for key, value in quantities.items():
			# Convert key string into into so we can do math
			key = int(key)
			for twoproduct in twoproducts:
				if twoproduct.id == key:
					if twoproduct.is_sale:
						total = total + (twoproduct.sale_price * value)
					else:
						total = total + (twoproduct.price * value)
		return total


	def __len__(self):
		return len(self.cart)

	def get_prods_two(self):
		# Get ids from cart
		twoproduct_ids = self.cart.keys()
		# Use ids to lookup products in database model
		twoproducts = TwoProduct.objects.filter(id__in=twoproduct_ids)

		# Return those looked up products
		return twoproducts

	def get_quants_two(self):
		quantities = self.cart
		return quantities

	def update_two(self, twoproduct, quantity):
		twoproduct_id = str(twoproduct)
		twoproduct_qty = int(quantity)

		# Get cart
		ourcart = self.cart
		# Update Dictionary/cart
		ourcart[twoproduct_id] = twoproduct_qty

		self.session.modified = True
	

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))


		thing = self.cart
		return thing

	def delete_two(self, twoproduct):
		twoproduct_id = str(twoproduct)
		# Delete from dictionary/cart
		if twoproduct_id in self.cart:
			del self.cart[twoproduct_id]

		self.session.modified = True

		# Deal with logged in user
		if self.request.user.is_authenticated:
			# Get the current user profile
			current_user = Profile.objects.filter(user__id=self.request.user.id)
			# Convert {'3':1, '2':4} to {"3":1, "2":4}
			carty = str(self.cart)
			carty = carty.replace("\'", "\"")
			# Save carty to the Profile Model
			current_user.update(old_cart=str(carty))