# by Irh9 
# http://www.autohotkey.com/forum/author-lrh9.html
# http://www.autohotkey.com/forum/viewtopic.php?p=428795#428795 
import ctypes
import itertools
import os   
import sys  
            
ENCODING = 'utf-8'
            
DLL_TYPES = ("Win32a", "Win32w", "X64W")
DLL_NAMES = ("AutoHotkey.dll", "AutoHotkeyMini.dll")
  
if __name__ == '__main__':
    _path = sys.argv[0]
else:
    _path = __file__
  
_dir = os.path.dirname(os.path.abspath(_path))
  
DLL_PATHS = {}
for dir_, name in itertools.product(DLL_TYPES, DLL_NAMES):
    DLL_PATHS[os.path.join(dir_, name)] = os.path.join(_dir, dir_, name)
  
def set_library(dll_type, dll_name):
    global AHK
    AHK = ctypes.cdll.LoadLibrary(DLL_PATHS[os.path.join(dll_type, dll_name)])
  
set_library('Win32a', 'AutoHotkey.dll')
  
def _evaluate(obj):
    casted = ctypes.cast(obj, ctypes.c_char_p)
    value = casted.value
#    return eval(value.decode())  # not sure why we need eval here...
    return value.decode()  
  
def _represent(obj):
    return repr(obj).encode()
  
def run(file_path, options="", parameters=""):
    return AHK.ahkdll(file_path.encode(), options.encode(), parameters.encode())
  
def run_text(text="#Persistent\n#NoTrayIcon", options="", parameters=""):
    return AHK.ahktextdll(text.encode(), options.encode(), parameters.encode())

def ready():
    return bool(AHK.ahkReady())

def add(file_path, include_again=False, ignore_failure=0):
    return AHK.addFile(file_path.encode(), ctypes.c_uint8(include_again), ctypes.c_uint8(ignore_failure))

def add_text(text, execute=0):
    return AHK.addScript(text.encode(), ctypes.c_uint8(execute))

def execute_text(text):
    return AHK.ahkExec(text.encode())

def execute_label(label, subroutine=True):
    nowait = not subroutine
    return bool(AHK.ahkLabel(label.encode(), ctypes.c_uint(nowait)))

def execute_function(function, *args):
    p = AHK.ahkFunction(function.encode(), *[_represent(arg) for arg in args])
    return _evaluate(p)

def post_function(function, *args):
    return not AHK.ahkPostFunction(function.encode(), *[_represent(arg) for arg in args])

def assign(variable, value):
    return not AHK.ahkassign(variable.encode(), _represent(value))

def get(variable, pointer=False):
    p = AHK.ahkgetvar(variable.encode(), ctypes.c_uint(pointer))
    return _evaluate(p)

def terminate(kill=False):
    return not AHK.ahkTerminate(ctypes.c_int(kill))

def reload():
    return not AHK.ahkReload()

def get_function_pointer(function):
    return AHK.ahkFindFunc(function.encode())

def get_label_pointer(label):
    return AHK.ahkFindLabel(label.encode())

def pause():
    return bool(AHK.ahkPause("on".encode()))

def unpause():
    return not AHK.ahkPause("off".encode())

def execute_line(line_pointer, mode=0, wait=False):
    return AHK.ahkExecuteLine(ctypes.c_uint(line_pointer), ctypes.c_uint(mode), ctypes.c_uint(wait))
