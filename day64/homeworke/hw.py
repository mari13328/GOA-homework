
def greet(name):

    return ("hello" , name ) 

print(greet("Mari"))
print(greet("Seso"))
print(greet("Ana"))

                                                    

def numbers(num1 , num2):

    return (num1 + num2)

print(numbers(5 , 3))
print(numbers(15 , 25))
print(numbers(-2 , -4))

                                                    

def box(num):

    return (num * num)

print(box(4))
print(box(7))
print(box(10))

                                                    


def check_age(age):

    if age >= 18:
        return "სრულწლოვანი ხარ"
    else:
        return "არ ხარ სრულწლოვანი"


print(check_age(19))
print(check_age(18))
print(check_age(16))


                                                    

def text1(text):
    print(len(text))

text1("hello")
text1("hi")
text1("ola")



                                                    

def multiplay(num3 , num4):

    return ( num3 * num4)

print(multiplay(3 , 4))
print(multiplay(5 , 10))
print(multiplay(9 , 13))

                                                    


def check_even():

    number = 7
    if number % 2 == 0:
        return "this number is even"
    else:
        return "this number is odd"


print(check_even())

