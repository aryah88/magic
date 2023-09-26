#!/usr/bin/env python
# coding: utf-8

# In[9]:


from random import shuffle
def shuffle_list (my_list):
    shuffle(my_list)
    return(my_list)




def players_guess():
    guess=''
    
    while guess not in['0','1','2']:
        guess=input("enter the number u think the ball is in either 0,1,2")
       
    return int(guess)




def check_guess(my_list,guess):
    if  my_list[guess]=='0':
        print("correct!")
    else :
        print('wrong!')
        print(my_list)
        
        

        
        
        
        
#initial guess
my_list=['','0','']

#shuffling the list
mixedlist=shuffle_list(my_list)

#players guess
guess=players_guess()

#checking the guess
check_guess(mixedlist,guess)


# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




