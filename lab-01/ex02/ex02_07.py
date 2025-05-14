print('Nhap cac dong can ban (Nhap done de ket thuc): ')
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    
print('\n Cac dong nhap sau khi chuyen thanh in ho: ')
for line in lines:
    print(line.upper())