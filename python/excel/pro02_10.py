# Openpyxl 冻结窗格
"""
冻结窗格时，在滚动到工作表的另一个区域时，我们会保持工作表的某个区域可见。
"""

from openpyxl import Workbook
from openpyxl.styles import Alignment

book = Workbook()
sheet = book.active

sheet.freeze_panes = 'B2'

book.save('pro02_10.xlsx')