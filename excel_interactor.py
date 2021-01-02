import xlrd
import xlwt
from xlwt import Workbook
from model.product import Product
from utils.time_utils import get_current_time_in_millis

class ExcelInteractor:
  def __init__(self, wb_path):
    self.work_book = xlrd.open_workbook(wb_path)

  def get_sheets_names(self):
    print(self.work_book.sheet_names())

  def get_product_list(self):
    sheet = self.work_book.sheet_by_name(u'products')

    current_row = 2
    total_row = sheet.nrows

    productList = []

    while(current_row < total_row):
        productList.append(Product(sheet.cell_value(current_row, 3), sheet.cell_value(
            current_row, 4), sheet.cell_value(current_row, 9), sheet.cell_value(current_row, 10),get_current_time_in_millis()))
        current_row += 1

    return productList

  def dump_product_list_to_excel(self, product_list):
    sheet = self.work_book.sheet_by_name(u'products')

    
