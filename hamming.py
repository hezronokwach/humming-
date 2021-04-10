def hamming(x,y):
    str1=str(f'{x:08b}')#convert to binary then cast to string
    str2=str(f'{y:08b}')#convert to binary then cast to string
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1#increment counter if corresponding bits don't match
    return count


if __name__ == '__main__':
    num1=int(input("first number:\n"))
    num2=int(input("second number:\n"))
    print("\nthe hamming distance is:\n",hamming(num1,num2))



