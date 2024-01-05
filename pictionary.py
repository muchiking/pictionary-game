import random 
from names import *


num_= {}

num_[1]=0
num_[2]= 0 
num_[3]=0
num_[4]=0 
num_[5]= 0



while(True):

    # print(random.randrange)
    
    rand = random.randrange(1,6)

    print(rand)

    if rand == 1:
        print(objects[(num_[1])])
        num_[1] = num_[1] +1
    elif  rand==2:
        print(action_verbs[(num_[2])])
        num_[2]=num_[2]+1
    elif  rand==3:
        print(places[(num_[3])])
        num_[3]=num_[3]+1
    elif  rand==4:
        print(african_animals[(num_[4])])
        num_[4]=num_[4]+1
    elif  rand==5:
        print(random_[(num_[5])])
        (num_[5])=num_[5]+1

    print("\n")



    

    input()



