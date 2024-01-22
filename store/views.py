
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# J'importe le model des produits pour la vue.
from store.models import Product, Cart, Order


# Creation des vues.
def index(request):
    products = Product.objects.all()

    return render(request, 'store/index.html', context={"products": products})

# Creation de la fonction de detaille.
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product})

# Creation de la fonction du panier
def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user,
                                                 ordered=False,
                                                 product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)

    return render(request,'store/cart.html', context={"orders": cart.orders.all()})
# vue de suppression
def delete_cart(request):
    if cart := request.user.cart:
        cart.delete()

    return redirect('index')
def about(request):
    return render(request, 'store/about.html')

def about(request):
    return render(request, 'store/contact.html')
