from productfile import product
from productfile import electronic_item
from productfile import grocery_item
from productfile import orders
import unittest

class producttesing(unittest.TestCase):
    def setUp(self):
        self.milk = grocery_item("milk", 40, 20, 3, 45, 3)
        self.tv = electronic_item("tv", 3, 3, 2)
        self.orderobj = orders("prime", "hyd")
        #self.orderobj = orders("prime", "hyd")
        self.orderobj.add_item(self.milk, 3)
        self.orderobj.add_item(self.tv, 2)
    def test_disply(self):
        self.assertEqual(self.milk.name,"milk")
        self.assertEqual(self.milk.price,40)
        self.assertEqual(self.milk.deal_price,20)
        self.assertEqual(self.milk.rating,3)
        self.assertEqual(self.milk.manufactur_date,45, "manufactur_date is invalid")
        self.assertEqual(self.milk.expiry_date,3)
    def test_get_deal_price(self):
        self.assertEqual(self.milk.get_deal_price(),20)
        self.assertEqual(self.orderobj.items_in_cart[0][1],3)
    def test_add_items(self):
        self.assertEqual(self.orderobj.items_in_cart[0][0].name,"milk")
        self.assertEqual(self.orderobj.items_in_cart[0][0].price,40)
        self.assertEqual(self.orderobj.items_in_cart[0][0].deal_price,20)
    def test_total(self):
        self.orderobj.display_total_bill()
        self.assertEqual(self.orderobj.total_bill,66)
