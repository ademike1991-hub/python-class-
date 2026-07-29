list_of_fruit = [apple,  banana,orange, grape]
print(list_of_fruit)
print(list_of_fruit[0])
print(list_of_fruit[1])
print(list_of_fruit[2])
print(list_of_fruit[3])

number_
of_fruit = len(list_of_fruit)
print("Number of fruit in the list:", 
number_of_fruit)

for loop 
in range(number_of_fruit):
    print(list_of_fruit[loop])

    while loop
    while true:
        print("This is an infinite loop")
        press ctrl+c to stop the loop

        FOUNCTIONS (arguments and return values)

        def simple_caculation(num1, num2, operation):
        
            if operation == "add":
                return num1 + num2
            elif operation == "subtract":
                return num1 - num2
            elif operation == "multiply":
                return num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    return num1 / num2
                else:
                    return "Error: Division by zero"
            else:
                return "Error: Invalid operation"
                please choose a valid operation: add, subtract, multiply,or divide]


      Example usage of the function:
      sum_result = simple_calculation(7, 40, "divide")
  print("The result of the operation is:", result)
  print("The result of the operation is:", 
  
  OOP
  class-A blueprint for creating objects(instances) that encapsulates data and behavior related to that data. It defines the properties (attributes)
   and methods (functions) defineed within
   a classattributes and can be called on the class
   itselfs or its instances.
   
   Difine a class name 'Animal'
   class Animal:
       def __init__(self, name, species):
           self.name = name
           self.species = species

       def make_sound(self):
           pass

           Example usage of the class Animal class
           lion = Animal("Leo", "Lion"190)
           print(lion.name)  # Output: Leo
           dog = Animal("Buddy", "Dog"25)
              print(dog.species)  # Output: Dog
              cat = Animal("Whiskers", "Cat"5)
              print(cat.name)  # Output: Whiskers

              dog.display_info()
              dog.make_sound(Bark!)
              lion.make_sound(Roar!)
              cat.make_sound(Meow!)
