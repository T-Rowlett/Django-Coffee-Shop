from django.shortcuts import render, redirect
from app.models import Coffee, Transaction
from datetime import datetime

# Create your views here.


def home(request):
    coffees = Coffee.objects.all()
    return render(request, "app/coffee_list.html", {"coffees": coffees})


def transaction_detail(request, id):
    transaction = Transaction.objects.get(id=id)
    return render(request, "app/transaction_detail.html", {"transaction": transaction})


def buy_coffee(request, id):
    if request.method == "POST":
        coffee = Coffee.objects.get(id=id)
        transaction = coffee.transaction_set.create(
            time=datetime.now(),
            item=coffee,
            pre_tax=coffee.price,
            tax=round(coffee.price * 0.07, 2),
        )
        return redirect("transaction_detail", transaction.id)

