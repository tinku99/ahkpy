          
# python /c/Python26/Scripts/ipython.py -wthread -i pyquery.py
# must use -wthread otherwise calling com client hangs

      
import win32com.client
import time, datetime
from pcomserver import PComServer
class PyExample(PComServer):
    def printMatrix(self, matrix):
        print type(matrix)
        print matrix
        for i in matrix:
            print i
    def getMatrix(self):
        x = ["s", "d", "fd"]
        y = [x, x, x]
        return y

    
clsid = "{55C2F76F-5136-4614-A397-12214CC011E5}"
appid = "Python.Example"
p = PyExample(clsid, appid)
    
