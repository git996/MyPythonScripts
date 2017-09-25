# project euler attempts-Sushant

def main():
    #problem_1()
    #problem_2()
    #problem_3(87)
    problem_4()


def problem_1():
    MultipleLimit = 1000
    Num1 = 3
    Num2 = 5
    Sum = 0
    for x in range(1,MultipleLimit):
        if (x%Num1 == 0 or x%Num2 ==0):
            Sum = Sum + x
    print(Sum)

def problem_2():
    FibLimit = 10;
    Start = [1,2]
    Series = [1,2]
    Sum = Start[1]
    while (Start[1] < 4000000):
        precalc = Start[1]
        Start[1] = Sum + Start[0]
        Start[0] = precalc
        Sum = Start[1]
        if (Sum < 4000000):
            if (Sum%2 ==0):
                Series.append(Sum)
    print('Sum of Even Numbers: ', (sum(Series)-1))

#problem 3 - prime factor calculator
def problem_3(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    print(factors)

#problem 4 - largest palindrome from product of two 3-digit numbers
def problem_4():
    num = 9998
    n  = num - 1
    while (n < num):
        reversed_n = list(reversed(str(n)))
        #print(n)
        factors = []
        if(list(str(n)) == reversed_n):
            
            
            x  = 99
            print(n)
            print('Yes')
            while (x < 1000):
                if(num%x == 0):
                    
                    factors.append(x) 
                    #print(factors.pop
                    #print(factors.pop())
                x += 1
        if (len(factors) > 1):
            print(factors)
        break
        
    
        n -= 1
    










































if __name__ == "__main__":
    # execute only if run as a script
    main()
