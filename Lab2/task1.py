import  re

class Product:

    def __init__(self, price, description, dimensions):

        self.dimensions = dimensions
        self.description = description
        self.price = price
        
    def __str__(self):
        return f'\tPrice = {self.__price}, \n\tDimensions = {self.__dimensions}, \n\tDescription = {self.__description}'     

    @property
    def price(self):  
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError()
        if price < 0:
            raise TypeError()
        self.__price = price 

    @property
    def description(self):  
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError()
        self.__description = description 

    @property
    def dimensions(self):  
        return self.__dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        if not isinstance(dimensions, int):
            raise TypeError()
        self.__dimensions = dimensions     



    
class Customer:

    def __init__(self, name, surname, patronymic, phone):

        self.name = name
        self.surname = surname
        self.patronymic = patronymic           
        self.phone = phone 

    def __str__(self):
        return f'\tName = {self.__name},\n\tSurname = {self.__surname},\n\tPatronymic = {self.__patronymic},\n\tPhone = {self.__phone}' 

    @property
    def name(self):  
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise TypeError()        
        if not isinstance(name, str):
            raise TypeError()
        self.__name = name   

    @property
    def surname(self):  
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if not surname:
            raise TypeError()
        if not isinstance(surname, str):
            raise TypeError()
        self.__surname = surname 

    @property
    def patronymic(self):  
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, patronymic):
        if not patronymic:
            raise TypeError()
        if not isinstance(patronymic, str):
            raise TypeError()
        self.__patronymic = patronymic 
        
    @property
    def phone(self):  
        return self.__phone

    @phone.setter
    def phone(self, phone):
        n = re.match("^/+38 /(/d{3}/) /d{3}-?/d{2}-?/d{2}$", phone)
        if not isinstance(phone, str):
            raise TypeError()
        if n:
            raise TypeError()            
        self.__phone = phone                        


class Order():

    def __init__(self, user, *args):
        self.user = user
        self.products = args

    @property
    def user(self):
        return self.__user

    @user.setter    
    def user(self, user):
        if isinstance(user, Customer):
            self.__user = user
        else:
            raise TypeError('User must be Customer type')  

    @property
    def products(self):
        return self.__products
    
    @products.setter
    def products(self, products):
        if any(not isinstance(product, Product) for product in products):
            raise TypeError("Products must be of Product type")
        self.__products = list(products)              

    def total_price(self, amount):
        total = 0
        for price in self.__products:
            total += price.price    
        return total * amount        

    def add_elements(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise TypeError('Product must be Product type')

    def dell_elements(self, product):
        self.products.remove(product)        

    def __str__(self):
        return f'  Ordered by:\n{str(self.__user)}\n\tTotal price: {self.total_price(12)}'                 
        

def main():
    try:
        product1 = Product(1200, "Drill", 13)
        product2 = Product(2200, "Audi", 980)
        cust = Customer("Vlad", "Mytlitskiy", "Vitalievich", "+38(096)-405-85-02")        
        print(f'  Product number 1:\n {product1}')
        print(f'  Product number 2:\n {product2}')
        orders = Order(cust, product1, product2)
        print(orders)
    except Exception:
        print("Exeption!")
main()
