import datetime
import sys
import wx
import os

from petstore.com.petstore.dao.orderDao import OrderDao
from petstore.com.petstore.dao.ProductDao import ProductDao
from petstore.com.petstore.dao.orderdetailDao import OrderDetailDao
from petstore.com.petstore.ui.my_frame import MyFrame
from petstore.com.petstore.ui.cart_gridtable import CartGridTable


class CartFrame(MyFrame):
    def __init__(self, cart, product_list_frame):
        super().__init__(title='商品购物车', size=(1000, 700))
        # 购物车，键为id,值为数量
        self.cart = cart
        self.product_list_frame = product_list_frame

        self.data = self.loaddata()
