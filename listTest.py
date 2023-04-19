#The following are just reading from text files and generating list
with open('breakfast.txt','r') as BL:
    BFlist = [line.strip() for line in BL.readlines()]
#print(BFlist)

with open('lunch.txt','r') as LL:
    lunchList = [line.strip() for line in LL.readlines()]
#print(lunchList)

with open('dinner.txt','r') as DL:
    dinnerList = [line.strip() for line in DL.readlines()]
#print(dinnerList)


#Below I am creating 3 dictonaries.
with open('ingredients.txt','r') as IL:
    ing_dict={}
    for line in IL:
        key, value = line.strip().split(':')
        ing_dict[key] = value
       
with open('instructions.txt','r') as I:
    ins_dict={}
    for line in I:
        key, value = line.strip().split(':')
        ins_dict[key] = value


with open('yield.txt','r') as Y:
    yield_dict={}
    for line in Y:
        key, value = line.strip().split(':')
        yield_dict[key] = value

#below is just a place holder.
again=0
while again == 0:

    print("What do you want? Breakfast, Lunch, or Dinner")
    meal=int(input("Type 1 for Breakfast, 2 for Lunch, or 3 for Dinner\n"))
    if meal == 1:
        print("Which breakfast item would you like?")
        for i in BFlist:
            print(i)
        choice=input("Which meal do you want?\n")
        prep=choice
    elif meal == 2:
        print("Which lunch item would you like?")
        for i in lunchList:
            print(i)
        choice=input("Which meal do you want?\n")
        prep=choice
    elif meal == 3:
        print("Which dinner item would you like?")
        for i in dinnerList:
            print(i)
        choice=input("Which meal do you want?\n")
        prep=choice
    else:
        print("incorrect input")
    
    print(ing_dict[prep])
    print(ins_dict[prep])
    print(yield_dict[prep])

    more=input("Would you like another meal?\n")
    if more == 'n':
        again=1