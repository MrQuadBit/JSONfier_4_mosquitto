def main():
	#CLI Tool
	item = ""
	json = {}

	#Instructions
	print("----------------------------------------------------------------------------")
	print("Ingresa la clave y el valor separados por un espacio, e.g.")
	print("\nID 1234")
	print("Nombre Fulano")
	print("mnsg Hola mundo con JSON")
	print("JSON ->  {'ID': '1234', 'Nombre': 'Fulano', 'mnsg': 'Hola mundo con JSON'}\n")
	print("**Para salir ingresa la letra 'C' o 'c'**", end="\n\n")

	#Getting and filling the JSON
	while(True):
		item = input()

		#Check if user wants to exit
		if(item == 'C' or item == "c"):
			break

		#Creating dictionary
		item = item.split()
		json[item[0]] = " ".join(item[1:])

		print("JSON -> ", json, end="\n\n")

	#Formatting string
	print("Quieres agregar un '\\' antes de cada '\"' ?")
	answer = input("(y/n)")
	if answer == 'y':
		print(str(json).replace("\'", "\\\""))
	else:
		print(str(json).replace("\'", "\""))
if __name__ == "__main__":
	main()
