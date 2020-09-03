print("Hello World!")

# import matplotlib.pyplot as plt # abbreviate module name as plt
# import numpy

'''
a = numpy.random.randn(10000) # fills a list called 'a' with 10000 values

plt.hist(a) # creats the graph/histogram
plt.show() # shows the graph


# how to define a function
def addTip(subTotal, percent):
	billWithTip = subTotal + percent * subTotal
	return billWithTip

amount = float(input("How much was your bill?"))
tip = float(input("How much are you willing to tip?"))

# call the function
grandTotal = addTip(amount, tip)
print("Your total bill with tip is $", round(grandTotal, 2))
'''

def hyp(a, b):
	hyp = (a**2 + b**2)**0.5
	return hyp
	
def mean(a, b, c):
	mean = (a + b + c)/3
	return mean

def perimeter(base, height):
	perimeter = base*2 + height*2
	return perimeter

print(hyp(3,4))
print(mean(3, 4, 7))
print(perimeter(3, 4))s