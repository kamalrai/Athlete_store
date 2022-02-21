from codecs import register
from django.urls import reverse,resolve
from django.test import SimpleTestCase, TestCase, Client
from .views import *
from django.contrib.auth.models import User


class TestUrls(SimpleTestCase):
    def test_home_url(self):
        url=reverse("store:home")
        self.assertEquals(resolve(url).func,home)

    def test_checkout_url(self):
        url=reverse("store:checkout")
        self.assertEquals(resolve(url).func,checkout)

    def test_orders_url(self):
        url=reverse("store:orders")
        self.assertEquals(resolve(url).func,orders)

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

    
        



