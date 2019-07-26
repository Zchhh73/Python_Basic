'''定义窗口基类'''
import sys
import wx
import os


class MyFrame(wx.Frame):
    # 用户登录成功后，保留信息
    Session = {}

    def __init__(self, title, size):
        super().__init__(parent=None, title=title, size=size, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)

        self.Centre()
        self.contentpanel = wx.Panel(parent=self)
        icon = wx.Icon(os.path.join(
            os.path.join(os.path.abspath(os.path.join(os.getcwd(), "../../..")), 'resources\icon\\dog.jpg')),
            wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)
        # 设置窗口最大最小尺寸
        self.SetSizeHints(size, size)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def OnClose(self, event):
        self.Destroy()
        sys.exit(0)
