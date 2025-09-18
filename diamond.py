def create_diamond(a):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for i in range(len(alphabet)):
        if alphabet[i] == a.lower():
            indexoriginal = i
    linesize = build_line_size(indexoriginal)
    while i <= len(alphabet[indexoriginal]):
        build_string(alphabet[i], linesize)
        i += 1


    build_string(a, linesize)

    return str(a)

def build_line_size(index):
    line = ""
    for i in range(index):
        line += " "
    return len(line)

def build_string(letter, stringsize):
    line = stringsize
    middleLine = int((len(line) / 2))
    for i in range(len(line)):
        if i == middleLine + 1:
            line += letter
        #elif i == middleLine - 1:
            #line += letter
        #else:
            #line += " "
    return line





