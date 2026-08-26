from funciones import verificationPassword #Acá lo que hacemos es llamar al función creada para la contraseña, primero va el 
#nombre de la hoja donde están las funciones y luego el nombre de la funcuón (de la hoja fuciones porte la función verif...)

passwordAdmin = "Caremonda"
passwordCajero = "1245"
passwordLogistica = "Nose"
passwordDomiciliario = "EsRappi"
intentos = 3 #ponemos la cantidad de intentos que tiene el usario para poner su contraseña correctamente. 

while True:
    print ("\n" + "=" * 30)  
    print ("SELECCIONE SU ROLL".center(30))
    print ("="*30)

    print("\n1. ADMINISTRADOR")
    print("2. CAJERO")
    print("3. LOGISTICA")
    print("4. DOMICILIARIO")

    print("\n5. SALIR")

    while True:
        try:
            seleccion = int(input("INGRSE SU ROLL: "))
            break
        except ValueError:
                print("Ingrese una opción válida: ")

    if seleccion == 5: 
         exit("Tenga buen día")
    else: 
         match seleccion:
              case 1: #ADMIN
                         if verificationPassword (passwordAdmin, intentos):
                                                          print("Bienvenido, ADMIN")
#El error que estaba presentado, era que no se repetía el código cuando se ponia mal la contraseña. Se resolvió en la
# def, el return false, estaba dentro del for            
              case 2: #CAJERO
                         if verificationPassword (passwordCajero, intentos):
                                                          print("Bienvenido, CAJERO") 
              case 3: #LOGISTICA
                         if verificationPassword (passwordLogistica, intentos):
                                                          print("Bienvenido, LOGISTICA") 
              case 4: #DOMICILIARIO
                         if verificationPassword (passwordDomiciliario, intentos):
                                                          print("Bienvenido, DOMICILIARIO") 