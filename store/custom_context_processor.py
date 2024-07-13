from store.models import Category, Cart, Product


def store_website_navbar2(request):
    cart = Cart.objects.filter(session=request.session.session_key).last()
    cart_total = 0
    cart_product = []
    if cart:
        cart_product = Product.objects.filter(pk__in=cart.item)
        for item in cart_product:
            cart_total += item.price

    categories = Category.objects.order_by('order')
    return {
        'categories': categories,
        'cart_products': cart_product,
        'cart_total': cart_total
    }