# def star(n):
#     strin = "*"
#     print(strin * (n))

# print("1번 문제")
    
# for i in range(6):
#     star(6-i)
    
# print("2번 문제")

# for i in range(6):
#     star(i+1)
    
# print("3번 문제")

# for i in range(6):
#     capt = " "
#     print(capt * (6-i), end = "")
#     star(2*i+1)
    
    
# print("4번 문제")

# for i in range(6):
#     capt = " "
#     print(capt * (6-i), end = "")
#     star(2*i+1)

# for i in range(6):
#     capt = " "
#     print(capt * (i+1), end = "")
#     star(2*(6-i)-1)
    
t = 0
slist = []    

# for i in range(5):
#     for j in range(5):
#         t += 1
#         slist.append(t)
#     print(slist)
#     slist = []
    

# for i in range(1, 6):
#     for j in range(1, 6):
#         t = ((j-1)*5) + i
#         slist.append(t)
#     print(slist)
#     slist = []    
    
    
num = 26

for i in range(5):
    for j in range(5):
        num -= 1
        slist.append(num)
    print(slist)
    slist = []