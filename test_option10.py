import polynomial as poly


print("\n\
###########################################\n\
#### Test for the function: multiply\n\
###########################################\
")

p1=[2.0,1.0]
p2=[2.0,1.0]
print("\nTest multiply function using p1=",p1,"and p2=",p2)
print("Correct answer: [4.0, 4.0, 1.0]")
print("Yours:",poly.multiply(p1,p2))


p1=[2.0,1.0]
p2=[2.0,-1.0]
print("\nTest multiply function using p1=",p1,"and p2=",p2)
print("Correct answer: [4.0, 0.0, -1.0]")
print("Yours:",poly.multiply(p1,p2))


p1=[3.0,1.0,2.0,-3.0,4.0]
p2=[1.0,3.0,2.0,-1.0]
print("\nTest multiply function using p1=",p1,"and p2=",p2)
print("Correct answer: [3.0, 10.0, 11.0, 2.0, -2.0, 4.0, 11.0, -4.0]")
print("Yours:",poly.multiply(p1,p2))


p1=[2.0,-3.0,5.0]
p2=[0.0]
print("\nTest multiply function using p1=",p1,"and p2=",p2)
print("Correct answer: [0.0, 0.0, 0.0]")
print("Yours:",poly.multiply(p1,p2))
