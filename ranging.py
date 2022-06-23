#print a dictionary with keys from o to 15 and values are squares of keys
#create a variable holding the new dictionary
#create a counter variable that'll represent the index 
#loop through the new dictionary
#Each variable in p assign it a value of squared each value.
from itertools import zip_longest


def somey():
    z=range(0,15) 
    for i in z:
        p=dict.fromkeys(z)
    # print(p) 
                     #loop through the values and square the values 
    for i in p:
        p[i]=i*i
        # for v in p.values():
            # v*=v
    print(p)



somey()
#create a list of the range 
#using list comprehension,make a list of items in list i squared
#using zip function,make a dictoinary out of them ,1st list,keys second values
#end function
def trying():
    z=range(0,15)
    put1=list(z)
    list3=[i*i for i in put1]
    zipping=zip_longest(put1,list3)
    print(dict(zipping))
trying()