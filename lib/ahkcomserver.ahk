;; comserver()
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















