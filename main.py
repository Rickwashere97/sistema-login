passwordAdmin = "Caremonda"
passwordCajero = "1245"
passwordLogistica = "Nose"
passwordDomiciliario = "EsRappi"
intentos = 3
passWord = ""

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
                   for intento in range(intentos):
                                                              passWord = input("Ingrse su contraseña asignada: ")
                                                              if passWord == passwordAdmin:
                                                                   print ("Acceso consedido: ADMIN")
                                                                   break
                                                              else:
                                                                   intentosRestantes = intentos - intento - 1
                                                                   print(f"Error, le quedan {intentosRestantes} intentos")
              case 2: #CAJERO
                   for intento in range(intentos):
                                                                              passWord = input("Ingrse su contraseña asignada: ")
                                                                              if passWord == passwordCajero:
                                                                                   print ("Acceso consedido: CAJERO")
                                                                                   break
                                                                              else:
                                                                                   intentosRestantes = intentos - intento - 1
                                                                                   print(f"Error, le quedan {intentosRestantes} intentos")
              case 3: #LOGISTICA
                    for intento in range(intentos):
                                                               passWord = input("Ingrse su contraseña asignada: ")
                                                               if passWord == passwordLogistica:
                                                                    print ("Acceso consedido: LOGISTICA")
                                                                    break
                                                               else:
                                                                    intentosRestantes = intentos - intento - 1
                                                                    print(f"Error, le quedan {intentosRestantes} intentos")
              case 4: #DOMICILIARIO
                    for intento in range(intentos):
                                                                               passWord = input("Ingrse su contraseña asignada: ")
                                                                               if passWord == passwordDomiciliario:
                                                                                    print ("Acceso consedido: DOMICILIARIO")
                                                                                    break
                                                                               else:
                                                                                    intentosRestantes = intentos - intento - 1
                                                                                    print(f"Error, le quedan {intentosRestantes} intentos")
                        
   
 