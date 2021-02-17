
def function():

	while True:

		number = int(input("Choose a number between 1 and 1000 to see if its Odd or Even: "))
		print("                                                                            ")

		odd = number % 2 == 1
		even = number % 2 == 0

		if even:
			print(f"The number {number} is an Even Number !")
			print("                                                                            ")

		elif odd:
			print(f"The number {number} is an Odd Number !")
			print("                                                                            ")

		choose = input("Do you have another number? Answer with Yes or No! ").lower()
		print("                                                                            ")

		yes = choose == "yes"
		no = choose == "no"

		if yes:
			pass

		if no:
			break

if __name__ == '__main__':
	function()
