from baskets.models import Basket

def basket(request):
    print('Привет из контекстного процессора')
    basket = []

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    return {
        'basket': basket,
    }