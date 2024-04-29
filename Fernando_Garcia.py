#Programa hecho por Fernando Garcia seccion 1

pikachu=4000
otaku=5000
Pulpo=5200
anguila=4800
pika=0
otak=0
pulp=0
ang=0
while True:
    opcion=int(input("Bienvenido a Maki Sushi, porfavor eliga sus sushi \nPresione 1  para Pikachu roll ($4000) \nPresione 2 para Otaku Roll ($5000) \nPresione 3 para Pulpo venenoso Roll ($5200) \nPresione 4 para Anguila electrica roll ($4800) \nPresione 5 para terminar \n"))
    
    if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=4 and opcion!=5:
        print("Seleccione una opcion valida \n")  
    
    if opcion==1:
        pika=pika+1
    

    if opcion==2:
        otak=otak+1

    
    if opcion==3:
        pulp=pulp+1


    if opcion==4:
        ang=ang+1

    
    if opcion==5:
       break
total= (pika*pikachu)+(otak*otaku)+(pulp*Pulpo)+(ang*anguila)
total_rolls= pika+otak+pulp+ang
print("Tus sushis elegidos son: \nPikachu roll: ", pika)
print("Otaku roll: ", otak )
print("Pulpo roll: ", pulp)
print("Anguila roll: ", ang)
print("El total de rolls es de:", total_rolls)
print("")
while True:
    opciondesc=int(input("Presione 1 si posee un codigo de descuento \nPresione 2 si no posee descuento \n1"))
    if opciondesc ==2:
        print("El subtotal es de: ",total)
        break
    
    if opciondesc==1:
        descuento=str(input("Ingrese su codigo de descuento: \n"))
        if descuento=="soyotaku":
            totalConDescuento=total*0.9
            desc=total*0.1
            print("El subtotal es de: ",total)
            print("El descuento es de: ", desc)
            print("El total de la venta es de: ", totalConDescuento)
            break
        if descuento != "soyotaku":
            print("codigo incorrecto")
            print("El subtotal es de: ",total)
            break

