from PIL import Image, ImageFont, ImageDraw

velgbilde = input('Velg bilde du vil redigere (skriv full adresse): ')

im = Image.open(f'{velgbilde}')

wm = im.width // 2

draw = ImageDraw.Draw(im)

text1 = input("Text-top: ")
text2 = input("Text-bottom: ")
print(im.height)
høyde1 = int(input('Top text height: '))
høyde2 = int(input('Bottom text height: '))

text_position = (wm, høyde2)
fs = 70
f = ImageFont.load_default().font_variant(size=fs)
draw.text(text_position, text2, fill="black", font=f)


text_position1 = (wm, høyde1)
fs1 = 70
f1 = ImageFont.load_default().font_variant(size=fs1)
draw.text(text_position1, text1, fill="black", font=f1)

imgname = input('Hva vil du at bildet skal hete?: ')
im.save(f"image/{imgname}")