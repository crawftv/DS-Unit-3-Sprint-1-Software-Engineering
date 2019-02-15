from acme import Product
import random
ADJECTIVE = ['Awesome', 'Shiny', 'Impressive','Portable', 'Improved',"Cool","neat","chill","mystery"]
NOUN = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', "box","book","binder clip","notecards"]

def generate_products(n=30):
    product_list = []
    for i in range(0,n):
        product_name = choice(ADJECTIVE) +" " +choice(NOUN)
        weight= random.randint(5,100)
        price = random.randint(5,100)
        flamability=random.uniform(0,2.5)
        product = Product(product_name,weight= weight, price=price,flamability = flamability)
        product_list.append(product)
        unique_products = len(set(product.name for product in product_list))
        average_price = sum([product.price for product in product_list])/len([product.price for product in product_list])
        average_weight = sum([product.weight for product in product_list])/len([product.weight for product in product_list])
        average_flammability = sum([product.flamability for product in product_list])/len([product.flamability for product in product_list])
        print_statement = "ACME  CORPORATION OFFICIAL INVENTORY REPORT\n" \
        "Unique product names: "+str(unique_products)+"\n"\
        "Average price: " + str(average_price)+\
        "\nAverage weight: "+ str(average_weight)+\
        "\nAverage flammability: " + str(average_flammability)
    print(print_statement)