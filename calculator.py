
def main():
  num11=input("Enter the first number: ")
  num1=int(num11)
  num22=input("Enter the second number: ")
  num2=int(num22)
  op=input("Choose the operation (+, -, /, *): ")
 
#   cal(num1,num2,op)
#   def cal(num1,num2,op):
  result=0
 
  if num1.isnumeric() and num1.isnumeric():
	 if op == "+":
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


if __name__ == '__main__':
	main()
