from PIL import Image
import pilgram
velgbilde = input('velg bilde du vil redigere(skriv full adresse): ')

im = Image.open(f'{velgbilde}')
print(im.width, im.height)
if im.width < 1080:
    p = 1080 - im.width
    im = im.resize((im.width + p, im.height + p))

else:
    p = im.width - 1080
    im = im.resize((im.width - p, im.height - p))
print(im.width, im.height)

bildenavn = input('hva vil du at bildet skal hete')
im.save(f'image/{bildenavn}')