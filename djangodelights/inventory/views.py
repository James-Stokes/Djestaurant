from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, RecipeRequirements, Purchase
from .forms import IngredientCreateForm, MenuItemCreateForm, RecipeRequirementsCreateForm, PurchaseCreateForm, UpdateIngredientForm


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    fields = '__all__'


class IngredientDetailView(LoginRequiredMixin, DetailView):
    model = Ingredient
    template_name = 'inventory/ingredient_detail.html'
    fields = '__all__'


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    fields = '__all__'
    form_class = IngredientCreateForm


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_form.html'
    fields = '__all__'
    form_class = UpdateIngredientForm


class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'
    fields = '__all__'


class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    fields = '__all__'


class ProfitAndRevenueView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = 'inventory/profit_and_revenue.html'
    fields = '__all__'
    context_object_name = 'purchase_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profit'] = 0
        context['revenue'] = 0
        for purchase in context['purchase_list']:
            context['profit'] += purchase.menu_item.price - purchase.menu_item.recipe_requirements_set.first().ingredient.price_per_unit * purchase.menu_item.recipe_requirements_set.first().quantity
            context['revenue'] += purchase.menu_item.price
        return context