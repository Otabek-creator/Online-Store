from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        for visible_field in self.visible_fields():
            if isinstance(visible_field.field, forms.fields.BooleanField):
                visible_field.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible_field.field.widget.attrs['class'] = 'form-control'


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)

        for visible_field in self.visible_fields():
            if isinstance(visible_field.field, forms.fields.BooleanField):
                visible_field.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible_field.field.widget.attrs['class'] = 'form-control'
