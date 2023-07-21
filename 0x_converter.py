import math
# input= 10000
# TODO: 1.make the programe run many times 
# 2.If the type of the input is unsupported,
# warn the user to input a number.

# print("Do you want to continue converting?(No/Yes): ")
# opt=0
bb=0
while True:
    # print("Please input any number:(if you want to quit,type q) ")
    bbb=input("Please input any number:(if you want to quit,type q) ")
    if bbb=="q":
        break
    try:
        bb=int(bbb)
    except ValueError:
        
        # else:
        print("Invalid input")
        bb=input("Please input any number:(if you want to quit,type q) ")
        # continue
    # if type(bbb) is str and !="q":
    #     print("You input a string,please input a number. ")
    #     bb=input()
    #     b=float(bb)
        
    # b=float(bb)
    b=float(bb)
    a=int(math.log2(b)/4)
    sum=0
    array=[]
    for i in range(0,10):
        y=int(b/(math.pow(16,a)))
        # print("y: ", y)
        m=sum+math.pow(16,a)*y
        b=b-m
        array.append(y)
        a=a-1
        if a<0:
            break
    print("Hex of the number is: ", array)
    # print("Do you want to continue converting?(No/Yes): ")
    # opt=input()
    # if opt=="No":
    #     break
    # if opt=="Yes":





# remainder=input
# for i in range(0,10):
#     next=int(remainder/16)
#     digit=remainder-next*16
#     remainder=next
#     array.append(digit)
#     if next==0:
#        break
# print(array)