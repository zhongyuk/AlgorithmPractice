"""
Descriptions: last-in, first-out (LIFO) principle
Attributes:
	top: a pointer pointing at the top element/node
	capacity:  the maximum capacity of the stack
	size: the current size of the stack
Methods: 
	push: insert an element to the top of the stack, throws stack overflows error if full
	pop: delete an element from the top of the stack, returns the data of the deleting element,
	throws stack underflows error if empty
	isempty: test if stack is empty or not
"""

class Node(object):
	def __init__(self, data, next, prev):
		self.data = data
		self.next = next
		self.prev = prev

class Stack(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0
		self.top = None

	def isempty(self):
		if self.size == 0:
			return True
		else:
			return False

	def push(self, data):
		if self.size == self.capacity:
			raise IndexError("Stack overflows")
		elif self.size == 0:
			self.top = Node(data, None, None)
			self.size += 1
		else:
			node = Node(data, None, self.top)
			self.top.next = node
			self.top = node
			self.size += 1

	def pop(self):
		if self.isempty():
			raise IndexError("Stack underflows")
		else:
			data = self.top.data
			self.top.prev.next = None
			self.top = self.top.prev
			return data

class testStack(object):
	def __init__(self):
		
