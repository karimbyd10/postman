from django.shortcuts import render, get_object_or_404, redirect
from .models import Food, Category, Order, OrderItem


def home(request):
    foods = Food.objects.all()[:6]
    return render(request,"home.html",{"foods":foods})


def menu(request):
    foods = Food.objects.all()
    categories = Category.objects.all()

    category_id = request.GET.get("category")
    search = request.GET.get("search")

    if category_id:
        foods = foods.filter(category_id=category_id)

    if search:
        foods = foods.filter(name__icontains=search)

    return render(request,"menu.html",{
        "foods":foods,
        "categories":categories
    })


def food_detail(request,id):
    food = get_object_or_404(Food,id=id)
    return render(request,"food_detail.html",{"food":food})


def add_to_cart(request,id):

    cart = request.session.get('cart',{})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart

    return redirect("cart")


def cart(request):

    cart = request.session.get('cart',{})
    foods = []
    total = 0

    for id,qty in cart.items():
        food = Food.objects.get(id=id)
        food.qty = qty
        food.total = food.price * qty
        total += food.total
        foods.append(food)

    return render(request,"cart.html",{
        "foods":foods,
        "total":total
    })


def remove_from_cart(request,id):

    cart = request.session.get('cart',{})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart

    return redirect("cart")


def checkout(request):

    cart = request.session.get('cart',{})

    if request.method == "POST":

        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]

        order = Order.objects.create(
            customer_name=name,
            phone=phone,
            address=address
        )

        for id,qty in cart.items():
            food = Food.objects.get(id=id)

            OrderItem.objects.create(
                order=order,
                food=food,
                quantity=qty
            )

        request.session['cart'] = {}

        return render(request,"success.html")

    return render(request,"checkout.html")