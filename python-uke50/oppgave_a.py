from PIL import Image
import pilgram
velgbilde = input('velg bilde du vil redigere(skriv full adresse): ')

im = Image.open(f'{velgbilde}')
pilgram._1977(im).save('image/sample-_1977.png')