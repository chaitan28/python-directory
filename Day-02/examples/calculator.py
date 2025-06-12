a = 40
b = 30
print("a=40" )
print("b=30" )
def add():
    c=a+b
    print("addtion:", c) 
add()

def sub():
    d=a-b
    print(f"subtration:", d ) #Uses an f-string to embed variable values a = 10 print(f"a={a}")  # Output: a=10

sub()           

def multiply():
    e = a * b
    print(f"mutliplication:", e )

def divide():
    f = a/b
    print( "division:", f )

def remainder():
    h=a%b
    print( "remainder:", h)

remainder()
multiply()
divide()
