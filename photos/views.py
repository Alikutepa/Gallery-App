from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'main/index.html', context)



def categoryPage(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:20]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'main/category.html', context)

def imageDetailPage(request, slug1, slug2):

    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)

    context = {}
    context['category'] = category
    context['image'] = image

    return render(request, 'main/category.html', context)

def image_location(request, location):
    images = Image.filter_by_location(location)
    print(images)
    return render(request, 'images/location.html', {'location_images': images})    



