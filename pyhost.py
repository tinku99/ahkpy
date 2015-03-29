# if you don't want to use wxpython then do the next 2 lines          
# python /c/Python26/Scripts/ipython.py -wthread -i pyquery.py
# must use -wthread otherwise calling com client hangs

      
import win32com.client
import time, datetime
import pythoncom
from pcomserver import PComServer
# import wx

class PyExample(PComServer):
    def echo(self, msg):
	return msg	
    
clsid = "{55C2F76F-5136-4614-A397-12214CC011E5}"
appid = "Python.Example"
p = PyExample(clsid, appid)
pythoncom.PumpMessages()
