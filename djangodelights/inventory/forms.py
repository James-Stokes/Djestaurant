from django import forms
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase


class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "price_per_unit")


class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ("name", "price")


class RecipeRequirementsCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirements
        fields = ("ingredient", "menu_item", "quantity")


class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ("menu_item",)


class UpdateIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ("name", "quantity", "price_per_unit")