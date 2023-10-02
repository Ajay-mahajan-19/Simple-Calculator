print(''' There are operators 👇🏻

             + Addition
             - Subtraction
             * Multiplication
             / Division 
        ''')
a=int(input("Enter first value :"))
b=int(input("Enter second value :"))
opr=input("Enter the operator...(+,-,*,/) :")

if opr=="+":
	print('Addition is' ,a+b)
	
elif opr=="-":
	print('Subtraction is' ,a-b)
	
elif opr=="*":
	print('Multiplication is' ,a*b)
	
elif opr=="/":
	print('Division is' ,a/b)
	
else:
	print("Invalid ")
