import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from widgets.canvas_widget import CanvasWidget
from config import get_config

from libs.version import __version__

__appname__ = 'Image Viewer'
form_class = uic.loadUiType("UI/image_viewer_main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._initData()
        self._loadUiInit()
        self._setEvent()


    def _initData(self):
        '''
        Data 초기화
        :return:
        '''
        self._config = get_config()
        pass


    def _loadUiInit(self):
        '''
        UI 초기화
        :return: None
        '''
        self.setWindowTitle("{title} ({version})".format(title=__appname__, version=__version__))
        self.canvas_widget = CanvasWidget()
        self.layout_canvas.addWidget(self.canvas_widget)
        pass


    def _setEvent(self):
        '''
        Event 설정
        :return: None
        '''
        self.action_openFile.triggered.connect(self.openFile)            # 메뉴 - Open File

        pass


    #def paintEvent(self, event):
        #painter = QPainter()
        #painter.begin(self)
        #painter.drawImage(15,self.canvas_widget.lbl_image)
        #self.drawImages(painter)
        #painter.end()


    #def drawImages(self, painter):
        #print("draw image") 
    

    def openFile(self):
        if self._config["debug"]:
            print('Debug : Open File')
        
        fileName, fileType = QFileDialog.getOpenFileName(self, "불러올 이미지를 선택하세요.", "", "jpg file(*.jpg);;gif file(*.gif);;png file(*.png)" )

        if fileName:
            print(fileName)
            print(fileType)

            pixmap = QPixmap(fileName)
            
            pixmap = pixmap.scaled(800, 500)
            #pixmap =pixmap.scaled(int(pixmap.width()/2),int(pixmap.height()/2))
            #self.canvas_widget = QImage(fileName).scaled(120,120)
            self.canvas_widget.lbl_image.setPixmap(pixmap)
                      
        QMessageBox.information(self, "Open File", "Open file event")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())