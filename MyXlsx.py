#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
本文件用以实现对Excel xlsx格式文件的读写操作
读取的文件名格式固定，根据文件名格式来判断文件表头格式 接触网 OCS+UnitName+Date.xlsx 通信网 CNS+UnitName+Date.xlsx
1.表头格式
2.数据格式
3.数据写入
4.数据读取
'''
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from xlsxwriter import worksheet
import xlsxwriter

def settitleFormat(worksheet):
    #根据不同的sheetname将表头格式固定，并返回表头格式对象
    titleFormat = xlsxwriter.add_format()
    pass

def setDataFormat(worksheet):
    pass

# def setTableFormat(worksheet = worksheet):
#     if worksheet.name` ==
#     pass
def writeTitle(worksheet):
    pass

def writeData(worksheet):
    pass

def readTitle(worksheet):
    pass

def readData(worksheet):
    pass
# 保存文件，接触网共9张表格对应最后生成的文件9个sheet页面

'''
1历史概况----------------------------------tableWidget
2设备概况表--------------------------------tableWidget_2
3设备汇总表 (设备变更履历表)-----------------tableWidget_3
4分段-------------------------------------tableWidget_4
5分相-------------------------------------tableWidget_5
6隔开-------------------------------------tableWidget_6
7跨越-------------------------------------tableWidget_7
8桥梁-------------------------------------tableWidget_8
9上网点-----------------------------------tableWidget_9
'''
def saveSheet(filename='',table = QTableWidget):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet(table.objectName())
    if worksheet.get_name() == 'tableWidget':
        #设置页面宽度
        worksheet.set_column('A:A', 13)
        worksheet.set_column('B:B', 110)
        # worksheet.set_column('C:C', 90)

        titleFormat = workbook.add_format()
        # titleFormat.set_bold()  # 设置粗体字
        titleFormat.set_font_size(18)  # 设置字体大小为18
        titleFormat.set_font_name('黑体')  # 设置字体样式为雅黑
        titleFormat.set_align('center')  # 设置水平居中对齐
        titleFormat.set_align('vcenter')  # 设置垂直居中对齐
        #合并title区域单元格
        worksheet.merge_range(0, 0, 0, 1,"历史概况履历表",titleFormat)

        title2LeftFormat = workbook.add_format()
        title2LeftFormat.set_bold()
        title2LeftFormat.set_font_name('宋体')  # 设置字体样式为雅黑
        title2LeftFormat.set_font_size(10)  # 设置字体大小为10
        title2LeftFormat.set_align('center')
        title2LeftFormat.set_align('vcenter')  # 设置垂直居中对齐
        # title2left = "部门（工队）：" + "定西供电工队"
        title2left = "部门（工队）：定西供电工队                                                                                肃技-网1"
        worksheet.merge_range(1, 0, 1, 1, title2left, title2LeftFormat)


        title3Format = workbook.add_format()
        title3Format.set_bold()
        title3Format.set_font_name('宋体')  # 设置字体样式为雅黑
        title3Format.set_font_size(10)  # 设置字体大小为10
        title3Format.set_align('center')
        title3Format.set_align('vcenter')  # 设置垂直居中对齐
        title3Format.set_border()
        worksheet.write(2, 0, '年度', title3Format)
        worksheet.write(2, 1, '概况记录', title3Format)


        # 再添加一个样式rowFormat，将作为数据行的格式
        yearFormat = workbook.add_format()
        yearFormat.set_font_size(10)
        yearFormat.set_font_name('宋体')
        yearFormat.set_align('center')
        yearFormat.set_align('vcenter')
        # yearFormat.set_align('vjustify')
        yearFormat.set_border()
        yearFormat.set_text_wrap()

        profileFormat = workbook.add_format()
        profileFormat.set_font_size(10)
        profileFormat.set_font_name('宋体')
        profileFormat.set_align('left')
        # profileFormat.set_align('vjustify')
        profileFormat.set_border()
        profileFormat.set_text_wrap()  # 设置自动换行


        rowFormat = workbook.add_format()
        rowFormat.set_text_wrap()

        for row in range(table.rowCount()):
             for column in range(table.columnCount()):
                item = QTableWidgetItem(table.item(row, column))
                # print(item.text())
                # worksheet.write(row + 3, column, item.text(),merge_format)
                if column == 0:
                    worksheet.write(row + 3, column, item.text(),yearFormat)
                elif column == 1:
                    # worksheet.merge_range(row + 3, 1, row + 3, 2, item.text(),merge_format)
                    worksheet.write(row + 3, column, item.text(), profileFormat)
                else:
                    return Exception
        pass
    elif worksheet.get_name() == 'tableWidget_2':
        pass
    elif worksheet.get_name() == 'tableWidget_3':
        pass
    elif worksheet.get_name() == 'tableWidget_4':
        pass
    elif worksheet.get_name() == 'tableWidget_5':
        pass
    elif worksheet.get_name() == 'tableWidget_6':
        pass
    elif worksheet.get_name() == 'tableWidget_7':
        pass
    elif worksheet.get_name() == 'tableWidget_8':
        pass
    elif worksheet.get_name() == 'tableWidget_9':
        pass
    workbook.close()
    return 0

def testsheet():
    workbook = xlsxwriter.Workbook('d:\\test.xlsx')
    worksheet = workbook.add_worksheet('tableWidget')
    if worksheet.get_name() == 'tableWidget':
        #设置页面宽度
        worksheet.set_column('A:A', 13)
        worksheet.set_column('B:B', 110)
        # worksheet.set_column('C:C', 90)

        # add_format() 为当前workbook添加一个样式名为titleFormat
        titleFormat = workbook.add_format()
        # titleFormat.set_bold()  # 设置粗体字
        titleFormat.set_font_size(18)  # 设置字体大小为18
        titleFormat.set_font_name('黑体')  # 设置字体样式为雅黑
        titleFormat.set_align('center')  # 设置水平居中对齐
        titleFormat.set_align('vcenter')  # 设置垂直居中对齐
        # 将titleFormat应用在第一行，此行为标题
        # worksheet.set_row(0, None, titleFormat)
        #合并title区域单元格
        worksheet.merge_range(0, 0, 0, 1,"历史概况履历表",titleFormat)

        # title2RightFormat = workbook.add_format()
        # title2RightFormat.set_bold()
        # title2RightFormat.set_font_name('宋体')  # 设置字体样式为雅黑
        # title2RightFormat.set_font_size(10)  # 设置字体大小为10
        # title2RightFormat.set_align('right')
        # title2RightFormat.set_align('vcenter')  # 设置垂直居中对齐
        # # worksheet.set_row(2, None, title2RightFormat)
        # title2right = "肃技-网1"
        # worksheet.write(1, 1, title2right, title2RightFormat)


        title2LeftFormat = workbook.add_format()
        title2LeftFormat.set_bold()
        title2LeftFormat.set_font_name('宋体')  # 设置字体样式为雅黑
        title2LeftFormat.set_font_size(10)  # 设置字体大小为10
        title2LeftFormat.set_align('center')
        title2LeftFormat.set_align('vcenter')  # 设置垂直居中对齐
        # title2left = "部门（工队）：" + "定西供电工队"
        title2left = "部门（工队）：定西供电工队                                                                                肃技-网1"
        # worksheet.write(1, 0, title2left, title2LeftFormat)
        # worksheet.set_row(1, None, title2LeftFormat)
        worksheet.merge_range(1, 0, 1, 1, title2left, title2LeftFormat)



        title3Format = workbook.add_format()
        title3Format.set_bold()
        title3Format.set_font_name('宋体')  # 设置字体样式为雅黑
        title3Format.set_font_size(10)  # 设置字体大小为10
        title3Format.set_align('center')
        title3Format.set_align('vcenter')  # 设置垂直居中对齐
        title3Format.set_border()
        worksheet.write(2, 0, '年度', title3Format)
        worksheet.write(2, 1, '概况记录', title3Format)


        # 再添加一个样式rowFormat，将作为数据行的格式
        rowFormat = workbook.add_format()
        rowFormat.set_font_size(10)
        rowFormat.set_font_name('Microsoft yahei')
        rowFormat.set_align('left')
        rowFormat.set_align('vcenter')
        rowFormat.set_text_wrap()  # 设置自动换行
        # rangetable = 'leftupcorner:rightdowncorner', 如'A1:D20', 用左上角的单元格编号与右下角的单元格编号标识表格中的一块矩形区域。
        pass
    workbook.close()



if __name__ == '__main__':
    testsheet()