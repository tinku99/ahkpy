import os, gc
import win32com.client
import time, datetime
from win32com.server.util import wrap, unwrap
from win32com.server.dispatcher import DefaultDebugDispatcher
from ctypes import *
import commands
import pythoncom
import winerror
from win32com.server.exception import Exception         
import win32com.server.util, win32com.server.policy

class PComServer:
    def __init__(self, clsid, appid):
        self.data = []
        self.handle = 0
        self.dobjects = {}
        self.iid = pythoncom.MakeIID(clsid)
        self.clsid = clsid
        self.ahk = 0
        self.appid = appid
    def start(self):
        ob = win32com.server.util.wrap(self, usePolicy=win32com.server.policy.DynamicPolicy)
        try:
            handle = pythoncom.RegisterActiveObject(ob, self.iid, 0)
        except pythoncom.com_error, details:
            print "Warning - could not register the object in the ROT:", details
            handle = None    
        self.handle = handle
        return self
    def register(self, ahkAppID):
        ahk = win32com.client.Dispatch(ahkAppID) 
        ahk.aRegisterIDs(self.clsid, self.appid)
        self.ahk = ahk
        return ahk
    def __del__(self):
        pythoncom.RevokeActiveObject(self.handle)
    def _dynamic_(self, name, lcid, wFlags, args):
        if wFlags & pythoncom.DISPATCH_METHOD:
            return getattr(self,name)(*args)
        if wFlags & pythoncom.DISPATCH_PROPERTYGET:
            try:
                # to avoid problems with byref param handling, tuple results are converted to lists.
                ret = self.__dict__[name]
                if type(ret)==type(()):
                    ret = list(ret)
                return ret
            except KeyError: # Probably a method request.
                raise Exception(scode=winerror.DISP_E_MEMBERNOTFOUND)
        if wFlags & (pythoncom.DISPATCH_PROPERTYPUT | pythoncom.DISPATCH_PROPERTYPUTREF):
            setattr(self, name, args[0])
            return
        raise Exception(scode=winerror.E_INVALIDARG, desc="invalid wFlags")
    def write(self, x):
        print x
        return 0
