from audioop import reverse
from pydoc import resolve
from django.test import Client, SimpleTestCase,TestCase
from store.views import home, detail, all_categories, orders, add_to_cart, checkout, remove_cart, plus_cart, minus_cart, cart, Orders,
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_case_home_url(self):
        url=reverse('store:home')
        self.assertEquals(resolve(url).func, home)

    def test_case_checkout_url(self):
        url=reverse("store:checkout")
        self.assertEquals(resolve(url).func,checkout)

    def test_case_remove_url(self):
        url=reverse("store:remove-cart", args=[1])
        self.assertEquals(resolve(url).func,remove_cart)
    
    def test_case_plus_url(self):
        url=reverse("store:plus-cart", args=[1])
        self.assertEquals(resolve(url).func,plus_cart)

    def test_case_minus_url(self):
        url=reverse("store:minus-cart", args=[1])
        self.assertEquals(resolve(url).func,minus_cart)

    def test_case_cart_url(self):
        url=reverse("store:cart")
        self.assertEquals(resolve(url).func,cart)

    
    

# Create your tests here.
