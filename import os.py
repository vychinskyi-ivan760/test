import os
from tkinter import Image
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import ( QApplication, QWidget, QFileDialog, QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout )

app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')
lb_image = QLabel("картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()


btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image, 95)
rom_tools = QHBoxLayout()
rom_tools.addWidget(btn_left)
rom_tools.addWidget(btn_right)
rom_tools.addWidget(btn_flip)
rom_tools.addWidget(btn_sharp)
rom_tools.addWidget(btn_bw)
col2.addLayout(rom_tools)


row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


workdir = ''

def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
            return result
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter( os.listdir(workdir), extensions )
    lw_files.clear
    for files in filenames:
        lw_files.addItem(files)

btn_dir.clicked.connect(showFilenamesList)


class ImageProcesor():
    def __init__(self):
        self.image = None 
        self.dir = None
        self.filenames = None 
        self.self_dir = "Modfiled/"

    def LoadImage(self, filename):
        self.filenames = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def saveImage(self):
        path = os.path.join(workdir, self.filenames)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filenames)
        self.image.save(fullname)
    
    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def showChosenImage():
        if lw_files.currentRow() >= 0:
            filename = lw_files.currentItem().text()
            workimage.loadImage(filename)
            workimage.showImage(os.path.join(workdir, workimage.filename))
 
workimage = ImageProcessor() #поточне робоче зображення для роботи
lw_files.currentRowChanged.connect(showChosenImage)
 
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_flip.clicked.connect(workimage.do_flip)

app.exec_()
win.show()