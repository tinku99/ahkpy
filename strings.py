def stringtrimright(string, trimsize): 
    return string[:-trimsize]

print stringtrimright("hello", 2)


def stringtrimleft(string, trimsize): 
    return string[trimsize:]

print stringtrimleft("hello", 2)

def strlen(string):
    return len(string)

print strlen("hello")
