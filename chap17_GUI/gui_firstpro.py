import wx

app = wx.App()

frm = wx.Frame(None, title='第一个GUI程序.', size=(400, 300), pos=(100, 100))

frm.Show()
app.MainLoop()
