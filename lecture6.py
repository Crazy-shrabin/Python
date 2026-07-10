# cities = ["ktm", "pkr", "ctwn", "brtn", "illam"]
# famous = ["temple","nature", "market", "deal", "teas"]


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


def show (n):
    if (n == 0):
        return
    print(n)
    show(n - 1)

show(55)