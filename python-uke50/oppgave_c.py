from PIL import Image
import pilgram
 
velgbilde = input('velg bilde du vil redigere(skriv full adresse): ')

im = Image.open(f'{velgbilde}')

valg = input("right, left or upside down: ")

if valg == ('right'):
    rotated_im = im.rotate(270)

elif valg == ('left'):
    rotated_im = im.rotate(90)

elif valg == ('upside down'):
    rotated_im = im.rotate(180)
    
rotated_im.save(f"image/sample-rotated_ {valg} .jpg")