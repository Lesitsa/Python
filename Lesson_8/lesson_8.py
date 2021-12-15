'''№1 Classes
Написать класс “animals” (животные), который включает общие признаки и 
поведения животных. От “animals” наследовать класс “mammals” (млекопитающие),
который включает общие признаки и поведения млекопитающих.
От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака),
у каждого свои признаки и поведения.
'''
print('№1 Classes \n')
class Animals:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def say(self, text):
        print(f"{text} I'm {self.age} years old.")

animal = Animals('male', 15)
animal.say("Hello, I'm Animal.")
print()


class Mammals(Animals):
    def __init__(self, gender, age, weight):
        super().__init__(gender, age)
        self.weight = weight
    
    def say_weight(self):
        if self.gender == 'male':
            print(f'My weight is {self.weight} kg')
        else:
            print('What are scales?')

mammal = Mammals('female', 4, 10)
mammal.say("Hi, I'm Mammal!")
mammal.say_weight()
print()


class Human(Mammals):
    def __init__(self, gender, age, weight, name, _pasport):
        super().__init__(gender, age, weight)
        self.name = name
        self._pasport = _pasport
    
    def data(self):
        print(f'Name: {self.name} \nPassport data: {self._pasport}')

Mike = Human('male', 17, 60, 'Mike', 7821075750)
Mike.say("Hi, I'm Mike!")
Mike.say_weight()
Mike.data()
print()


class Cat(Mammals):
    def __init__(self, gender, age, weight, name, desire_to_catch_mice):
        super().__init__(gender, age, weight)
        self.name = name
        self.desire_to_catch_mice = desire_to_catch_mice

    def say_name(self):
        print(f"Meow! I'm {self.name}. I'm {self.age} years old.")
        if self.desire_to_catch_mice == 'No':
            print("I hate catching mice! I'd rather sleep...")

Moon = Cat('female', 3, 4, 'Moon', 'No')
Moon.say_name()
Moon.say_weight()
print()


class Dog(Mammals):
    def __init__(self, gender, age, weight, name, number_of_commands_studied):
        super().__init__(gender, age, weight)
        self.name = name
        self.number_of_commands_studied = number_of_commands_studied

    def say_name(self):
        print(f"Woof! I'm {self.name}. I'm {self.age} years old. \n"
              f"I know {self.number_of_commands_studied} teams!")

Rocks = Dog('male', 11, 15, 'Rocks', 10)
Rocks.say_name()
Rocks.say_weight()
print()


'''№2 Class “Student”
Написать класс “Student”, который наследует класс human,
у которого среди прочих признаков есть “Количество сданных дз”.
'''
print('\n№2 Class “Student” \n')
class Student(Human):
    def __init__(self, gender, age, weight, name, _pasport,
                 course, number_of_homework_handed_over):
        super().__init__(gender, age, weight, name, _pasport)
        self.course = course
        self.number_of_homework_handed_over = number_of_homework_handed_over
    
    def courses(self):
        print(f'My course {self.course}')
    
    def homework(self):
        if self.number_of_homework_handed_over > 0:
            print(f'{self.number_of_homework_handed_over} homework completed')
        else:
            print('What...? What housework?')
    
    def __gt__(self, other):
        return self.number_of_homework_handed_over > other.number_of_homework_handed_over

    def __lt__(self, other):
        return self.number_of_homework_handed_over < other.number_of_homework_handed_over

    def __eq__(self, other):
        return self.number_of_homework_handed_over == other.number_of_homework_handed_over

    def __ne__(self, other):
        return self.number_of_homework_handed_over != other.number_of_homework_handed_over

Zhenya = Student('male', 19, 65, 'Zhenya', 7817836406, 2, 7)
Zhenya.say("Hello, I'm Zhenya!")
Zhenya.say_weight()
Zhenya.data()
Zhenya.courses()
Zhenya.homework()
print()

Masha = Student('female', 22, 57, 'Masha', 7819465871, 4, 0)
Masha.say("Hi! I'm Masha!")
Masha.say_weight()
Masha.data()
Masha.courses()
Masha.homework()
print()


'''№3 Comparison of students on homework
Перегрузить операторы сравнения так, чтобы студенты сравнивались
по количеству сданных ими дз.
''' 
print('\n№3 Comparison of students on homework: \n')
print(f"Zhenya's HW is more than Masha's HW:                {Zhenya > Masha}\n"
      f"Zhenya's HW is less than Masha's HW:                {Zhenya < Masha}\n"
      f"The number of HW of Zhenya and Masha is equal:      {Zhenya == Masha}\n"
      f"The number of HW of Zhenya and Masha isn't equal:   {Zhenya != Masha}\n")