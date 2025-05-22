from rembg import remove 
from PIL import Image
import os 

os.chdir('tools/IMG')


## Path for input and output image
input_img = 'img/test3.png'
output_img = 'img/test4.png'

## loading and removing background
inp = Image.open(input_img)
output = remove(inp)

## Saving background removed image to same location as input image
output.save(output_img)
