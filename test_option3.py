import polynomial as poly


print("\n\
###########################################\n\
#### Test for the function: degree\n\
###########################################\
")

p=[4.5,5.0]
print("\nTest degree function using p=",p)
print("Correct answer: 1")
print("Yours:",poly.degree(p))

p=[-2.0,1.0,2.0,0.0,3.0]
print("\nTest degree function using p=",p)
print("Correct answer: 4")
print("Yours:",poly.degree(p))

p=[0.0,0.0,0.0]
print("\n(corner case) Test get_expression function using p=",p)
print("Correct answer: 0")
print("Yours:",poly.degree(p))


p=[]
print("\n(corner case) Test get_expression function using p=",p)
print("Correct answer: 0")
print("Yours:",poly.degree(p))
