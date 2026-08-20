from django.db import models
from django.urls import reverse
from .validators import validate_name, validate_comment

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredient = models.TextField()
    image = models.ImageField(upload_to="")
    cookingtime = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField()
    carb = models.PositiveIntegerField()
    fat = models.PositiveIntegerField()
    is_low_calorie = models.BooleanField(default=False)
    is_healthy = models.BooleanField(default=False)
    is_easy = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("recipe", args=[self.id])
    
    def healthy(self):
        return self.is_healthy
    
    def difficulty(self):
        if self.is_easy:
            return "Easy"
        else:
            return "Hard"

class Review(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
    
    name = models.CharField(validators=[validate_name])
    rating = models.PositiveIntegerField(
        choices=[
            (1, "1 STAR"),
            (2, "2 STARS"),
            (3, "3 STARS"),
            (4, "4 STARS"),
            (5, "5 STARS")
        ]
    )
    comment = models.TextField(validators=[validate_comment])
    
    def __str__(self):
        return self.name