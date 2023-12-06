from .models import *

# Return all the customer from the customer table
x= Customer.objects.all()


# Return first customer from the customer table
x = Customer.objects.first()


# Return last customer from the customer table
x = Customer.objects.last()


# Return single customer by name from the customer table
x= Customer.objects.get(name='Ashik')

# Return single customer by id from the customer table
x = Customer.objects.get(id=2)


# Return all the orders related to the customer
x = Customer.objects.get(name='Ashik')
allOrder = x.order_set.all()


# Return the customer name related to the order
x1 = Order.objects.first()
cName = x1.customer.name

# Return the product from the Product table with the value of 'Outdoor' in category attribute
x = Product.objects.filter(category='Outdoor')

#sort the order by id
ftl = Product.object.all().order_by('id')
ltf = Product.object.all().order_by('-id')


# return all products with tag of Sports (query field many to many)

x = Product.objects.filter(tags__name = 'Sports')


#Retruns total count for each product ordered

allOrder = {}

for order in x1.order_set.all():
    if order.product.name in allOrder:
        allOrder[order.product.name] += 1
    else:
        allOrder[order.product.name] = 1









