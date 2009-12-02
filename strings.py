import re 

def stringtrimright(string, trimsize): 
    return string[:-trimsize]

def stringtrimleft(string, trimsize): 
    return string[trimsize:]


def strlen(string):
    return len(string)


def stringsplit(s, separator):
    return s.split(separator)

def regexmatch(haystack, needle):
#    return re.match("(" + needle + ")", haystack)
    return re.search(needle, haystack)

if __name__ == "__main__":
    print stringtrimright("hello", 2)
    print stringtrimleft("hello", 2)
    print strlen("hello")
    print stringsplit("hello", "e")
    print regexmatch("  #hello #there", "\s*(#\w+)\s")




