# OpenPyXL 图像
# 将图像插入Excel中
from openpyxl import Workbook
from openpyxl.drawing.image import Image

book = Workbook()
sheet = book.active
# 设置要插入的图像的相对位置
img = Image("icesid.jpg")
sheet['A1'] = 'This is Sid'
# 插入图像
sheet.add_image(img, 'B2')

book.save("pro02_12.xlsx")