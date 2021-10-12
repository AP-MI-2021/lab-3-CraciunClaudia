from typing import List


def read_list() -> List[int]:
    lst = []
    lst_str = input('Dati numerele separate prin spatiu:')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def is_even(n):
    '''
    Determina daca numarul dat este par.
    :param n:Numarul dat
    :return:Daca este par returneaza True si daca nu este returneaza False
    '''
    if n % 2 == 0:
        return True
    return False

def test_is_even():
    assert is_even(1) == False
    assert is_even(2) == True
    assert is_even(10) == True
    assert is_even (9) == False

def get_even(lst):
    '''
    Determina daca toate numerele sunt pare
    :param lst: Lista de numere
    :return: O lista cu numere pare
    '''
    result = []
    for num in lst:
        if is_even(num):
            result.append(num)
    return result

def get_longest_all_even(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa a unei liste cu proprietatea ca toate numerele sunt pare
    :param lst: Lista in care se cauta subsecventa
    :return:subsecventa gasita
    '''
    nr= len(lst)
    result = []
    for st in range(nr):
        for dr in range(st , nr):
            all_even = True
            for num in lst [st:dr+1]:
                if num % 2 !=0:
                    all_even=False
                    break
            if all_even :
                if dr - st + 1 > len(result):
                    result = lst[st:dr+1]
    return result

def is_prime_digits(n):
    '''
    Determina daca toate cifrele numarului sunt prime
    :param n: Numarul dat
    :return: True daca toate cifrele sunt prime sau False daca nu sunt toate prime
    '''

    while(n):
        if n % 10 == 1 :
            return False
        if n % 10 == 0 :
            return False
        if n % 10 == 4 :
            return False

        if n % 10 == 6 :
            return False
        if n % 10 == 8 :
            return False
        if  n % 10 ==9 :
            return False
        n = n / 10

    return True

def get_digits(lst):
    result = []
    for num in lst:
        if is_prime_digits(num):
            result.append(num)
    return result
def test_is_prime_digits():
    assert is_prime_digits(172) == False
    assert is_prime_digits(272) == True
    assert is_prime_digits(333) == True
    assert is_prime_digits(499) == False

def get_longest_prime_digits(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele sunt formate din cifre prime
    :param lst: Lista de numere
    :return: Subsecventa gasita
    '''
    nr = len(lst)
    result = []
    for st in range (nr):
        for dr in range (st , nr):
            all_prime_digits = True
            for num in lst [st:dr+1]:
                if  is_prime_digits(num) == False :
                    all_prime_digits = False
                    break
                if is_prime_digits(num) == True:
                    if dr - st + 1 > len(result):
                        result = lst[st:dr + 1]
    return result






def main():
    lst = []
    while True:
        print("1. Citire lista")
        print("2. Determinare cea mai lunga subsecventa cu proprietatea:Toate numerele sunt pare")
        print("3. Determinare cea mai lunga subsecventa cu proprietatea:Toate numere sunt formate din cifre prime")
        print("4.x. Exit")
        optiune = input ('Alege optiunea: ')
        if optiune == "1" :
            lst = read_list()
        elif optiune == "2":

            print(get_longest_all_even(lst))

        elif optiune == "3":
            print(get_longest_prime_digits(lst))
        elif optiune == "4":
            break
        else:
            print("Optiune invalida")

if __name__ == '__main__' :
    test_is_even()
    main()