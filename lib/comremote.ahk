;
; File encoding:  UTF-8
; Author: fincs
;
; ComRemote: expose a COM object in order to receive remote (RPC) calls
;

Str2GUID(ByRef var, str){
	VarSetCapacity(var, 16)
	DllCall("ole32\CLSIDFromString", "wstr", str, "ptr", &var)
	return &var
}

ComRemote(disp, clsid){
	static ACTIVEOBJECT_WEAK := 1
	static _base := Object("Close", "_CR_Disconnect", "__Delete", "_CR_Disconnect")
	if DllCall("oleaut32\RegisterActiveObject"
	  , "ptr", pdisp := ComObjValue(disp)
	  , "ptr", Str2GUID(clsid_bin, clsid)
	  , "uint", ACTIVEOBJECT_WEAK
	  , "uint*", dwRegister) < 0
		return

	DllCall("ole32\CoLockObjectExternal", "ptr", pdisp, "int", 1, "int", 1)
	return Object("disp", disp, "dwRegister", dwRegister, "base", _base)
}

_CR_Disconnect(this){
	if this.closed
		return
	DllCall("ole32\CoLockObjectExternal", "ptr", pdisp := ComObjValue(this.disp), "int", 0, "int", 1)
	DllCall("oleaut32\RevokeActiveObject", "uint", this.dwRegister, "ptr", 0)
	DllCall("ole32\CoDisconnectObject", "ptr", pdisp, "uint", 0)
	this.closed := true
}
