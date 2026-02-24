from data.dataconnection import DataConnection

class DienThoaiRepository:
    def __init__(self):
        self.conn = DataConnection.get_connection()

    def get_all_dienthoai(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MaDT, TenDT, HangSX, MauSac, GiaBan FROM DienThoai")
        return cursor.fetchall()
    
    def add_dienthoai(self, MaDT, TenDT, HangSX, MauSac, GiaBan):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO DienThoai (MaDT, TenDT, HangSX, MauSac, GiaBan) VALUES (?, ?, ?, ?, ?)",
            (MaDT, TenDT, HangSX, MauSac, GiaBan)
        )
        self.conn.commit()

    def update_dienthoai(self, MaDT, TenDT, HangSX, MauSac, GiaBan):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE DienThoai SET TenDT=?, HangSX=?, MauSac=?, GiaBan=? WHERE MaDT=?",
            (TenDT, HangSX, MauSac, GiaBan, MaDT)
        )
        self.conn.commit()
    
    def delete_dienthoai(self, MaDT):
        cursor = self.conn.cursor()
        cursor.execute(
            "DELETE FROM DienThoai WHERE MaDT=?", (MaDT,))
        self.conn.commit()

    def search_dienthoai_by_ma(self, MaDT):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT MaDT, TenDT, HangSX, MauSac, GiaBan FROM DienThoai WHERE MaDT LIKE ?",
            ('%' + MaDT + '%',)
        )
        return cursor.fetchall()
