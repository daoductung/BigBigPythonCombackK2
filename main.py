from customer import Customer
from invoice import Invoice, ImportInvoice, ExportInvoice
from personnel import Personnel
from producer import Producer
from product import Product, ProductDetails

import datetime

while True:
    print("------------> MENU <-----------")
    print("1. Nhan vien.")
    print("2. Khach hang.")
    print("3. Hoa don.")
    print("4. Giay.")
    print("5. Nha cung cap.")
    print("6. Thoat")
    choose = input(print("Moi ban chuc nang:"))

    if choose == '1':
        nv = Personnel("1", "Nguyen Van A", 22, "Hung Yen", "0123456789", datetime.date(2018, 12, 12))
        print("Thong tin nhan vien")
        nv.Display()
    elif choose == '2':
        kh = Customer("1", "Nguyen Van A", 23, "Ha Noi")
        print("Thong tin khach hang")
        kh.Display()
    elif choose == '3':
        hdn = ImportInvoice("1", "Hoa don nhap", "Nhap hang", datetime.date(2018, 12, 12), "Nguyen Van B", 2000000, "Biti")
        hdx = ExportInvoice("1", "Hoa don xuat", "Xuat hang", datetime.date(2018, 12, 12), "Nguyen Van B", 200000, "Nguyen Van C", "Ha Noi", "0123456789")
        print("Thong tin hoa don nhap")
        hdn.Display()
        print("Thong tin hoa don xuat")
        hdx.Display()
    elif choose == '4':
        g = ProductDetails("1", "Convert", "Biti", datetime.date(2018, 12, 22))
        print("Thong tin san pham")
        g.Display()
    elif choose == '5':
        ncc = Producer("1", "Biti", "Ha Noi")
        print("Thong tin nha cung cap")
        ncc.Display()
    elif choose == "6":
        print("Da thoat.")
        break
    else:
        print("Nhap sai! Vui long nhap lai")
