'''
1
input number from the user --  88949
print the number in reverse -- 94988
print the biggest digit -- 9
print how many times the biggest digit appears? -- 2
print the min digit -- 4
print the sum of digits -- 38
print the avg of digits -- 8+8+9+4+9 / 5
'''

number = input("Please enter a number: ")

print(number[::-1])
print(max(number))
print(number.count(max(number)))
print(min(number))
list1 = []
for i in number:
    list1.append(int(i))
print(sum(list1))
print(sum(list1) / len(list1))

"""
2
write a function that gets a list of numbers and returns if the list is sorted or not
"""

def is_list_sorte(list3: list) -> bool:
    if list3 == sorted(list3):
        return True
    else:
        return False

list2 = [1,2,3,5,6,7,8,9]
list3 = [6,8,3,7,9]
print(is_list_sorte(list3))

"""
3
write a function that gets a list of numbers (with duplication), n-th biggest and returns it
i.e. [88, 100, 90, 95, 95, 97, 97, 99, 97, 99] , 4 -->
will return 95 (because it is the 4-th biggest after 100, 99, 97, 95)
"""

def is_n_biggest(list_of_numbers: list, n: int) -> bool:
    """
    :param list list_of_numbers: list of numbers
    :param int n: ranked number
    return: the - n-th biggest number
    """
    while n > 0:
        no_double_numb = []
        for number in list_of_numbers:
            if number in no_double_numb:
                continue
            else:
                no_double_numb.append(number)
        if n > len(no_double_numb):
            return f'n-th biggest number is: {max(no_double_numb)}'
        sorted_list = sorted(no_double_numb)
        return sorted_list[-n]

number = input("Please enter a number: ")
while not number.isdigit():
    number = input("Please enter a number: ")
n = int(number)
list_of_numbers = [88, 100, 90, 95, 95, 97, 97, 99, 97, 99]
print(is_n_biggest(list_of_numbers, n))




