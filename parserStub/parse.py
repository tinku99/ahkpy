import os, re, sys
from fileread import *
from strings import *
filename = sys.argv[1]
file = open(filename)
lines = file.readlines()
script = fileread(filename)
scope = "global"
hotkey = ""
hotstring = ""
phrase = ""

def isDirective(line):
    global scope
    result = regexmatch(line, r'\s*(#\w+)\s(.*)')
    if result: 
        scope = result.group(2)
    return result    
def isHotkey(line):
    global hotkey, hotstring
    result = regexmatch(line, r'([+*^#!~]\w{1,3})::')
    if result: 
        hotkey = result.group(1)
        hotstring = ""
    return result    

def isHotstring(line):
    global hotkey, hotstring
    result = regexmatch(line, r'::(\w+?)::')
    if result: 
        hotstring = result.group(1)
        hotkey = ""
    return result    

for line in lines:
    if regexmatch(line, r'\w'): 
        if not isDirective(line):
            if not isHotkey(line):
                if not isHotstring(line):
                    print scope
                    print hotkey or hotstring
                    print line 


        
