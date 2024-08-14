# lets store a favourite number(Integer)
favourite_number = 7 
print(f"my favourite number is {favourite_number}")

#string variable
greeting ="Hello Python Students"
print(greeting)

#Boolean Variable
is_python_fun = True
print(f"is python fun? {is_python_fun}")

#Control flow :if elif(elseif),else
temperature = 30
if temperature > 25:
    print("it's hot outside! wear shorts.")
elif temperature > 15:
    print("it's warm outside! wear a t-shirt.")
else:
    print("it's cold outside! wear a jacket.")

# For loop (you know the number of iterations),while loop(Done ubtil a particular condition is met)
# For loop
for  i in range(5):
    print(f"This is a for loop iteration {i}")

#while loop
countdown = 5
while countdown > 0:
    print(f"countdown: {countdown}")
    countdown -=1
print("blast off!")

# Functions
def greet(name):
    return f"Hello, {name}"
# Apply the function
print(greet("John"))
print(greet ("Mercy"))





