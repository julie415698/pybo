import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

img_path = r'C:\imagetest\bolg4.PNG' # filename
image_pil = Image.open(img_path)
image = pytesseract.image_to_string(image_pil,lang="kor")
print(image) #성공
