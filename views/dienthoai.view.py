from controllers.dienthoai_controller import DienThoaiController
from models.dienthoai_model import DienThoaiModel

class MainView:
    def __init__(self):
        self.controller = DienThoaiController()

    def menu(self):
        while True:
            print("\n=== Quản Lý  ===")
            print("1. Xem tất cả điện thoại")
            print("2. Thêm điện thoại")
            print("3. Sửa điện thoại")
            print("4. Xóa điện thoại theo mã")
            print("5. Tìm kiếm điện thoại theo mã")
            print("6. Thoát")
            choice = input("Chọn một cái đi cậu (1-6): ")

            if choice == '1':
                self.controller.lay_tat_ca_dienthoai()
            elif choice == '2':
                TenDT = input("Nhập Tên Điện Thoại: ")
                HangDT = input("Nhập Hãng Điện Thoại: ")
                MauSac = input("Nhập Màu Sắc: ")
                GiaBan = float(input("Nhập Giá Bán: "))
                self.controller.them_dienthoai(TenDT, HangDT, MauSac, GiaBan)
            elif choice == '3':
                MaDT = input("Nhập Mã Điện Thoại cần sửa: ")
                TenDT = input("Nhập Tên Điện Thoại mới: ")
                HangDT = input("Nhập Hãng Điện Thoại mới: ")
                MauSac = input("Nhập Màu Sắc mới: ")
                GiaBan = float(input("Nhập Giá Bán mới: "))
                self.controller.sua_dienthoai(MaDT, TenDT, HangDT, MauSac, GiaBan)
            elif choice == '4':
                MaDT = input("Nhập Mã Điện Thoại cần xóa: ")
                self.controller.xoa_dienthoai(MaDT)