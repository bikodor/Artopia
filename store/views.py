from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Product, Basket

def check_amount():
    basket = Basket.objects.all()
    amount = 0
    for b in basket:
        amount += b.count
    return amount

class Home(ListView):
    template_name = 'store/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount'] = check_amount()
        return context

class ProductPage(DetailView):
    template_name = 'store/product.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return get_object_or_404(Product.objects.all(), slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['amount'] = check_amount()
        return context

    def post(self, request, *args, **kwargs):
        product_slug = self.kwargs.get('slug')
        product = get_object_or_404(Product, slug=product_slug)
        basket, created = Basket.objects.get_or_create(
            pk=product.pk,
            title=product.title,
            defaults={
                'price': product.price,
                'photo': product.photo,
            }
        )
        if not created:
            basket.count += 1
            basket.save()

        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            return JsonResponse({'count': basket.count})
        else:
            return redirect(reverse('store:product', kwargs={'slug': product_slug}))

class BasketPage(ListView):


    def get(self, request, *args, **kwargs):
        posts = Basket.objects.all()
        return render(request, 'store/basket.html', {'posts': posts, 'amount': check_amount()})

    def post(self, request, *args, **kwargs):
        if 'delete_item' in request.POST:
            item_id = request.POST.get('delete_item')
            item = get_object_or_404(Basket, pk=item_id)
            item.delete()
            return redirect('store:basket')  # Используйте имя URL вашего представления
        elif 'order' in request.POST:
            Basket.objects.all().delete()
            return redirect('store:success_buy')  # Перенаправьте на страницу успеха заказа
        else:
            return HttpResponse("Неверный запрос", status=400)

class SuccessBuy(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'store/success_buy.html')
