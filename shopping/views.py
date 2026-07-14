from django.shortcuts import render, get_object_or_404
from .models import Food, Order


def home(request):
    foods = Food.objects.all()
    return render(request, 'index.html', {'foods': foods})


def signup(request):
    return render(request, 'signUp.html')


def order_now(request, id):
    food = get_object_or_404(Food, id=id)

    if request.method == "POST":
        Order.objects.create(
            food=food,
            quantity=1,
            total_price=food.price
        )

        return render(request, "order.html", {
            "food": food,
            "message": "Order Placed Successfully ✅"
        })

    return render(request, "order.html", {"food": food})


def place_order(request, id):
    food = get_object_or_404(Food, id=id)

    Order.objects.create(
        food=food,
        quantity=1,
        total_price=food.price
    )

    return render(request, 'payment.html', {'food': food})