def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y

print("please choose a option")
print("a add ")
print("b subtract ")
print("c multiply ")
print("d divide ")

choice=input("please choose an option ")
x=int(input("please first number "))
y=int(input("please second number "))
if choice=="a":
  print(add (x,y))
elif choice=="b":
  print(subtract (x,y))
elif choice=="c":
  print(multiply (x,y))
elif choice=="d":
  print(divide (x,y))
else:
  print("invalid input")