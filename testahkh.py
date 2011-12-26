from ctypes import * 
import ctypes
import time
import os, sys
script = '''                    
#persistent                 
return                      
                            
filter(report, regex){             
 ; listvars                    
 ; msgbox % regex               
if pos := RegExMatch(report, regex)
return 1                           
else                               
return 0                           
}                                  
'''                                                                                              
                                                                                                 
ahk = cdll.ahka                                                                                  
scripta = create_string_buffer(script)                                                           
ahk.ahktextdll(scripta, "", "")                                                                  
 # time.sleep(1)                                                                                    
def _evaluate(obj):     
    casted = ctypes.cast(obj, ctypes.c_char_p)
    value = casted.value
    return value.decode()
  
hr1 = ahk.ahkFunction("filter", create_string_buffer("hello world"), create_string_buffer("hellos"))    
hr2 =  ahk.ahkFunction("filter", create_string_buffer("hello world"), create_string_buffer("hello"))
print _evaluate(hr1)
print _evaluate(hr2)                                                      
           
           
           
