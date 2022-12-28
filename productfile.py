class product:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating
    def display_product_details(self):
        print(self.name,self.price,self.deal_price,self.rating)
    def get_deal_price(self):
        return self.deal_price
class electronic_item(product):
    def set_warranty(self,warranty_in_months):
        self.warranty_in_months=warranty_in_months
    def get_warranty(self):
        return self.warranty_in_months
class grocery_item(product):
    def __init__(self,name,price,deal_price,rating,manufactur_date,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.manufactur_date=manufactur_date
        self.expiry_date=expiry_date
    def display_product_details(self):
        print(self.name,self.price,self.deal_price,self.rating,self.manufactur_date,self.expiry_date)
class orders:
    def __init__(self,delivery_speed,address):
        self.items_in_cart=[]
        self.delivery_speed=delivery_speed
        self.address=address
    def add_item(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print(quantity)
    def display_total_bill(self):
        self.total_bill=0
        for product,quantity in self.items_in_cart:
            price=product.get_deal_price()*quantity
            self.total_bill+=price
        #print(total_bill)

