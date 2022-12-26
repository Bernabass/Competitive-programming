import textwrap

def wrap(string, max_width):
    count = 0
    paragraph = ""
    res = ""
    for idx , char in enumerate(string):
        count += 1
        paragraph += char 
        if count == max_width or idx == len(string) - 1 :
            res += paragraph + "\n"
            paragraph = ""
            count = 0   
    return res
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    