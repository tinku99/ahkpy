#Persistent
CLSID_ThisScript := "{38A3EB13-D0C4-478b-9720-4D0B2D361DB9}"
APPID_ThisScript := "ahk.Utility"
funcs := ["aRegisterIDs", "aGetObject", "aCallFunc"]
server := ahkComServer(CLSID_ThisScript, APPID_ThisScript, funcs)	
pythonAppid := "Python.Example"
py := ComObjActive(pythonAppid)
py.write("hello")
return

f2::
py := ComObjActive(pythonAppid)
py.write("hello")
return
   
aRegisterIDs(this, CLSID, APPID){
global pythonAppid, pythonClsid
pythonAppid := APPID
pythonClsid := CLSID
RegisterIDs(CLSID, APPID)
}

aGetObject(this, name){
global
return %name%
}

aCallFunc(this, func, args){
return %func%(args)
}
     

;; ahkcomserver()
ahkComServer(CLSID_ThisScript, APPID_ThisScript, funcs)
{
global serverReady
server := object()
  
  RegisterIDs(CLSID_ThisScript, APPID_ThisScript)
for i, func in funcs
{
str .= func . ", "
}
str := SubStr(str, 1, strlen(str) - 2)

  myObj := ComDispatch("", str)
  if !(hRemote := ComRemote(myObj, CLSID_ThisScript))
  {
    MsgBox, 16, %A_ScriptName%, Can't remote the object!
    ExitApp
  }
server.CLSID := CLSID_ThisScript
server.APPID := APPID_ThisScript
server.hRemote := hRemote
serverReady := 1
  return server
}
