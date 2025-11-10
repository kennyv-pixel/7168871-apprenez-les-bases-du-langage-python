nombre1 = input("Ecrivez un nombre")
nombre2 = intpu("Ecrivez un autre nombre")

if not nombre1.isnumeric() and nombre2.isnumeric():

	 raise SystemExit("Fin du programme")
	 nombre1 = int(nombre1)
	 nombre2 = int(nombre2)

operation = input("Entrez l'opération souhaitée ['+', '-', '*', '/']: ")

if operation not in ['+', '-', '*', '/']:
	print("Erreur le symbole doit etre '+';'-','*', '/'.")
	raise SystemExit("fermeture")

if operation == '+':
	resultat = nombre1 + nombre2
elif opération == '-':
	resultat = nombre1 - nombre2
elif operation == '*':
	resultat = nombrer1 * nombre2
elif operation == '/':
	resultat = nombre1 / nombre2
	if nombre2 == 0:
		raise SystemExit("fermeture")

	resultat = round(nombre1/nombre2, 2)

	print(f" Le résultat de l'opération est : {round(resulat, 2)}")		
