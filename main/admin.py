from django.contrib import admin
from .models import Category, Tag, Recipe, Review


admin.site.register(Category)
admin.site.register(Tag)
class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine]
    list_display = (
        "title",
        "category",
        "calories",
        "is_healthy",
        "is_easy",
    )

    list_filter = (
        "category",
        "is_healthy",
        "is_easy",
        "is_low_calorie",
    )

    search_fields = (
        "title",
        "description",
        "ingredient",
    )
admin.site.register(Review)