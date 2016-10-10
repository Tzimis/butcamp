input_number=input("Enter the number of triangle numbers tha you want to print:")
input_number=int(input_number)
i=1
while(i<=input_number):
    sum = i*(i+1)/2
    print(int(sum), end=' ')
    i += 1
    
