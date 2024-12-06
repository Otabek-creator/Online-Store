from django import forms
from product.models import Contact, Product


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
    # message = forms.CharField(required=True,
    #                           widget=forms.Textarea())

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'gender', 'message', 'image']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder" : "Ismingizni kiriting..."
                }
            ),
            'email': forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder" : "Emailni kiriting..."
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min" : "998000000000",
                    "max" : "998999999999",
                    "placeholder" : "Telefon raqamingizni kiriting..."
                }
            ),
            'gender': forms.Select(
                attrs={
                    "class": "form-control"
                }
            ),
            'message' : forms.Textarea(
                attrs = {
                    "class" : "form-control"
                }
            )
        }


class CreateProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)

        for visible_field in self.visible_fields():
            if isinstance(visible_field.field, forms.fields.BooleanField):
                visible_field.field.widget.attrs['class'] = 'form-check-input'
            else:
                visible_field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'discount_percent', 'is_active', 'count', 'image', 'category', 'created_by']
        labels = {
            "description" : "Ma'lumot",
            "is_active" : "Holati",
            "count" : "Soni",
            "image" : "Surati",
        }
