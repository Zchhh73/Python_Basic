import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='FlexGrid布局', size=(400, 200))
        self.Centre()
        panel = wx.Panel(self)

        # 创建3行2列，间隙为10
        fgs = wx.FlexGridSizer(3, 2, 10, 10)
        title = wx.StaticText(panel, label='标题：')
        author = wx.StaticText(panel, label='作者：')
        review = wx.StaticText(panel, label='内容：')

        tc1 = wx.TextCtrl(panel)
        tc2 = wx.TextCtrl(panel)
        tc3 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

        fgs.AddMany([title, (tc1, 1, wx.EXPAND),
                     author, (tc2, 1, wx.EXPAND),
                     review, (tc3, 1, wx.EXPAND)])

        # 第一行可扩展 占1/5
        fgs.AddGrowableRow(0, 1)
        fgs.AddGrowableRow(1, 1)
        # 第三行可扩展 占3/5
        fgs.AddGrowableRow(2, 3)
        # 第1列可扩展 占1/3
        fgs.AddGrowableCol(0, 1)
        # 第2列可扩展 占2/3
        fgs.AddGrowableCol(1, 2)
