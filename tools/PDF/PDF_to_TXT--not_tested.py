from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image
import pytesseract
from pytesseract import Output
import cv2
import numpy

images = convert_from_path('invoice.pdf')
for i,source in enumerate(images):
    print ("Page N°{}\n".format(i+1))
    
    #convert PIL to opencv
    pil_image = source.convert('RGB') 
    open_cv_image = numpy.array(pil_image) 
    # Convert RGB to BGR 
    img = open_cv_image[:, :, ::-1].copy() 
    #img = cv2.imread(source)

    d = pytesseract.image_to_data(img, output_type=Output.DICT)
     
    NbBox = len(d['level'])
    print ("Number of boxes: {}".format(NbBox))

    for j in range(NbBox):
        (x, y, w, h) = (d['left'][j], d['top'][j], d['width'][j], d['height'][j])
        # display rectangle
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()