import wx.grid

COLUMN_NAMES = {'商品编号', '商品类别', '商品中文名', '商品英文名'}

class ProductListGridTable(wx.grid.GridTableBase):
    def __init__(self,data):
        super().__init__()
        self.colLabels = COLUMN_NAMES
        self.data =data

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(COLUMN_NAMES)

    def GetValue(self, row, col):
        product = self.data[row]
        if col == 0:
            return product['productid']
        elif col == 1:
            return product['category']
        elif col == 2:
            return product['cname']
        else:
            return product['ename']

    def GetColLabelValue(self, col):
        return self.colLabels[col]