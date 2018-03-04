
# coding: utf-8

# In[20]:


#Implement try and catch block with respect to divide by 0 error
def Numberoperation(x,y):
    #calculate the 5/0
    try:
        x/y
    except ZeroDivisionError:
        print ("A number cannot be divided by 0")
#Define the denominator as 0 to show the exception handling.
b=0
#User defined input for numerator.
a=input("Enter the integer number which needs the division operation ")
#Calling function for calculation and exception handling.
Numberoperation(int(a),b)

