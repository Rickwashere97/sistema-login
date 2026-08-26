def verificationPassword (passwordCorrect, intentos):
        for intento in range (intentos):
            password = input("INGRESE SU CONTRASEÑA: ")
            if password == passwordCorrect:
                return True
            else: 
                intentosRestantes = intentos - intento - 1  
                print (f"CONTRASREÑA INCORRECTA, LE QUEDAN {intentosRestantes} INTETOS.")
        return False