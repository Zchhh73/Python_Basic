import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,title="鼠标处理事件",size=(800,600))
        self.Centre()
        self.Bind(wx.EVT_LEFT_DOWN,self.on_left_down)
        self.Bind(wx.EVT_LEFT_UP, self.on_left_up)
        self.Bind(wx.EVT_MOTION, self.on_mouse_move)

    def on_left_down(self):
        print('鼠标按下')

    def on_left_up(self):
        print('鼠标释放')

    def on_mouse_move(self,event):
        if event.Dragging() and event.LeftIsDown():
            pos = event.GetPosition()
            print(pos)
