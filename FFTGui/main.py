import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, \
    QVBoxLayout, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt
from plot import Plot
from table import Table

from typing import Union, Optional


def _init_frame(widget: QWidget):
    frame = QFrame()
    frame.setFrameShape(QFrame.StyledPanel)
    layout = QVBoxLayout()
    layout.addWidget(widget)
    frame.setLayout(layout)
    return frame


def _perform_fft_transform():
    pass


class MainWindow(QMainWindow):
    """Main Window of the application"""

    def __init__(self):
        super().__init__()
        self.raw_signal_plot: Optional[Plot] = None
        self.fft_signal_plot: Optional[Plot] = None
        self.table: Optional[Table] = None
        self.init_ui()

    def init_ui(self):
        self.init_main_menu()

        self.raw_signal_plot = Plot()
        self.fft_signal_plot = Plot()
        self.table = Table()
        top = _init_frame(self.raw_signal_plot)
        bottom = _init_frame(self.fft_signal_plot)
        right = _init_frame(self.table)

        v_splitter = QSplitter(Qt.Vertical)
        v_splitter.addWidget(top)
        v_splitter.addWidget(bottom)

        h_splitter = QSplitter(Qt.Horizontal)
        h_splitter.addWidget(v_splitter)
        h_splitter.addWidget(right)

        self.setCentralWidget(h_splitter)

    def init_main_menu(self):
        """Init main menu bar"""
        self.createActions()
        menubar = self.menuBar()
        file_menu = menubar.addMenu('&Fichier')
        file_menu.addAction(self.file_open)
        file_menu.addAction(self.close_window)

    def createActions(self):
        """Create actions for the main menu bar"""
        self.file_open = QAction('&Ouvrir',
                                 shortcut='Ctrl+O',
                                 statusTip='Ouvre un fichier csv',
                                 triggered=self.onFileOpen)
        self.close_window = QAction('&Quitter',
                                    shortcut='Ctrl+Q',
                                    statusTip="Quitte l'application",
                                    triggered=self.close)

    def onFileOpen(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())
