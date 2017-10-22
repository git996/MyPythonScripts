
#import _pickle as pickle
#from collections import Counter
#import keras
#import postprocessing


def main():
    keyword = input("Enter Key: ")

    read_file('relativity.txt', keyword)


def read_file(fileName, key):

    f = open(fileName,'r')
    content = f.read()

    content = content.split()

    #s = parsed_content.find(key)
    #print(content.index('to'))
    n = False
    counter = 0
    result = []
    for index,x in enumerate(content):

        if(x == key):
            counter += 1
            print(*content[index-8:index+8], sep = ' ')
            result.append(content[index-8:index+8])
            n = True


    if  n == False:
       print("No key found")
       main()
    if  n == True: print(str(counter)+' '+"instances found"), main()





    input()




if __name__ == "__main__":
    # execute only if run as a script
    main()
