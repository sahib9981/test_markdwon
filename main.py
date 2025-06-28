import conversion,verif_email
import mathutils.operations


print("1)_conversion\n2)_verification e-mail\n3)_factorielle\n")
choix = input("Entre votre nombre de choix : ")

change_km = conversion.km_to_miles(100)
change_c = conversion.celsius_to_fahrenheit(23)

match choix:
    case '1':
        print("a)_la conversion de km a miles\nb)_la conversion de C a F")
        test = input("choisir un conversion : ")
        if test == 'a':
            #change de km
            print(f"100km = {change_km} miles")
        elif test == 'b':
            #change c
            print(f"23C = {change_c} F")
        else:
            print("Votre choix n'est pas disponible.")
    case '2':
        verif_email.est_valid()
    case '3':
        #factorielle.
        mathutils.operations.fact(3)
    case _ :
        print("Votre choix n'est pas disponible.")





