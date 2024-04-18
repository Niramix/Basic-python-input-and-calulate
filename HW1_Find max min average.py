
#Input number and variable

lst = []
n = int(input("How many number for test: "))
i = 1
print("Input", n, "number for test.")


#While loop for input number
while n > 0:
    ele = int(input("Input number {}: ".format(i)))
    lst.append(ele) # adding the element
    n = n-1
    i = i+1
    
#Calculate
maximum = max(lst, key=int)
minimum = min(lst, key=int)
average = sum(lst)/len(lst)


#All result
print("\nAll numers =",lst)
print("\nMaximum number =",maximum)
print("\nMinimum number =",minimum)
print("\nAverage of list =", round(average))