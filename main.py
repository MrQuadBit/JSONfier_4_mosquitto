import sys

def main():
	n = len(sys.argv)
	#Check if there is an argument
	if(n > 1):
		#Inline argument
		evalJSON(sys.argv[1])
	else:
		#Console manipulation
		op = instructionsMenu1()
		if(op == 1):
			#Files Reader
			print("Leer Archivo")
		elif(op == 2):
			#CLI Tool
			item = ""
			json = {}

			while(True):
				item = instructionsMenu2()

				#Check if user wants to exit
				if(item == 'C' or item == "c"):
					break

				item = item.split()
				json[item[0]] = "".join(item[1:])
			print(json)
		else:
			print("Opción invalida")

def instructionsMenu2():
	print("\n-----------------------------------------------------------")
	print("Ingresa la clave y el valor separados por un espacio")
	print("e.g.\n-->ID 1234")
	print("**Para salir ingresa la letra 'C' o 'c'**")
	return input()
	print("-----------------------------------------------------------\n")

def instructionsMenu1():
	print("\n-----------------------------------------------------------")
	print("Qué quieres hacer?")
	print("1.-Leer JSON desde archivo")
	print("2.-Crear un JSON")
	return int(input())
	print("-----------------------------------------------------------\n")

def evalJSON(s):
	print("404 function not found")

if __name__ == "__main__":
	main()
