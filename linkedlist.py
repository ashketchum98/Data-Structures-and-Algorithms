class Node:
	def __init__(self,data=None,next=None):
		self.data=data
		self.next=next

class LinkedList:

	def __init__(self):
		self.start=None

	def insertatfront(self,data):
		if self.start==None:
			self.start= Node(data)
		else:
			self.newnode= Node(data)
			self.newnode.next=self.start
			self.start=self.newnode
	
	def deleteatfront(self):
		if self.start==None:
			print("Empty List")
		else:
			print("Deleted Element : ",self.start.data)
			self.start=self.start.next

	def traverse(self):
		self.ptr=self.start
		if self.ptr==None:
			print("Empty List")
		else:
			while self.ptr!=None:
				print(" ",self.ptr.data)
				self.ptr=self.ptr.next

a= LinkedList()
ch='y'
while ch=='y':
	print("Menu")
	print("1 : InsertatFront")
	print("2 : Deleteatfront")
	print("3 : Traverse")
	choice=int(input("Enter your choice : "))
	if choice==1:
		item=int(input("Enter data to be inserted : "))
		a.insertatfront(item)
	elif choice==2:
		a.deleteatfront()
	elif choice==3:
		a.traverse()
	else:
		print(" !!! Wrong choice !!!")

	ch=input("Do you want to continue : (y/n) ")	                          


