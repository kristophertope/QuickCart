from django.shortcuts import render
from django.http import HttpResponse
from shopping.models import inventory_items

def home(request):
    return render(request, "index.html")

def products(request):
    inventory = list(inventory_items.objects.all().values())
    item_number_list = [i["item_number"] for i in inventory]
    item_name_list = [i["item_name"] for i in inventory]
    item_price_list = [float(i["item_price"]) for i in inventory]
    item_description_list = [i["item_description"] for i in inventory]
    item_image_list = [i["item_image"] for i in inventory]
    
    return render(request, "products.html", locals())

def test():
        print('test complete')

def cart(request):
    inventory = list(inventory_items.objects.all().values())
    item_number_list = [i["item_number"] for i in inventory]
    item_name_list = [i["item_name"] for i in inventory]
    item_price_list = [float(i["item_price"]) for i in inventory]
    item_description_list = [i["item_description"] for i in inventory]
    item_image_list = [i["item_image"] for i in inventory]

    return render(request, "cart.html", locals())
