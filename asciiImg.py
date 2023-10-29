from PIL import Image
img = Image.open("creeper.png")

#ASCII characters for image
density  = [
            ' Ñ ',' @ ',' # ',' W ',' $ ',' 9 ',' 8 ',
            ' 7 ',' 6 ',' 5 ',' 4 ',' 3 ',' 2 ',' 1 ',
            ' 0 ',' ? ',' ! ',' a ',' b ',' c ',' ; ',
            ' : ',' + ',' = ',' - ',' . ',' _ ','   '
            ] 
photo = []
#looping through image pixels and mapping to ASCII Chars
for col in range(img.size[1]):
    for row in range(img.size[0]):
        pix = img.getpixel((row,col))
        pixSum = (pix[0] + pix[1] + pix[2])/3
        if pixSum <= 18:
            photo.append(density[27])
        elif pixSum > 18 and pixSum <= 27:
            photo.append(density[26])
        elif pixSum > 27 and pixSum <= 36:
            photo.append(density[25])
        elif pixSum > 36 and pixSum <= 45:
            photo.append(density[24])
        elif pixSum > 45 and pixSum <= 54:
            photo.append(density[23])
        elif pixSum > 54 and pixSum <= 63:
            photo.append(density[22])
        elif pixSum > 63 and pixSum <= 72:
            photo.append(density[21])
        elif pixSum > 72 and pixSum <= 81:
            photo.append(density[20])
        elif pixSum > 81 and pixSum <= 90:
            photo.append(density[19])
        elif pixSum > 90 and pixSum <= 99:
            photo.append(density[18])
        elif pixSum > 99 and pixSum <= 108:
            photo.append(density[17])
        elif pixSum > 108 and pixSum <= 117:
            photo.append(density[16])
        elif pixSum > 117 and pixSum <= 126:
            photo.append(density[15])
        elif pixSum > 126 and pixSum <= 135:
            photo.append(density[14])
        elif pixSum > 135 and pixSum <= 144:
            photo.append(density[13])
        elif pixSum > 144 and pixSum <= 153:
            photo.append(density[12])
        elif pixSum > 153 and pixSum <= 162:
            photo.append(density[11])
        elif pixSum > 162 and pixSum <= 171:
            photo.append(density[10])
        elif pixSum > 171 and pixSum <= 180:
            photo.append(density[9])
        elif pixSum > 180 and pixSum <= 189:
            photo.append(density[8])
        elif pixSum > 189 and pixSum <= 198:
            photo.append(density[7])
        elif pixSum > 198 and pixSum <= 207:
            photo.append(density[6])
        elif pixSum > 207 and pixSum <= 216:
            photo.append(density[5])
        elif pixSum > 216 and pixSum <= 225:
            photo.append(density[4])
        elif pixSum > 225 and pixSum <= 234:
            photo.append(density[3])
        elif pixSum > 234 and pixSum <= 243:
            photo.append(density[2])
        elif pixSum > 243 and pixSum <= 252:
            photo.append(density[1])
        elif pixSum > 252:
            photo.append(density[0])
    photo.append("\n")
#printing image in console
print(''.join(photo))