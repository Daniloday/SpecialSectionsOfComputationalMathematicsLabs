from convert import *
from lab1 import *


def main():
	b = int(2 ** 64)
	convert = Convert(b)
	lab1 = Lab1(convert, b)
	while True:
		print("Choose option:\n1. Small to large \n2. Add \n3. Sub \n4. Mul \n5. Sqr \n6. Div \n7. Power\n8. Test1\n9. Test2 \nN/n to quit" )
		choose = input()
		if choose == '1':
			lab1.small_to_large()
		if choose == '2':
			lab1.add()
		if choose == '3':
			lab1.sub()
		if choose == '4':
			lab1.mul()
		if choose == '5':
			lab1.sqr()
		if choose == '6':
			lab1.div()
		if choose == '7':
			lab1.power()
		if choose == '8':
			lab1.test1()
		if choose == '9':
			lab1.test2()
		if choose == 'n' or choose == 'N':
			break
	

if __name__ == '__main__':
	main()