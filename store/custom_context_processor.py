from store.models import Category


def store_website_navbar2(request):
    categories = Category.objects.order_by('order')
    return {
        'categories': categories,
    }