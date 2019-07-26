import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='StaticBox布局', size=(300, 200))
        self.Centre()
        panel = wx.Panel(parent=self)
        # 垂直方向的Box
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.statictext = wx.StaticText(parent=panel, label='Button1单击')
        vbox.Add(self.statictext, proportion=2, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER, border=10)

        b1 = wx.Button(parent=panel, id=10, label='按钮框')
        b2 = wx.Button(parent=panel, id=11, label='按钮框')
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)
        # 创建静态框对象
        sb = wx.StaticBox(panel, label='候选框')
        # 创建水平方向的StaticBox布局管理器
        habox = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        habox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
        habox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)
        vbox.Add(habox, proportion=1, flag=wx.CENTER)
        panel.SetSizer(vbox)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击')


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
