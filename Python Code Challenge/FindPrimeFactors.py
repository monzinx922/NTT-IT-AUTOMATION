def is_prime(number):
    for i in range(2,number):
        if(number%i) == 0:
            return False
    return True

def prime_list(number):
    list = []
    for i in range(2,number+1):
        if is_prime(i):
            list.append(i)
    return list

def get_prime_factors(number):
    p_list = prime_list(number)
    ans_list = []
    for i in p_list:
        while(number%i == 0):
            ans_list.append(i)
            number = number/i

    return ans_list

print(get_prime_factors(630))

