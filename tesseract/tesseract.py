import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
import pytesseract

class Convert:

    def tesseract(request):
        root = tk.Tk()
        #root.withdraw()         #  '#' 제외하면 위젯 안보임 : new
        root.title('waiting...')
        root.geometry('250x50')

        #tkinter label
        label = tk.Label(root, text="이미지를 선택한 후, 기다려 주세요", bg='white')
        label.pack(padx=10, pady=15)


        # root.filename : type / str
        root.filename = filedialog.askopenfilename(initialdir='./png', title='파일선택', filetypes=(
            ('png files', '*.png'), ('jpg files', '*.jpg')))

        # 이미지 불러서 나타내기
        img=Image.open(root.filename)
        img.show()
        root.destroy()  # true - 자동닫김 / mainloop는 오류 떠서 바꿈


        # tesseract 한글변환
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        convert = pytesseract.image_to_string(img, lang="kor+eng")
        convert=convert.replace("\n","<br>")

        context={'convert':convert, 'filename':root.filename}
        #1.특수문자 인식
        #2.이미지 출력하기
        #3.출력할때 줄바꿈하기


        # 딕셔너리로 반환
        return context

'''
#성공
t=Convert()
str=t.tesseract()
print(str.replace('\n',''))
'''