# learning about string

a = """I trying to learn about python and how the string work
learning is fun
pythin is not python
shah alam is in selangor"""

print(a)


# [] will show what
print(a[1])


for x in "banana":
    print(x)

if "free" not in a:
    print("Yes, free is not present")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])



a = 100000
d = "volvo"
b = "I want the car brand {1} and i want to pay RM {0}"
print(b.format(a, d))



