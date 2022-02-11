'''
import math
name = input("what is your name?",)
print("hello", name, "its nice to meet you")
mile = int(input("how many miles did you drive to get here?"))
kilometers = mile*1.6
print("you mean", kilometers, "kilometers? its great")
ages = int(input("and how old are you again?"))
print("alright, you are", ages, "\b. its great")

num_1, num_2 = input("please enter 2 digits with a space in between and all tell you what is going on").split()
num_2 = int (num_2)
num_1 = int (num_1)
sum_1 = num_2+num_1
print("sum of {} and {} is equal to {}".format(num_1, num_2, sum_1))
print("sinus first one is", math.sin(num_1), "and the second one is:", math.sin(num_2))
print("square roots are",math.sqrt(num_1),math.sqrt(num_2) )
'''

'''
# calculator
adad1, oon, adad2 = input("please do the math").format()
adad1 = int(adad1)
adad2 = int(adad2)
if oon == "*":
    res1 = adad1*adad2
    print("the result is:", res1 )
elif oon == "+":
    res1 = adad1+adad2
    print("the result is:", res1)
elif oon == "-":
    res1 = adad1-adad2
    print("the result is:", res1)
elif oon == "/":
    res1 = adad1/adad2
    print("the result is:", res1)
else: print("i dont know what do you mean?")
'''

'''
#choosing grades
age1 = int(input("please type your age:"))
if age1 == 5:
    print("go to kindergarten")
elif (age1 >=6) and (age1<=17):
    print("go to grade:", age1-5)
elif age1 > 17:
    print("go to collage")
else: print("wrong answer")
'''

'''
#vote
age = int(input("how old are you?"))
can_vote = True if age >= 18 else False
print("you can vote: ", can_vote)
'''

'''
#calculate investment
investment = int(input("how much money do you want to invest:"))
soodrate = int(input("how much is the interest:"))
years = int(input("how many years do you want to keep your money in:"))
pool = investment + (investment*soodrate/100)
for i in range(years):
    print("after", i+1, "years you gonna have", pool)
    pool = pool + (pool*soodrate/100)
'''

'''
#palm tree
tall = int(input("how tall do you like your tree:"))
i=1
n=0
hashtag = str("#")
spaces = str(" ")
while True:
    if (i % 2 != 0):
        x=tall-n
        print(spaces*x ,hashtag*i)
        n += 1
        i += 1
    elif n == tall:
        break
    else: i += 1
print(spaces*tall, hashtag)
'''

'''
# Error escape
while True:
    try:
        voroodi = int(input("please enter a number:"))
        break
    except ValueError:
        print("please just enter a number")
    except:
        print("there is something wrong, please enter a number again")
print("good job")
'''

'''
#guess a number
secret_num = 7
while True:
    num_guess = int(input("please guess a number between 1-10:"))
    if num_guess == secret_num:
        print("congrats, that's the one")
        break
    else:
        print("try again")
        continue
'''

'''
#code your name
out_str = input("write a word to code (all caps):")
tool1 = len(out_str)
coded_str = ''
decode_str = ''
for i in range(tool1):
    coded_str += str(ord(out_str[i])-23)
print(coded_str)
tool2 = len(coded_str)
for j in range(0,tool2,2):
    s2 = chr(int(coded_str[j:j+2])+23)
    decode_str += s2
print("decode is",decode_str)
'''

'''
#sentences to acronym
acr3 = ''
pc2acr = input("please write something to get the acronym:")
acr1 = pc2acr.split()
toolpc = len(acr1)
for i in range(0,toolpc):
    acr2 = acr1[i]
    acr3 += acr2[0]
print(acr3.upper())
'''

'''
#shifter code (not exactrly true)
orig1 = input('write a sentence to code')
redishift = int(input('write number:'))
redi2 = ''
for i in range(0, len(orig1)):
    redi1 = ord(orig1[i]) + redishift
    redi2 += chr(redi1)
print(redi2)

redi3 = str(redi2)
redi6 = ''
for j in range(0, len(orig1)):
    redi4 = redi3[j]
    redi5 = ord(redi4) - redishift
    redi6 += chr(redi5)
print(redi6)
'''

'''
#equation solver
def my_eq1(eq_2):
    unknown, oon, num_1, equals, mun_2 = eq_2.split()
    print(unknown, oon, num_1, equals, mun_2)
    num_1 = int(num_1)
    num_2 = int(mun_2)
    if oon == '-':
        x_1 = num_1 + num_2
    elif oon == '+':
        x_1 = num_2 - num_1
    elif oon == '*':
        x_1 = num_2/num_1
    else: print('i dont know what it is')
    return x_1

print(my_eq1('x * 5 = 10'))
'''

'''
#prime Nubmers
def prime_mumber(numb):
    for i in range(2,numb):
        if (numb % i) == 0:
            return False
    return True
def list_adder(enqad):
    num_cont = []
    for i in range(2,enqad):
        if prime_mumber(i):
            num_cont.append(i)
    return num_cont

print(list_adder(int(input("please enter a number:"))))
'''

'''
import random
randomlist = []
for i in range(0,5):
    n = random.randint(1,10)
    randomlist.append(n)
print(randomlist)
'''

'''
multidim = [[0] * 10 for i in range(10)]
for i in range(1, 10):
    for j in range(1, 10):
        multidim[i][j] = i*j


for i in range(1, 10):
    for j in range(1, 10):
        print(multidim[i][j], end=", ")
    print()
'''

'''
import os
with open("my_text.txt", mode="w", encoding="utf-8") as my_file:
    my_file.write("some random text\nsome more")

with open("my_text.txt", encoding="utf-8") as my_file:
    print(my_file.read())

with open("my_text.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        print("line num: ", line_num)
        word_list = line.split()
        print("number of words: ", len(word_list))
        char_count = 0
        for word in word_list:
            for char in word:
                char_count += 1
        ave_num_chars = char_count/len(word_list)
        print("average word length: {:.2f}".format(ave_num_chars))
        line_num += 1
'''

'''
class Dog:
    def __init__(self, name="", ghad=0, vazn=0):
        self.name = name
        self.ghad = ghad
        self.vazn = vazn

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))

def main():
    spot = Dog("ashh", 10, 29)
    spot.eat()

main()
'''

'''
class Square:
    def __init__(self, height="0",width="0"):
        self.height = height
        self.width = width


    @property
    def height(self):
        print("Retrieving the height")
        return self.__height
    @height.setter
    def height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            print("please only enter a number for height")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("please only enter a number for width")

    def get_area(self):
        return int(self.__width) * int(self.__height)


def main():
    square = Square()
    height = input("enter Height:")
    width = input("enter width:")
    square.width = width
    square.height = height
    print("height", square.height)
    print("width", square.width)
    print("the area is = ", square.get_area())
main()
'''


import random
import math

class Warrior:
    def __init__(self, name="Warrior",health=0, attk_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attk_max = attk_max
        self.block_max = block_max

    def attack(self):
        attk_amt = self.attk_max * (random.random() + 0.5)
        return attk_amt
    def block(self):
        block_amt = self.block_max * (random.random() + 0.5)
        return block_amt

class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.get_attack_result(warrior1,warrior2) == "Game Over":
                break
            if self.get_attack_result(warrior2,warrior1) == "Game Over":
                break

    def get_attack_result(self, warriorA, warriorB):
        warrior_a_attack_amt = warriorA.attack()
        warrior_b_block_amt = warriorB.block()
        damage_2_warrior_b = math.ceil(warrior_a_attack_amt - warrior_b_block_amt)
        warriorB.health = warriorB.health - damage_2_warrior_b
        print("{} attacks {} and deal {} damage".format(warriorA.name, warriorB.name, damage_2_warrior_b))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "fight again"
def main():
    thor = Warrior("thor", 50, 20, 10)
    loki = Warrior("loki", 50, 20, 10)
    battle = Battle()
    battle.start_fight(loki,thor)

main()



