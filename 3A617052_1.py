def diamond(n):
    for i in range(n+1):
        print(" "*(n-i)+"*"*(2*i-1))
    for i in range(n-1,0,-1):
        print(" "*(n-i)+"*"*(2*i-1))
        
a = int(input("Please enter the number of stars u want: "))
diamond(a)