cities = ["ktm", "pkr", "ctwn", "brtn", "illam"]
famous = ["temple","nature", "market", "deal", "teas"]


# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")



# print_len(cities)
# print_len(famous)

# print (famous)

# print_list(famous)


# def cal_fact(n):
#     fact = 1
#     for i in range (1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(7)


# def converter (usd_val):
#     npr_val = usd_val * 150
#     print(usd_val, "USD=", npr_val, "NPR")

# converter(15)

# recusive function
# def show (n):
#     if (n == 0):
#         return
#     print(n)
#     show(n - 1)

# show(55)

def calc_sum(a, b):
    return a + b
def print_hello ():
    print("hello")
def calc_avg(a, b, c):
    sum = a + b + c
    div = sum/3
    print(div)
    return div
def len_cities(list):
    print(len(list))
def single_line(list):
    print(list)
    return list
def print_list(list):
    for item in list:
        print(item, end = " ")
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)        






def usd_to_npr(n):
    a = 153.82 * n
    print("The total money conversion amount is: ", a) 

usd_to_npr(20)