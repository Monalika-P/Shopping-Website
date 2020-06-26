from django.shortcuts import render

# Create your views here.
from main.models import products

def product():

    p1 = products()
    p1.name = 'Crop Top'
    p1.des = 'Blue Lazer Cut'
    p1.price = 785
    p1.img = 'cloth_1.jpg'

    p2 = products()
    p2.name = 'Coarter'
    p2.des = 'Blue casual shoes'
    p2.price = 10000
    p2.img = 'shoe_1.jpg'

    p3 = products()
    p3.name = 'Polo Shirt'
    p3.des = 'Casual Tshirt'
    p3.price = 5598
    p3.img = 'cloth_2.jpg'

    p4 = products()
    p4.name = 'Graphics Shirt'
    p4.des = 'Blue garphics house ware shirt'
    p4.price = 300
    p4.img = 'cloth_3.jpg'

    p5 = products()
    p5.name = 'Graphics Shirt'
    p5.des = 'Blue shirt'
    p5.price = 10000
    p5.img = 'cloth_3.jpg'

    prods = [p1, p2, p3, p4, p5]
    return prods

def Main(request):

    prods = product()
    return render(request, 'index.html', {'prods': prods })

def collection(request):

    prods = product()
    return render(request, 'try.html', {'prods': prods})


def buy(request):
    return render(request, 'description.html')

def sell(request):
    return render(request, 'sell.html')


