Dim WebAddress
WebAddress=InputBox("请输入你要ping的网络地址","ping a computer without using ping.exe","www.google.cn")
If WebAddress <> "" Then
Set OBJWMIService = GetObject("winmgmts:\\.\root\cimv2")
Set colPings = OBJWMIService.ExecQuery("Select * From Win32_PingStatus Where Address = '" &WebAddress& "'")
For Each OBJStatus in colPings
    If IsNull(OBJStatus.StatusCode) Or OBJStatus.StatusCode <> 0 Then 
        WScript.Echo "网址：" & WebAddress  & "无法连接,程序将退出！"
    Else
       call Main  
    End If
Next
End If

function Main()
   WScript.Echo "恭喜你，能够成功的ping通！" 
end function