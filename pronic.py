input_number=input("Enter the number of pronic numbers tha you want to print:")
input_number=int(input_number)
i=1
while(i<=input_number):
    p = i*(i+1)
    print(p, end=' ')
    i += 1
