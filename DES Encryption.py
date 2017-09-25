
import numpy
#for i in range (0, 16):
#    print (bin(i))
#input()
list1 = []

#while (len(list1) < 64):
  #  x = input('256 bit dictrionary. Enter a number: ')
 #   list1.append(x)
   # print(list1)
  #  print(len(list1))
with open("C:/Users/New/Dropbox/Semester 2 2017/Computer Network Security/pc2.txt") as vall:
    listpc2 = vall.read().split("', '")
    print(listpc2)
    print(len(listpc2))

k1 = []
f2 = open("C:/Users/New/Dropbox/Semester 2 2017/Computer Network Security/k1.txt","w+")
def num():
    
    

    
    
    x1 = input ('Input a number to find its binary value')
    x1 = int(x1)
    print(listpc2[x1-1])
    k1.append(listpc2[x1-1])
    f2.write( '\nk1: '+str(len(k1)) + ': ' + str(k1))
    
    
  
    
    num()

num()



def readlist():
    
    c0 = []
    c1 = []
    d0 = []
    d1 = []
    pc2 =  []

    with open('C:/Users/New/Dropbox/Semester 2 2017/Computer Network Security/new pc1.txt') as f:
        bits = f.read().split('\n\n')
        
    print(bits)
    print (len(bits))
    f1 = open("C:/Users/New/Dropbox/Semester 2 2017/Computer Network Security/pc1fixed.txt","w+")
    f1.write( '\npc1: '+str(len(bits)) + ': ' + str(bits))
    
    for i in range(0,28): # print value form 0 to 27 index
        c0.append(bits[i])
        #with open('C:/Users/New/Dropbox/Semester 2 2017/Computer Network Security/new pc1C0.txt') as f:
        #print("C0", bits[i] )
    f2 = open("C:/Users/New/Dropbox/Semester 2 2017/Computer Network Security/pc1fixed.txt","a")
    f2.write( '\nc0: '+str(len(c0)) + ': ' + str(c0))
    print('c0: ', len(c0),  c0)

    c1 = list(numpy.roll(c0, -1))
    print(c1)
    f2.write( '\nc1: '+str(len(c1)) + ': ' + str(c1))

    for i in range(28,56): # print value form 28 to 56 index
        d0.append(bits[i])
        #with open('C:/Users/New/Dropbox/Semester 2 2017/Computer Network Security/new pc1D0.txt') as f:
    f2.write( '\nd0: '+str(len(d0)) + ': ' + str(d0))
    print('d0:',len(d0), d0)
    d1 = list(numpy.roll(d0, -1))
    f2.write( '\nd1: '+str(len(d1)) + ': ' + str(d1))

    c1d1 = c1 + d1
    f2.write( '\nc1d1: '+str(len(c1d1)) + ': ' + str(c1d1))
    
    


    
   
   
    print(d1)
    f1.close()
    f2.close()


    
    
    

    #calculate c1 and d1

        

    


    
#readlist()
#test()