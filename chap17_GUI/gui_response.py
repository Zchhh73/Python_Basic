import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='一对多事件处理', size=(300, 180))
        self.Centre()
        panel = wx.Panel(parent=self)
        self.statictext = wx.StaticText(parent=panel, pos=(110, 15))
        b1 = wx.Button(parent=panel, id=10, label='Button1', pos=(100, 45))
        b2 = wx.Button(parent=panel, id=11, label='Button2', pos=(100, 85))
        self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=11)

    def on_click(self, event):
        event_id = event.GetId()
        print(event_id)
        if event_id == 10:
            self.statictext.SetLabelText('Button1单击')
        else:
            self.statictext.SetLabelText('Button2单击 ')


class App(wx.App):

    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
