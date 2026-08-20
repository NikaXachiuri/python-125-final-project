from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Category, Recipe, Review
from .forms import ReviewForm

def home(request):
    categorys = Category.objects.all()
    return render(
        request,
        "main/home.html",
        {
            "categorys": categorys
        }
 )

def category(request, id):
    category = get_object_or_404(Category, id=id)
    recipes = Recipe.objects.filter(category=category)

    return render(
        request,
        "main/category.html",
        {
            "category": category,
            "recipes": recipes
        }
    )

def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    return render(
        request,
        "main/recipe.html",
        {
            "recipe": recipe
        }
    )

def review(request, id):
    recipe = get_object_or_404(Review, id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.recipe = recipe
            new_review.save()

            return redirect("reviews")

    else:
        form = ReviewForm()

    return render(
        request,
        "main/review.html",
        {
            "recipe": recipe,
            "form": form
        }
    )

def reviews(request):
    reviews = Review.objects.all()
    return render(
        request,
        "main/reviews.html",
        {
            "reviews": reviews
        }
    )

def dele(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    
    return redirect("reviews")

def edit(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("reviews")
        
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "main/review.html",
        {
            "form": form,
            "recipe": review.recipe
        }
    )