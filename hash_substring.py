# python3

def read_input():
       # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    print("F vai I")
    fi = input()
    
    if "F" in fi :
        fails =input()
        
        path = './tests/' + fails
        with open(path, 'r') as testfile:
            text = testfile.readline().rstrip()
            pattern = testfile.readline().rstrip()
            return text, pattern
                

   
    
    elif "I" in fi :
        # input from keyboard
        text = input().rstrip()
        pattern = input().rstrip()
        return text, pattern
        
    else:
        print("error")
        return
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    # return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    # prime = 31
    # m = 5*10**5
    
    m = len(pattern)
    n = len(text)

    # izrekina cik vienibas bus vajadzigas
    burti = [1]
    for i in range (1, max(n)):
        burti.append(burti[i-1])

    # iedod burtiem karp vertibas
    karp= [0]*(n+1)
    for i in range(n):
        karp[i+1] = (karp[i] + (ord(text[i])- ord('a')+1)*10**(n-i-1)

    kpattern = 0
    for in in range(m):
        kpattern = (kpattern + (ord(pattern[i])- ord('a')+1)*10**(n-i-1)

    output = []
    for i in range (n-m+1):
        rezult= (karp[i+m] - karp[i] +m)
        if rezult == kpattern:
            if text [i:i+m] = karp:
                output.append.(i)
        







    # and return an iterable variable
    
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

