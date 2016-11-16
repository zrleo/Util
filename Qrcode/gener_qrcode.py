# -*- coding:utf-8 -*-


import qrcode

import xlrd

def read_exl(filepath):

    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0) #读取第一页
    rows = sheet.nrows #获取所有行数
    case_list = []
    print case_list
    for i in range(rows):
        case_list.append(sheet.row_values(i))
    gen_qrcode(case_list,filepath)

def gen_qrcode(case_list,filepath):
    '''此函数用来生成二维码'''

    for case in case_list:
        product_code = case[0]
        veryfy_code = int(case[1])

        print product_code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data('%s'%product_code)
        qr.make(fit=True)
        img = qr.make_image()
        img.save('%s.png'%veryfy_code)


if __name__ == '__main__':
    read_exl('code.xlsx')
