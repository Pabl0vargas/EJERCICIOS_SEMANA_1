#EJERCICIO_SEMANA_3
products = []

#we define the function to add product, price and quantity
def add_product(name, price, quantity):
    product = {
        "nombre": name,
        "precio": price,
        "cantidad": quantity
    }
    products.append(product)
    
#we define the function to search products
def search_product(name):
    for product in products:
        if product["nombre"] == name:
            return product
    return None
#we define the function to update price   
def update_price(name, new_price):
    for product in products:
        if product["nombre"] == name:
            product["precio"] = new_price
            print(f"El producto con el nombre {name} fue actualizado ")
            return
    print(f"El producto {name} no se en el inventario")
#we define the function to delete product
def delete_product(name):
    for product in products:
        if product["nombre"] == name:
            products.remove(product)
            print(f"Producto {name} eliminado con éxito.")
            return
    print(f"El producto {name} no se encuentra en el inventario.")

#lambda function to calculate total inventory
calculate_total = lambda: sum(map(lambda x: x["precio"] * x["cantidad"], products))

def menu():
    print(" \n====Gestión de productos====\n 1. Agregar producto\n 2.  Buscar productos\n " 
    "3. Actualizar precio\n 4. Eliminar producto\n 5. total del inventario\n 6. Salir del programa")
      
while True:
    menu()
    option_str = input("Ingrese la opción deseada: ").strip()# removes whitespace

    if not option_str.isdigit():# check if it is a digit
        print("\nOpción no válida. Por favor, elija una opción del menú.")
        continue
    
    option = int(option_str)#convert to int

    match option:
        case 1:
            name = input("\nIngrese el nombre del producto: ").lower().strip()
            if search_product(name):
                print(f"El producto '{name}' ya existe en el inventario.")
                continue
            if not name or not name.isalpha():  # Check that the name only contains letters
                print("El nombre debe contener solo letras y no puede estar vacío.")
                continue

           

            price_str = input("Ingrese el precio del producto: ").strip()
            if not price_str.replace('.', '', 1).isdigit():
                print("El precio debe ser un número válido.")
                continue
            price = float(price_str)
            if price < 0:
                print("El precio no puede ser negativo.")
                continue

            quantity_str = input("\nIngrese la cantidad de productos: ").strip()
            if not quantity_str.isdigit():
                print("La cantidad debe ser un número entero.")
                continue
            quantity = int(quantity_str)
            if quantity < 0:
                print("La cantidad no puede ser negativa.")
                continue
            add_product(name, price, quantity)
            print(f"Producto {name} agregado con éxito.")

        case 2:
                name = input("\nIngrese el nombre del producto que desea consultar: ").strip().lower()
                product = search_product(name)
                if product:    
                    print(f"\n|Nombre: {product['nombre']}| Precio: {product['precio']:,.2f}| Cantidad: {product['cantidad']}|")
                else:
                    print(f"El producto '{name}' no se encuentra en el inventario.")    
        case 3:
                name = input("\nIngrese el nombre del producto a actualizar: ").strip().lower()
                if not name or not name.isalpha():
                    print("El nombre solo debe contener letras y no puede estar vacío.")
                    continue

                new_price = input("\nIngrese el nuevo precio del producto: ").strip().lower()
                if not new_price.isdigit():
                    print("El precio debe ser un número válido.")
                    continue
                new_price = float(new_price)
                if new_price < 0:
                    print("El precio no puede ser negativo.")
                    continue
                update_price(name, new_price)      
        case 4:
            name = input("\nIngrese el nombre del producto a eliminar: ").strip().lower()
            if not name or not name.isalpha():
                print("El nombre solo debe contener letras y no puede estar vacío.")
                continue
            delete_product(name)
        case 5:
            total = calculate_total()
            print(f"\n| El valor total del inventario es: | ${total:,.2f} |")
        case 6:
            print("Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Intente de nuevo.")