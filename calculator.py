
def main():
  
num1=input("Enter the first number:")
num2=input("Enter the second number: ")
op=input("Choose the operation (+, -, /, *): ")


  
  
def calc(num1,num2,op):
   if (num1.isnumeric() and num2.isnumeric())==True:
	   if op=='+':
		   result=int(num1)+int(num2)
		   print("The answer is %d "%(result))
	   elif op=='-':
		    result=int(num1)-int(num2)
		    print("The answer is %d "%(result))
	   elif op=='/':
		    result=int(num1)/int(num2)
		    print("The answer is %d "%(result))
	   elif op=='*':
		    result=int(num1)*int(num2)
		    print("The answer is %d "%(result))
	   else:
		    print("operation is not valid")
   else:
	   print("the numbers were invalid")

calc(num1,num2,op)

if __name__ == '__main__':
	main()
