# import random
# def encrypt(message):
#     message=list(message)
#     message.append(message[0])
#     message.pop(0)
#     rd='qwertyuiopasdfghjklzxcvbnmSm'
#     for i in range(3):
#         message.append(random.choice(rd))
#         message.insert(0,random.choice(rd))
#     return str(''.join(message))  
# def decrypt(message):
#     message=list(message)
#     for i in range(3):
#         message.pop(0)
#         message.pop(len(message)-1)
#     message.insert(0,message[len(message)-1])
#     del message[len(message)-1]
#     return str(''.join(message))

# word=input("enter the message\n")
# while(True):
#     try:
#         func=int(input('Enter which function to perform\n1 for encrypt\n2 for decrypt\n'))
#         if(not(func in [1,2])):
#             raise Error()
#         break
#     except:
#         print("\tENTER VAILD NUMBER\n")
# if func==1:
#     f_word=encrypt(word)
# else:
#     f_word=decrypt(word)
# print(f_word)
a=[0,1,2,3,4,5]
a.pop(1)
print(a)