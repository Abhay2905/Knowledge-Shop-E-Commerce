from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class UserInfoForm(forms.ModelForm):
	phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False)
	address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=False)
	address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
	city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
	state = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}), required=False)
	pincode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'pincode'}), required=False)
	country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)

	class Meta:
		model = Profile
		fields = ('phone', 'address1', 'address2', 'city', 'state', 'pincode', 'country', )



class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'label-input100  input100 wrap-input100 validate-input m-b-23  form-control '
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = 'Password'
		self.fields['new_password1'].help_text = ''

		self.fields['new_password2'].widget.attrs['class'] = 'label-input100  input100 wrap-input100 validate-input m-b-23 form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = 'Confirm Password'
		self.fields['new_password2'].help_text = ''
		

class UpdateUserForm(UserChangeForm):
	# Hide Password stuff
	password = None
	# Get other fields
	email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}), required=False)
	first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}), required=False)
	last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}), required=False)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = 'User Name'
		self.fields['username'].help_text = ''

		
# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(label="Enter Your Email", widget=forms.TextInput(attrs={'class':'label-input100  input100 wrap-input100 validate-input m-b-23  form-control', 'placeholder':'Email Address'}), required=False)
#     firstname  =forms.CharField(label="Enter Your FirstName", max_length=100, widget=forms.TextInput(attrs={'class':'label-input100  input100 wrap-input100 validate-input m-b-23 form-control', 'placeholder':'First Name'}), required=False)
#     lastname = forms.CharField(label="Enter Your LastName", max_length=100, widget=forms.TextInput(attrs={'class':'label-input100  input100 wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Last Name'}), required=False)
	

#     class Meta:
#         model = User
#         fields = ['username', 'email','firstname','lastname', 'password1', 'password2']

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="Enter Your Email", widget=forms.TextInput(attrs={'class':'label-input100  input100 wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Email Address'}))
	firstname = forms.CharField(label="Enter Your FirstName", max_length=100, widget=forms.TextInput(attrs={'class':'label-input100  input100 wrap-input100 validate-input m-b-23 form-control', 'placeholder':'First Name'}))
	lastname = forms.CharField(label="Enter Your LastName", max_length=100, widget=forms.TextInput(attrs={'class':'label-input100  input100 wrap-input100 validate-input m-b-23 form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'email','firstname', 'lastname',  'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'label-input100  input100 wrap-input100 validate-input m-b-23 form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = 'Enter Your Username'
		self.fields['username'].help_text = ''

		self.fields['password1'].widget.attrs['class'] = 'label-input100  input100 wrap-input100 validate-input m-b-23 form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ' Enter Your Password'
		self.fields['password1'].help_text = ''

		self.fields['password2'].widget.attrs['class'] = 'label-input100  input100 wrap-input100 validate-input m-b-23 form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = 'Enter Confirm Password'
		self.fields['password2'].help_text = ''