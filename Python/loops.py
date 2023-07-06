class Test:
    def even ():
        a=int(input("Enter first number -> "))
        b=int(input("Enter second number-> "))
        for x in range(a,b):
            if x%2==0:
                print(x, end=" ")
    def odd ():
        a=int(input("Enter first number -> "))
        b=int(input("Enter second number-> "))
        for z in range(a,b):
            if z%2!=0:
                print(z, end=" ")
Test.odd()
Test.even()

def array_types():
    arr_1=[1,2,3,4,5,6,"test",23,36,False,23+4j]
    rrr_2=(1,2,3)
    arr_3={"Adrija", 123, 569}  
    arr_4={
           "name":Adrija
    }
