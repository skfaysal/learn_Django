from django.contrib import admin
from .models import Diseases
from .models import Customer
from .models import Tag
from .models import Product
from .models import Order

admin.site.register(Diseases)
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)