result = [] #Set a list to store answer

N = int(input()) #Giving a integer to make the following loop to control the number of input.

'''
Using two Try-except function. First one, it will judge every input whether blank exists. 
If there is no blank, and then it will generate "Please type a number." to store in result list.
Second, code will try to multiply two integers. Generate string "Total amount: c" if the input accepted.
Or generate "You should type an integer." to store if the input is unable to multiply.
'''
for i in range (N):
    try:
        a,b = map(str,input().split(' '))
        try:
            c = str(int(a)*int(b))
            result = result + ['Total amount: ' + c]
        except ValueError :
            c = 'You should type an integer.'
            result = result + [c]
    except ValueError :
        c = 'Please type a number.'
        result = result + [c]
    
for j in result:
    print(j)
