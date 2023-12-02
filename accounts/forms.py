from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password',
    }))
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']
    
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder']='Enter your First Name'
        self.fields['last_name'].widget.attrs['placeholder']='Enter your Last Name'
        self.fields['email'].widget.attrs['placeholder']='Enter your Email ID'
        self.fields['phone_number'].widget.attrs['placeholder']='Enter your Mobile Number'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'   #insted of writing class everytime we use a for loop for class
    
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise forms.ValidationError(
                "Password Does not Match !!!"
            )