from PIL import Image
import pilgram
velgbilde = input('velg bilde du vil redigere(skriv full adresse): ')

im = Image.open(f'{velgbilde}')

bildenavn = input('hva vil du at bildet skal hete')
pilgram.moon(im).save(f'image/{bildenavn}')