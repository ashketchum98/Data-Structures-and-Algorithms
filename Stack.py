class Stack:
	def __init__(self):
		self.list=[]

	def push(self,data):
		self.list.append(data)

	def pop(self):
		if not self.list:
			print("Stack Underflow")
		else :	
			print("Element deleted : ",self.list.pop())

	def traverse(self):
		if not self.list:
			print("Empty Stack")
		else:
			print(self.list)

a = Stack()
ch='y'
while ch=='y':
	print("Menu")
	print("1 : Push")
	print("2 : Pop")
	print("3 : Traverse")
	choice=int(input("Enter your choice : "))
	if choice==1:
		item=int(input("Enter data to be inserted : "))
		a.push(item)
	elif choice==2:
		a.pop()
	elif choice==3:
		a.traverse()
	else:
		print(" !!! Wrong choice !!!")

	ch=input("Do you want to continue : (y/n) ")	