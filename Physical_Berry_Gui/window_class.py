import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import text_editor_class
from cv2 import *

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        extract_action = QAction("Save & Exit",self)
        extract_action.setShortcut("Ctrl+q")
        extract_action.setStatusTip("Leave the app")
        extract_action.triggered.connect(self.quit)

        extract_action_edit = QAction("Show files", self)
        extract_action_edit.setShortcut("Ctrl+f")
        extract_action_edit.setStatusTip("Looking for files")
        extract_action_edit.triggered.connect(self.quit)


        openEditor = QAction("Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip("Open Editor")
        openEditor.triggered.connect(self.editor)

        openFile = QAction("Open File", self)
        openFile.setShortcut("Ctrl+o")
        openFile.setStatusTip("Open File")
        openFile.triggered.connect(self.file_Open)
        self.statusBar()

#        help_window = QAction("Help", self)
#        help_window.setShortcut("Ctrl+h")
#        help_window.setStatusTip("Help for the berry interface")
#        help_window.triggered.connect(self.help_window)
        #self.newWindow = help_window(self)

        self.pushButton = QPushButton("New Window", self)
        self.pushButton.move(120, 120)
        self.pushButton.clicked.connect(self.help_window)
        self.newWindow = help(self)

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("&File")
        fileMenu.addAction(extract_action)
        fileMenu.addAction(openFile)
        fileMenu = mainMenu.addMenu("&Editor")
        fileMenu.addAction(openEditor)
        #fileMenu = mainMenu.addMenu("&Help")
        #fileMenu.addAction(help)

        self.setWindowTitle("Berry GUI")
        self.setGeometry(100,200,1280,775)
        #self.button1 = QPushButton()
        #self.button2 = QPushButton()

        self.setWindowIcon(QIcon("berry_icon.png"))
        #self.home_window()

        # Toolbars initialized here
        # toolbar menu icon set here
        # Triggering actions are assigned here
        extract_action_toolbar_berry = QAction(QIcon("flatberry.png"), "Connect to the berries", self)
        extract_action_toolbar_berry.triggered.connect(self.close)

        self.toolBar = self.addToolBar("BeRRY")
        self.toolBar.addAction(extract_action_toolbar_berry)

        extract_action_toolbar_berry = QAction(QIcon("camera.png"), "Take Picture Using Webcam", self)
        extract_action_toolbar_berry.triggered.connect(self.camera)

        self.toolBar = self.addToolBar("Camera toolbar")
        self.toolBar.addAction(extract_action_toolbar_berry)

        extract_action_toolbar_berry = QAction(QIcon("lights.png"), "Flashes the lights", self)
        extract_action_toolbar_berry.triggered.connect(self.close)

        self.toolBar = self.addToolBar("Lights toolbar")
        self.toolBar.addAction(extract_action_toolbar_berry)

        extract_action_toolbar_berry = QAction(QIcon(""), "Opens the Editor", self)
        extract_action_toolbar_berry.triggered.connect(self.editor_window)

        self.toolBar = self.addToolBar("Editor")
        self.toolBar.addAction(extract_action_toolbar_berry)

        extract_action_toolbar_berry = QAction(QIcon(""), "Set the image", self)
        extract_action_toolbar_berry.triggered.connect(self.reset_background)

        self.toolBar = self.addToolBar("Reset Background")
        self.toolBar.addAction(extract_action_toolbar_berry)


        #background_image = QImage("berry_photo.jpg")
        self.layout = QGridLayout()
        #layout.addWidget(background_image)

        self.show()



    def help_window(self):
        self.newWindow.show()

    def quit(self):
        print("Quiting out, Thanks...")
        choice = QMessageBox.question(self, "Close Application", "Are you sure you want to quit?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Quiting Berry GUI")
            sys.exit()
        else:
            pass


    def editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)



    def look_for_files(self):
        print("Looking for all of your files...")

    def file_Open(self):

        name, _ = QFileDialog.getOpenFileName(self, "Open File")

        print(name)


        self.editor()
        with open(name, "r") as file:
            text = file.read()
            self.textEdit.setText(text)

    def editor_window(self):
        text_editor_class.main()
        print("Showing the Editor")


    def camera(self):
        # initialize the camera
        cam = VideoCapture(0)  # 0 -> index of camera
        s, img = cam.read()
        if s:  # frame captured without any errors
            #namedWindow("Berry Snapper")
            imshow("Berry Snapper", img)
            waitKey(0)
            destroyWindow("Berry Snapper")
            imwrite("CRAZY.jpg", img)  # save image


    def reset_background(self):
        self.layout = QGridLayout()
        # layout.addWidget(background_image)

        label = QLabel(self)
        pixmap = QPixmap('detected_berries.jpg')
        # pixmap = QPixmap("berry_background.jpg")
        label.setPixmap(pixmap)

        label.resize(pixmap.width(), pixmap.height())
        label.move(0, 55)

        self.layout.addWidget(label)



        label.resize(pixmap.width(), pixmap.height())
        label.move(0,55)

        self.layout.addWidget(label)
        self.show()


class help(QMainWindow):
    def __init__(self, parent=None):
        super(help, self).__init__(parent)
        #Setting a title, locating and sizing the window
        self.title = 'Help'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 500
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.pushButton = QPushButton("Close Me", self)
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.pushButton.move(120,120)

    def on_pushButton_clicked(self):
        self.close()



def main():
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


    def home_window(self):
        """
        button1 = QPushButton("Find Berries")
        button2 = QPushButton("Quit")
        #label = QLabel("Something")

        h_box = QHBoxLayout()
        h_box.addStretch()
        #h_box.addWidget(self.label)
        h_box.addStretch()

        v_box = QVBoxLayout()
        v_box.addWidget(self.button1)
        v_box.addWidget(self.button2)
        v_box.addLayout(h_box)

        self.setLayout(v_box)

        button1.clicked.connect(self.button_click)
        button2.clicked.connect(self.quit)
        button1.move(0, 100)
        button2.move(0, 300)
        """

        #self.show()

        # def button_click(self):
        # self.label.setText("Berries are up to Date")
        # self.dialog.show()