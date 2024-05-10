from math import sqrt

storage_dictionary = {0 : 1, 1 : 1, 2 : 2, 3 : 3, 4 : 5, 5 : 7}

def new_meaning(number):
    if number in storage_dictionary:
        return storage_dictionary[number]
    else:
        sum = 0
        i = 1
        while (number - i) > 0:
            sum += ((-1)**(i + 1))*(new_meaning(number - i*(3*i - 1)/2) + new_meaning(number - i*(3*i + 1)/2))
            i += 1
        sum
        storage_dictionary[number] = sum
        return sum


print(new_meaning(100) - 1)
