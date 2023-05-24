from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price_per_unit = models.IntegerField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class RecipeRequirements(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.menu_item.name + " - " + self.ingredient.name


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.menu_item.name + " - " + str(self.date)