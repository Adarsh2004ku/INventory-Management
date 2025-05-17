
fd = open('Inventory.txt',"r")
products= fd.read().split('\n')
fd.close()
for i in products:
    print(i)
ui_prod_id = input("Enter Product ID :")

for product in products:
    if(product.split(',')[0]== ui_prod_id):
        print(product)
for product in products:
    prod_details = product.split(',')
ui_prod_id = input("Enter Product ID :")
ui_prod_qn = input("Enter Product Quantity:")

for product in products:
    product_details = product.split(',')
    if(product.split(',')[0]== ui_prod_id):
        print("Product Name",prod_details[1])
        print("Price :",prod_details[2])
        print("Quantity :",prod_details[3])
        print("Billing Amount :",int(ui_prod_qn)*int(prod_details[2]))
        print("-"*30)
        
        
        
        
"""ui_prod_id = input("Enter Product ID :")

for product in products:
    if(product.split(',')[0]== ui_prod_id):
        print(product)"""