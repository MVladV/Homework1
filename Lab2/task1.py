import  re

class Product:

    def __init__(self, price, description, dimensions):
        if not isinstance(price, int):
            raise TypeError()
        elif not isinstance(description, str):
            raise TypeError()
        elif not isinstance(dimensions, int):
            raise TypeError()            
        else:
            self.__dimensions = dimensions
            self.__description = description
            self.__price = price
            self.__allp = 0
        
    def __str__(self):
        return f'Price = {self.__price}, Dimensions = {self.__dimensions}, Description = {self.__description}' 

    def get_price(self):
        return self.__price      

    
class Customer:

    def __init__(self, name, surname, patronymic, phone):
        n = re.match("^/d+-/d+-/d+$", phone)
        if not isinstance(name, str):
            raise TypeError()
        elif not isinstance(surname, str):
            raise TypeError()
        elif not isinstance(patronymic, str):
            raise TypeError()
        elif not isinstance(phone, str):
            raise TypeError() 
        elif n:
            raise TypeError()
        elif not name:
            raise TypeError()
        elif not surname:
            raise TypeError()
        elif not patronymic:
            raise TypeError()                        

        else:
            self.__name = name
            self.__surname = surname
            self.__patronymic = patronymic           
            self.__phone = phone 
    
    def __str__(self):
        return f'Name = {self.__name},\nSurname = {self.__surname},\nPatronymic = {self.__patronymic},\nPhone = {self.__phone}' 


class Order():

    def __init__(self, user, *args):
        self.__user = user
        self.__products = args

    def user(self, user):
        if isinstance(user, Customer):
            self.__user = user
        else:
            raise TypeError('User must be Customer type')  

    def products(self, products):
        if any(not isinstance(product, Store) for product in products):
            raise TypeError("Products must be of Product type")
        self.__products = list(products)              

    def total_price(self, amount):
        total = 0
        for price in self.__products:
            total += price.get_price()
        self.__allp = total*amount    
        return self.__allp        

    def add_elements(self, product):
        if isinstance(product, Store):
            self.__products.append(product)
        else:
            raise TypeError('Product must be Store type')

    def dell_elements(self, product):
        self.products.remove(product)        

    def __str__(self):
        return f'Ordered by:\n{str(self.__user)}\nTotal price: {self.__allp}'                 
        

def main():
    #try:
        product1 = Product(1200, "Drill", 13)
        product2 = Product(2200, "Audi", 980)
        cust = Customer("Vlad", "Mytlitskiy", "Vitalievich", "096-4058-502")        
        print(f'Product number 1:\n {product1}')
        print(f'Product number 2:\n {product2}')
        orders = Order(cust, product1, product2)
        orders.total_price(12)
        print(orders)
    #except Exception:
        print("Exeption!")
main()
