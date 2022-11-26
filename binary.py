conv = input("Please select the type of conversion you want to do(1-base 2 to base 10, 2-base 10 to base 2:\t")
while conv != '1' and conv != '2':
    conv = input("Please select the type of conversion you want to do(1-base 2 to base 10, 2-base 10 to base 2:\t")
 
valid = None
if conv == '1':
    binary = input("\nPlease put in a binary number to be converted:\t")
    for no in binary:
        try:
            if int(no) >= 2:
                valid = False
                break
        except:
            valid = False
            break        
    
    while valid == False:
        c = 0
        print("\nPlease put in a valid binary number")
        binary = input("Please put in a binary number to be converted:\t")
        for no in binary:
            try:
                if int(no) >= 2:
                    valid = False
                    break
                else:
                    c += 1
            except:
                valid = False
                break
        
        if c == len(binary):
            valid = True
            
    rank = []
    for ind, no in enumerate(binary):
        rank.append(no)
        rank.append(int((len(binary)-ind) -1))
    
    result = 0
    for ind, no in enumerate(rank):
        if ind == 0 or ind%2 == 0:
            result += int(int(no) * 2) ** int(rank[ind+1])
        else:
            continue
            
    print(result)
            
    
else:
    number = input("\nPlease put in a number to be converted to binary\n")
    while True:
        try:
            int(number)
            break
        except:
            print("\nPlease put in a valid integer")
            number = input("Please put in a number to be converted to binary\n")
    
    rem_list = []
    while int(number) >= 2:
        rem = int(number)%2
        number = int(number)//2
        rem_list.append(rem)
    rem_list.append(number)
    
    result = 0
    for t in range(len(rem_list)):
        if result == 0:
            result = f"{rem_list[-(t+1)]}"
        else:
            result = f"{result}{rem_list[-(t+1)]}"
            
    print(result)

