# syntax
# variable declaration
x = 15
y = 4

# arithmetic operations
sum = x + y     #addition
diff = x - y    #subtraction
prod = x * y    #multiplication
div = x / y     #division

# comparison operation
greater = x> y #greater than
lesser = x < y  #less than
equal = x == y  #equal to
not_equal = x != y #not equal to

# logical operations
and_op = (x > 10) and (y < 10)  #logical AND
or_op = (x > 10) or (y > 10)    #logical OR 
not_op = not(x > 10)            #logical NOT

# print statements
print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Division:", div) 
print("Is x greater than y?:", greater)
print("Is x less than y?:", lesser)
print("Is x equal to y?:", equal)
print("Is x not equal to y?:", not_equal)
print("Logical AND result:", and_op)
print("Logical OR result:", or_op)
print("Logical NOT result:", not_op)


# data types
#strings
name = "Muso"
sex = "Femaale"
hobby = "Sleeping"

#integers
age = 24

float
height = 5.6

bool
is_student = True
is_employed = False

# print data types
print("Name:", name)
print("Sex:", sex)
print("Hobby:", hobby)     
print("Age:", age)
print("Height:", height)
print("Is Student?:", is_student)

#list
fav_fruits = ["Apples", "Grapes", "Bananas"]
print("Favorite Fruits:", fav_fruits)

#list manipulation
fav_fruits.append("Mangoes")
print("Updated Favorite Fruits:", fav_fruits)


#tuple
fav_colors = ("Red", "Blue", "Green")
print("Favorite Colors:", fav_colors)

#dictionary
person = {
    "name": "Muso",
    "age": 24,
    "hobby": "Sleeping"
}
print("Person Dictionary:", person)

#dictionary manipulation
person["age"] = 25
print("Updated Person Dictionary:", person)


#set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers Set:", unique_numbers)
