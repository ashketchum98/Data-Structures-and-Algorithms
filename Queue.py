class Queue:
	def __init__(self):
		self.list=[]

	def enqueue(self,data):
		self.list.append(data)

	def dequeue(self):
		if not self.list:
			print("Queue Underflow")
		else :	
			print("Element deleted : ",self.list.pop(0))

	def traverse(self):
		if not self.list:
			print("Empty Queue")
		else:
			print(self.list)

a = Queue()
ch='y'
while ch=='y':
	print("Menu")
	print("1 : Enqueue")
	print("2 : Dequeue")
	print("3 : Traverse")
	choice=int(input("Enter your choice : "))
	if choice==1:
		item=int(input("Enter data to be inserted : "))
		a.enqueue(item)
	elif choice==2:
		a.dequeue()
	elif choice==3:
		a.traverse()
	else:
		print(" !!! Wrong choice !!!")

	ch=input("Do you want to continue : (y/n) ")	