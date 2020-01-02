# Fibonacci Series F(n) = F(n-1) + F(n-2) assuming first two numbers are 1,1
# This Program will give nth Fibonacci Number.

# Using Recursion - Inefficient Solution
def fib(n):
	
	if n==1 or n==2:
		result = 1
	else:
		result = fib(n-1) + fib(n-2)
	return result

# Memoized Solution - Top Down Approach - Making Recursive solution Efficient.
def fib_memoized(n, memo_arr):

	if memo_arr[n]!= None:
		return memo_arr[n]
	if n==1 or n==2:
		result = 1
	else:
		result = fib_memoized(n-1, memo_arr) + fib_memoized(n-2, memo_arr)
	memo_arr[n] = result
	return result

# Using Bottom Up Approach
def fib_bottom_up(n):

	if n==1 or n==2:
		return 1
	else:
		bottom_up_arr = []
		bottom_up_arr.append(1)
		bottom_up_arr.append(1)

		for i in range(2,n):
			bottom_up_arr.append(bottom_up_arr[i-1] + bottom_up_arr[i-2])

		return bottom_up_arr[n-1]

number = 6
print("Using Recursive - ",fib(number)) # Using Recursive Solution

memo_arr = [None]*(number+1)
print("Using Memoized - ",fib_memoized(number,memo_arr)) # Using Memoized Solution

print("Using Bottom Up Approach - ",fib_bottom_up(number)) # Using Bottom Up Approach

