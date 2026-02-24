class DienThoaiModel:
    def __init__(self, MaDT, TenDT, HangSX, MauSac, GiaBan):
        self.MaDT = MaDT
        self.TenDT = TenDT
        self.HangSX = HangSX
        self.MauSac = MauSac
        self.GiaBan = GiaBan

    def __str__(self):
        return f"DienThoaiModel(MaDT={self.MaDT}, TenDT={self.TenDT}, HangSX={self.HangSX}, MauSac={self.MauSac}, GiaBan={self.GiaBan})"