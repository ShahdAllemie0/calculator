
def main():
	#write your code here
  num1=input("Enter the first number: ")
  num2=input("Enter the second number: ")
  op=input("Choose the operation (+, -, /, *): ")

 
  if num1.isnumeric() and num1.isnumeric():
	 if op=='+':
		 result=num1+nume2
		 print("The answer is 24 "+result)
	 elif op=='-':
		 result=num1-nume2
		 print("The answer is 24 "+result)
	 elif op=='/':
		 result=num1/nume2
		 print("The answer is 24 "+result)
	 elif op=='*':
		 result=num1*nume2
		 print("The answer is 24 "+result)
	 else:
		print("operation is not valid")
  else:		
	  print("the numbers were invalid")	 		     		 		 
 		
	

	pass
	



if __name__ == '__main__':
	main()
