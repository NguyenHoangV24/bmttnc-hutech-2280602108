gio_lam = float(input('Nhap so gio tieu chuan: '))
luong_gio = float(input('Nhap thu lao tren moi gio tieu chuan: '))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, gio_lam - gio_tieu_chuan)

tien_luong = gio_tieu_chuan *luong_gio + gio_vuot_chuan *luong_gio

print('So tien luong thang la: ', tien_luong) 