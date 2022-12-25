import textwrap

def wrap(string, max_width):
    textwrapper = textwrap.TextWrapper(width=max_width)
    text_list = textwrapper.fill(text=string)
    
    return text_list
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
