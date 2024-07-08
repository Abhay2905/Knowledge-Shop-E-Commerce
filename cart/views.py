from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
# from .cart import CartOne
from store.models import Product, BsProduct, TwoProduct
# from store.models import OneProduct
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()
	cart_products_bs = cart.get_prods_bs
	quantities_bs = cart.get_quants_bs
	totals_bs = cart.cart_total_bs()
	# return redirect('bs_cartsummary.html', {"cart_products_bs":cart_products_bs, "quantities_bs":quantities_bs, "totals_bs":totals_bs})
	return render(request, "cart_summary.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals,"cart_products_bs":cart_products_bs, "quantities_bs":quantities_bs, "totals_bs":totals_bs})
 	# return render(request, "bs_cartsummary.html", {"cart_products_bs":cart_products_bs, "quantities_bs":quantities_bs, "totals_bs":totals_bs})
 



def cart_add(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Product Added To Cart..."))
		return response

def cart_delete(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		# Call delete Function in Cart
		cart.delete(product=product_id)

		response = JsonResponse({'product':product_id})
		#return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response


def cart_update(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		cart.update(product=product_id, quantity=product_qty)

		response = JsonResponse({'qty':product_qty})
		#return redirect('cart_summary')
		messages.success(request, ("Your Cart Has Been Updated..."))
		return response
	

# -------------------------------------------------------------------------bestSeller---------------------------------------------------------------------

# def cart_summary_bs(request):
# 	# Get the cart
# 	cart = Cart(request)
# 	cart_products_bs = cart.get_prods_bs
# 	quantities_bs = cart.get_quants_bs
# 	totals_bs = cart.cart_total_bs()
# 	return render(request, "bs_cartsummary.html", {"cart_products_bs":cart_products_bs, "quantities_bs":quantities_bs, "totals_bs":totals_bs})

def cart_add_bs(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		bsproduct_id = int(request.POST.get('bsproduct_id'))
		bsproduct_qty = int(request.POST.get('bsproduct_qty'))

		# lookup product in DB
		bsproduct = get_object_or_404(BsProduct, id=bsproduct_id)
		
		# Save to session
		cart.add_bs(bsproduct=bsproduct, quantity=bsproduct_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Product Added To Cart..."))
		return response

def cart_delete_bs(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		bsproduct_id = int(request.POST.get('bsproduct_id'))
		# Call delete Function in Cart
		cart.delete_bs(bsproduct=bsproduct_id)

		response = JsonResponse({'bsproduct':bsproduct_id})
		#return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response


def cart_update_bs(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		bsproduct_id = int(request.POST.get('bsproduct_id'))
		bsproduct_qty = int(request.POST.get('bsproduct_qty'))

		cart.update_bs(bsproduct=bsproduct_id, quantity=bsproduct_qty)

		response = JsonResponse({'qty':bsproduct_qty})
		#return redirect('cart_summary')
		messages.success(request, ("Your Cart Has Been Updated..."))
		return response


#---------------------------------------------------------------sale product two------------------------------------------------------------------

def cart_summary_two(request):
	# Get the cart
	cart = Cart(request)
	cart_products_two = cart.get_prods_two
	quantities_two = cart.get_quants_two
	totals_two = cart.cart_total_two()
	return render(request, "two_cartsummary.html", {"cart_products_two":cart_products_two, "quantities_two":quantities_two, "totals_two":totals_two})

def cart_add_two(request):
	# Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		twoproduct_id = int(request.POST.get('twoproduct_id'))
		twoproduct_qty = int(request.POST.get('twoproduct_qty'))

		# lookup product in DB
		twoproduct = get_object_or_404(TwoProduct, id=twoproduct_id)
		
		# Save to session
		cart.add_two(twoproduct=twoproduct, quantity=twoproduct_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		# response = JsonResponse({'Product Name: ': product.name})
		response = JsonResponse({'qty': cart_quantity})
		messages.success(request, ("Product Added To Cart..."))
		return response

def cart_delete_two(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		twoproduct_id = int(request.POST.get('twoproduct_id'))
		# Call delete Function in Cart
		cart.delete_two(twoproduct=twoproduct_id)

		response = JsonResponse({'twoproduct':twoproduct_id})
		#return redirect('cart_summary')
		messages.success(request, ("Item Deleted From Shopping Cart..."))
		return response


def cart_update_two(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		# Get stuff
		twoproduct_id = int(request.POST.get('twoproduct_id'))
		twoproduct_qty = int(request.POST.get('twoproduct_qty'))

		cart.update_two(twoproduct=twoproduct_id, quantity=twoproduct_qty)

		response = JsonResponse({'qty':twoproduct_qty})
		#return redirect('cart_summary')
		messages.success(request, ("Your Cart Has Been Updated..."))
		return response