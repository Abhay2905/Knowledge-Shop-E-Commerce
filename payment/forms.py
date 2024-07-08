from django import forms
from .models import ShippingAddress, PaymentForm

class ShippingForm(forms.ModelForm):
	shipping_full_name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Full Name'}), required=True)
	shipping_email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Email Address'}), required=True)
	shipping_address1 = forms.CharField(label="First Address", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'First Address'}), required=True)
	shipping_address2 = forms.CharField(label="Second Address", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Second Address'}), required=False)
	shipping_city = forms.CharField(label="City", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'City'}), required=True)
	shipping_state = forms.CharField(label=" State", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'State'}), required=False)
	shipping_pincode = forms.CharField(label="Pincode", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'pincode'}), required=False)
	shipping_country = forms.CharField(label="Country", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Country'}), required=True)

	class Meta:
		model = ShippingAddress
		fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_pincode', 'shipping_country']

		exclude = ['user',]

class PaymentForm(forms.Form):
	card_name =  forms.CharField(label="Name On Card", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Name On Card'}), required=True)
	card_number =  forms.CharField(label="Card Number", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Card Number'}), required=True)
	card_exp_date =  forms.CharField(label="Expiration Date", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Expiration Date'}), required=True)
	card_cvv_number =  forms.CharField(label="CVV Code", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'CVV Code'}), required=True)
	card_address1 =  forms.CharField(label="Billing Address 1", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Billing Address 1'}), required=True)
	card_address2 =  forms.CharField(label="Billing Address 2", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Billing Address 2'}), required=False)
	card_city =  forms.CharField(label="Billing City", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Billing City'}), required=True)
	card_state = forms.CharField(label="Billing State", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Billing State'}), required=True)
	card_pincode =  forms.CharField(label="Billing Pincode", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Billing Pincode'}), required=True)
	card_country =  forms.CharField(label="Billing Country", widget=forms.TextInput(attrs={'class':'input100 label-input100  wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Billing Country'}), required=True)


	class Meta:
		model = PaymentForm
		fields = ['card_name', 'card_number ', 'card_exp_date', 'card_cvv_number', 'card_address1', 'card_address2', 'card_city', 'card_state', 'card_pincode', 'card_country']

		exclude = ['user',]