from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    """ Form that is used for adding customer, product, and status details """
    class Meta:
        model = Order
        fields = ['customer', 'product', 'status']
        # or fields = "__all__"
