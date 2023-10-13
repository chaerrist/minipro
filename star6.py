# # def star(n):
# #     strin = "*"
# #     print(strin * (n))

# # print("1번 문제")
    
# # for i in range(6):
# #     star(6-i)
    
# # print("2번 문제")

# # for i in range(6):
# #     star(i+1)
    
# # print("3번 문제")

# # for i in range(6):
# #     capt = " "
# #     print(capt * (6-i), end = "")
# #     star(2*i+1)
    
    
# # print("4번 문제")

# # for i in range(6):
# #     capt = " "
# #     print(capt * (6-i), end = "")
# #     star(2*i+1)

# # for i in range(6):
# #     capt = " "
# #     print(capt * (i+1), end = "")
# #     star(2*(6-i)-1)
    
# # t = 0
# # slist = []    

# # # for i in range(5):
# # #     for j in range(5):
# # #         t += 1
# # #         slist.append(t)
# # #     print(slist)
# # #     slist = []
    

# # # for i in range(1, 6):
# # #     for j in range(1, 6):
# # #         t = ((j-1)*5) + i
# # #         slist.append(t)
# # #     print(slist)
# # #     slist = []    
    
    
# # num = 26

# # for i in range(5):
# #     for j in range(5):
# #         num -= 1
# #         slist.append(num)
# #     print(slist)
# #     slist = []

# import random

# rcp = [1, 2, 3]
# rrccpp = ["가위", "바위", "보"]
# # 1 = 가위, 2 = 바위, 3 = 보

# def ran_rcp():
#     ant = random.choice(rcp)
#     return ant

# def determin_winner(ans):
#     comp = ran_rcp()
#     print(comp)
#     if comp == ans:
#         print("무승부")
#         return
#     elif (
#         (comp == 1 and ans == 3) or
#         (comp == 2 and ans == 1) or
#         (comp == 3 and ans == 2)
#     ):
#         print("졌습니다.")
#     elif (
#         (comp == 1 and ans == 2) or
#         (comp == 2 and ans == 3) or
#         (comp == 3 and ans == 1)
#     ):
#         print("이겼습니다.")
        
# for i in range(3):
#     print("%s는 %s"%(str(rcp[i]), rrccpp[i]))
    
# ans1 = int(input("1~3을 입력하시오 : "))
# determin_winner(ans1)

# f = open("temp.txt", "w")
# f.write("hello \n")
# f.write("world")
# f.close()

# f = open("C:\\study\\minipro\\temp.text", "w")
# for i in range(101):
#     f.write(str(i) + "\n")

# f.close()

# f = open("C:\\study\\minipro\\temp.text", "a")
# f.write("hello \n")
# f.write("world")

# f.close()

f = open("C:\\study\\minipro\\temp.text", "r")
# res = f.read()

# for i in range(110):
#     res = f.readline()
#     print(res)

# res = f.readlines()
# print(res)

# line = f.readlines()
# for l in line :
#     print(l)

for line in f :
    print(line)
    
f.close()