def perfect_num(n):
    sum = 0
    for i in range(1,n):
        if n%i==0:
            sum += i
 
    if (sum == n):
        return ("It is a perfect number")
    else:
        return  ("It is not a perfect number")

#int main()
n=int(input("enter the number"))
print(perfect_num(n)) 