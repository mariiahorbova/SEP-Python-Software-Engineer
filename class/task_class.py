# 1. Write a Python class named Circle constructed by a radius and two methods
# which will compute the area and the perimeter of a circle.
class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return round(self.radius**2 * 3.14, 3)

    def perimeter(self):
        return round(self.radius * 2 * 3.14, 3)


print("\nClass circle")
some_circle = Circle(10)
print(some_circle.area())
print(some_circle.perimeter())


# 2. Write a Python class named Rectangle constructed by a length and width
# and a method which will compute the area of a rectangle.
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return round(self.length * self.width, 3)


print("\nClass rectangle")
some_rectangle = Rectangle(10.12, 5.20)
print(some_rectangle.area())


# 3. Write a Python class to reverse a string word by word.
class Reverse:
    def __init__(self, w):
        self.word = w

    def reverse(self):
        return " ".join(reversed(self.word.split()))


print("\nClass reverse string word by word")
some_string = Reverse("word by word using split")
print(some_string.reverse())


# 4. Write a Python class to implement pow(x, n).
class Pow:
    def power(self, x, n):
        if x == 0 or x == 1 or n == 1:
            return x

        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.power(x, -n)
        value = self.power(x, n // 2)
        if n % 2 == 0:
            return value * value
        return value * value * x


print("\nClass to implement pow")
some_pow = Pow()
print(some_pow.power(14, 7))
some_pow = Pow()
print(some_pow.power(34, -2))
some_pow = Pow()
print(some_pow.power(1, 0))


# 5. Write a Python class to find validity of a string of parentheses,
# '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
class Patentheses:
    def parentheses(self, string):
        stack, parentheses_chars = [], {"(": ")", "{": "}", "[": "]"}
        for p in string:
            if p in parentheses_chars:
                stack.append(p)
            elif len(stack) == 0 or parentheses_chars[stack.pop()] != p:
                return False
        return len(stack) == 0


print("\nValidity of parentheses")
print(Patentheses().parentheses("()[]"))
print(Patentheses().parentheses("()[{}"))
print(Patentheses().parentheses("(}"))


# 6. Define a class called Lunch.Its __init__() method should have two arguments:
# self and menu.Where menu is a string. Add a method called menu_price.It will involve a if statement:
# if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:",
# menu, "Price 13.40", else print "Error in menu".
# To check if it works define: Paul = Lunch("menu 1") and call Paul.menu_price().
class Lunch:
    def __init__(self, menu: str):
        self.menu = menu

    def menu_price(self):
        if self.menu == "menu 1":
            print("Your choice: " + self.menu + " Price 12.00")
        elif self.menu == "menu 2":
            print("Your choice: " + self.menu + " Price 13.40")
        else:
            print("Error in menu")


print("\nChecking Lunch")
Paul = Lunch("menu 1")
Paul.menu_price()
Laura = Lunch("menu 2")
Laura.menu_price()
John = Lunch("menu 0")
John.menu_price()


# 7. Define a Point3D class that inherits from object Inside the Point3D class,
# define an __init__() function that accepts self, x, y, and z,
# and assigns these numbers to the member variables self.x, self.y, self.z.
# Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z).
# This tells Python to represent this object in the following format: (x, y, z).
# Outside the class definition, create a variable named my_point containing
# a new instance of Point3D with x = 1, y = 2, and z = 3. Finally, print my_point.
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


print("\nClass Point3D inherits from an object")
my_point = Point3D(1, 2, 3)
print(my_point)


# 8. Define a class called Songs, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics.lyricsis a list.
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
# Define a variable:
# happy_bday = Song(["May god bless you, ",
#                     "Have a sunshine on you,",
#                     "Happy Birthday to you !"])
# Call the sing_me_songmehod on this variable.
class Songs:
    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for el in self.lyrics:
            print(el)


print("\nClass Sing")
happy_bday = Songs(
    ["May god bless you, ", "Have a sunshine on you,", "Happy Birthday to you !"]
)
happy_bday.sing_me_a_song()
