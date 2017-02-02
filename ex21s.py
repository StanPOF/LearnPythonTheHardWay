def add(a, b):
    print "ADDING %r + %r" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %r - %r" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLY %r * %r" % (a, b)
    return a * b

def divide (a, b):
    print "DIVIDING %r / %r" % (a, b)
    return a / b


print "Let's do some math with just functions!"

x = float(raw_input("x="))
y = float(raw_input("y="))
m = float(raw_input("m="))
n = float(raw_input("n="))
p = float(raw_input("p="))
q = float(raw_input("q="))
s = float(raw_input("s="))
w = float(raw_input("w="))

age = add(x, y)
height = subtract(m, n)
weight = multiply(p, q)
iq = divide(s, w)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"