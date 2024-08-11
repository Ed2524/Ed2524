# from django import forms
# from .models import Product, Category

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = "__all__"
#         labels = {
#             "name": "Name",
#             "image": "Image",
#             "description": "Description",
#             "price": "Price",
#             "category": "Category",
#         }

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields = "__all__"
#         labels = {
#             "name": "Name"
#         }


from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "image"]
        