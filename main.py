import sys

def main():
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

def instructions():
	print("\n-----------------------------------------------------------")
	print("Ingresa la clave y el valor separados por un espacio")
	print("e.g.\n-->ID 1234")
	print("**Para salir ingresa la letra 'C' o 'c'**")
	return input()
	print("-----------------------------------------------------------\n")
if __name__ == "__main__":
	main()
