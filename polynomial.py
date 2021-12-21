def display_menu():
    """ Display the list of polynomial available tools"""
    print("1-Insert; 2-Remove; 3-Info; 4-Evaluate; 5-Scaling; 6-Derive; 7-Integrate")
    print("8-Summation; 9-Subtract; 10-Multiply; 11-Divide")

    
def get_polynomial_easy(all_coef):
    """ Easy way out to use if you cannot implement get_polynomial as requested """
    return list(map(float,all_coef.split()))

def display_list(list_poly):   #displays the list of polynomials 
   l=len(list_poly)   
   for i in range(l):
       print(i+1,":",get_expression(list_poly[i]),)   #prints the index+1 and then the polynomial
    
def get_expression(p):
    degree=len(p)-1
    polynomial=""   #intialize the string
    for i in p:
        if degree>1 and i>0:   #for positive numbers above the degree of 1
            if i!=0:
                polynomial+="+"+str(i)+"x^"+str(degree)
            degree=degree-1
        elif degree>1 and i<0:   #for negative numbers above the degree of 1
            if i!=0:
                polynomial+=str(i)+"x^"+str(degree)
            degree=degree-1
        elif degree==1 and i>0:   #for postive numbers with the degree of 1
            if i!=0:
                polynomial+="+"+str(i)+"x"
            degree=degree-1
        elif degree==1 and i<0:   #for negative numbers with the degree of 1
            if i!=0:
                polynomial+=str(i)+"x"
            degree=degree-1
        elif degree==0 and i<0:   #for negative number with length of 1
            if i!=0:
                polynomial+=str(i)
                degree=degree-1
        elif degree==0 and i>0:   #for positive number with length of 1
            if i!=0:
                polynomial+="+"+str(i)
                degree=degree-1
        elif degree>1:   #for zero with degree>1
            if i==0:
                polynomial+=""
                degree=degree-1
        elif degree==1:   #for zero with degree=1
            if i==0:
                polynomial+= ""
                degree=degree-1
        elif degree==0:   #for zero with degree=0
            if i==0:
                polynomial+=""
                degree=degree-1
        else:
            if i!=0:
                polynomial+="+"+str(i)
    if polynomial=="" or len(p)==0:   #corner cases with zero and 'enter' entry
        polynomial="0.0"
    return polynomial

def degree(p):   #returns the degree of the function
    if len(p)==0:   #for cases where the degree should be zero
        max_degree=len(p)
    elif p==[0]*len(p):   #if the polynomial is equal to one number degree=zero
        max_degree=0
    else:   #basic function that returns the degree
        max_degree=len(p)-1
    return max_degree

def evaluate(p,x):   #evaluate the polynomial at a specific x value
    deg=len(p)-1
    value=0   #intialize the viariable value
    for i in p:
        value=value+i*(x**deg)   #adds on to the previous value
        deg=deg-1
    return value

def scale(p,s):   #scales the entire polynomial by a specific s value
    multiple=[]   #intialize the list
    scale_degree=len(p)-1
    scale=s
    for i in p:
        if p[0]:
            multiple=multiple+[(s*i)**1]   #for cases where len(p)-1 does not work
        else:
            multiple=multiple+[(s*i)**scale_degree]
            scale_degree=scale_degree-1   #lowers the degree by one to go to the next number in the list
    return multiple

def derive(p):   #derivative of polynomial
    d=[]   #intializes the list
    d=p[:]   #copies the list
    exponent=len(p)-1
    if len(p)<=1:
        d[0]=0.0   #derivative of a constant is zero
    else:
        del(d[exponent])   #deletes the previous constant
        for i in range(exponent):
            d[i]=d[i]*exponent   #ax^(exp)dx = a*exp^(exp-1)
            exponent=exponent-1
    return d

def integrate(p,lo,up):   #integrate polynomial then evaulate it
    integral=[]   #intialize list
    i_value=0   #intialize value to zero
    exponent_i=len(p)
    for i in p:
        integral=integral+[i/exponent_i]   #integral of ax^(exp)= a(exp+1)*x^(exp+1)
        exponent_i=exponent_i-1

        exponent_i=len(p)
    for j in integral:
        i_value=i_value+((j)*(up**exponent_i))-((j)*(lo**exponent_i))   #plugs in the bounds and subtracts them 
        exponent_i=exponent_i-1
    return i_value

def add(p1,p2):   #summation of two polynomials
    p3=[]   #intialize the list that contains the final polynomial
    if len(p1)>=len(p2):   #finds the largest range 
        r=len(p1)
        d=len(p1)-len(p2)
        addition_list=d*[0.0]+p2   #new list to perform addition
        for i in range(r):
            c=(float(p1[i])+float(addition_list[i]))   #allows coeffiecients of the same degree to be added
            p3=p3+[c]
    else:   #performs the same task as above but with len(p2)>len(p1)
        r=len(p2)
        d=len(p2)-len(p1)
        addition_list=d*[0.0]+p1   #new list to perform addition
        for i in range(r):
            c=(float(p2[i])+float(addition_list[i]))   #allows coeffiecients of the same degree to be added
            p3=p3+[c]
    return p3
    
def subtract(p1,p2):   #subtraction of two polynomials
    p3=[0.0]*len(p2)   #new list
    for i in range(len(p2)):
        p3[i]= -1*p2[i]   #p=p1-p2 => p=p1+p3 => p3=-p2
    return add(p1,p3)

def multiply(p1,p2):   #mutliplication of two polynomials
    p=[0.0]   #new list containing the multiplied coefficient of the polynomials
    degree_multi=len(p1)-1   #p*(coefficient of p1)
    for i in range(len(p1)):
        if i==0:   #for multiplication of zero
            print("0.0")
        else:
            scalar=p1[i]   #scales p2
            p3=scale(p2,scalar)   #p3=p2*scalar
            p3=p3+[0.0]*degree_multi 
            p=add(p3,p)   #add the coefficients of the same degree
            degree_multi=degree_multi-1
    return p
