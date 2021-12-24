num=1
for elem in range(1,101):
    img = openpyxl.drawing.image.Image(f'{num}.png')
    img.anchor = f'A{num}'
    ws.add_image(img)
    imgs.append(img)
    num+=1

wb.save('temp.xlsx')