from repository.dienthoai_repository import DienThoaiRepository

class DienThoaiService:
    def __init__(self):
        self.repo = DienThoaiRepository()

    def lay_tat_ca_dienthoai(self):
        return self.repo.get_all_dienthoai()
    
    def them_dienthoai(self, MaDT, TenDT, HangSX, MauSac, GiaBan):
        self.repo.add_dienthoai(MaDT, TenDT, HangSX, MauSac, GiaBan)
    
    def sua_dienthoai(self, MaDT, TenDT, HangSX, MauSac, GiaBan):
        self.repo.update_dienthoai(MaDT, TenDT, HangSX, MauSac, GiaBan)

    def xoa_dienthoai(self, MaDT):
        self.repo.delete_dienthoai(MaDT)

    def tim_kiem_dienthoai_theo_ma(self, MaDT):
        return self.repo.search_dienthoai_by_ma(MaDT)