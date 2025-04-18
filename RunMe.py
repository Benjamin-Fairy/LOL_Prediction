# coding = utf-8
import riotwatcher
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import os
from tqdm import tqdm
import threading

# reload(sys)
# sys.setdefaultencoding("utf8")

b, r = [0 for i in range(5)], [0 for i in range(5)]
胜方 = ''
胜率 = 0.00

postn = ['上路', '打野', '中路', '下路', '辅助']    # 分路预存列表


def resource_path(relative_path):   # 获取当前目录以获取资源文件
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Ui_MainWindow(object):    # PyQt5 数据可视化封装
    def setupUi(self, MainWindow):  # MainWindow窗口定义
        MainWindow.setObjectName("比赛预测可视化")
        MainWindow.setEnabled(True)
        MainWindow.resize(1287, 787)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)  # QWidgets定义
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap(os.path.join(sys.path[0]+"\\Resource", "background.png")))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(54, 52, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(b[0]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_2.setMidLineWidth(0)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(54, 188, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setBaseSize(QtCore.QSize(0, 0))
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(b[1]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_3.setMidLineWidth(0)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(54, 324, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setBaseSize(QtCore.QSize(0, 0))
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(b[2]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_4.setMidLineWidth(0)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(54, 460, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setBaseSize(QtCore.QSize(0, 0))
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(b[3]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_5.setMidLineWidth(0)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(54, 596, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setBaseSize(QtCore.QSize(0, 0))
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(b[4]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_6.setMidLineWidth(0)
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.AutoText)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1160, 52, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setBaseSize(QtCore.QSize(0, 0))
        self.label_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(r[0]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_7.setMidLineWidth(0)
        self.label_7.setText("")
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1160, 188, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setBaseSize(QtCore.QSize(0, 0))
        self.label_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(r[1]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_8.setMidLineWidth(0)
        self.label_8.setText("")
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1160, 324, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setBaseSize(QtCore.QSize(0, 0))
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setStyleSheet("min-width:  72px;\n"
                                   "max-width:  72px;\n"
                                   "min-height: 72px;\n"
                                   "max-height: 72px;\n"
                                   "border-radius: 36px;\n"
                                   "border-width: 0 0 0 0;\n"
                                   "border-image: url(" +
                                   os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                str(r[2]) +
                                                ".png").replace("\\", '/') +
                                   ") 8 8 8 8 stretch strectch;")
        self.label_9.setMidLineWidth(0)
        self.label_9.setText("")
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setOpenExternalLinks(False)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1160, 460, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setBaseSize(QtCore.QSize(0, 0))
        self.label_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet("min-width:  72px;\n"
                                    "max-width:  72px;\n"
                                    "min-height: 72px;\n"
                                    "max-height: 72px;\n"
                                    "border-radius: 36px;\n"
                                    "border-width: 0 0 0 0;\n"
                                    "border-image: url(" +
                                    os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                 str(r[3]) +
                                                 ".png").replace("\\", '/') +
                                    ") 8 8 8 8 stretch strectch;")
        self.label_10.setMidLineWidth(0)
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.AutoText)
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setOpenExternalLinks(False)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1160, 596, 72, 72))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setBaseSize(QtCore.QSize(0, 0))
        self.label_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("min-width:  72px;\n"
                                    "max-width:  72px;\n"
                                    "min-height: 72px;\n"
                                    "max-height: 72px;\n"
                                    "border-radius: 36px;\n"
                                    "border-width: 0 0 0 0;\n"
                                    "border-image: url(" +
                                    os.path.join(sys.path[0]+"\\Resource", "Head/" +
                                                 str(r[4]) +
                                                 ".png").replace("\\", '/') +
                                    ") 8 8 8 8 stretch strectch;")
        self.label_11.setMidLineWidth(0)
        self.label_11.setText("")
        self.label_11.setTextFormat(QtCore.Qt.AutoText)
        self.label_11.setScaledContents(True)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setWordWrap(False)
        self.label_11.setOpenExternalLinks(False)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(150, 40, 461, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_12.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_12.setFont(font)
        self.label_12.setText(b[0])
        self.label_12.setScaledContents(False)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 176, 461, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_13.setFont(font)
        self.label_13.setText(b[1])
        self.label_13.setScaledContents(False)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(150, 312, 471, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_14.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_14.setFont(font)
        self.label_14.setText(b[2])
        self.label_14.setScaledContents(False)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(150, 448, 431, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_15.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_15.setFont(font)
        self.label_15.setText(b[3])
        self.label_15.setScaledContents(False)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(150, 584, 481, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_16.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_16.setFont(font)
        self.label_16.setText(b[4])
        self.label_16.setScaledContents(False)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(660, 176, 481, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_18.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_18.setFont(font)
        self.label_18.setText(r[1])
        self.label_18.setScaledContents(False)
        self.label_18.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(650, 40, 491, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_22.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_22.setFont(font)
        self.label_22.setText(r[0])
        self.label_22.setScaledContents(False)
        self.label_22.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(710, 312, 431, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_23.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_23.setFont(font)
        self.label_23.setText(r[2])
        self.label_23.setScaledContents(False)
        self.label_23.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(690, 448, 451, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_24.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_24.setFont(font)
        self.label_24.setText(r[3])
        self.label_24.setScaledContents(False)
        self.label_24.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(700, 584, 441, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_25.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(36)
        self.label_25.setFont(font)
        self.label_25.setText(r[4])
        self.label_25.setScaledContents(False)
        self.label_25.setAlignment(QtCore.Qt.AlignRight
                                   | QtCore.Qt.AlignTrailing
                                   | QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(220, 123, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_19.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[b[0]]][0] * 100, 2)) +
            '%')
        self.label_19.setScaledContents(False)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(220, 259, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_20.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_20.setFont(font)
        self.label_20.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[b[1]]][1] * 100, 2)) +
            '%')
        self.label_20.setScaledContents(False)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(220, 395, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_21.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[b[2]]][2] * 100, 2)) +
            '%')
        self.label_21.setScaledContents(False)
        self.label_21.setObjectName("label_21")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(220, 531, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_26.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_26.setFont(font)
        self.label_26.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[b[3]]][3] * 100, 2)) +
            '%')
        self.label_26.setScaledContents(False)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(220, 667, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_27.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_27.setFont(font)
        self.label_27.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[b[4]]][4] * 100, 2)) +
            '%')
        self.label_27.setScaledContents(False)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(875, 124, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_28.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_28.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[r[0]]][0] * 100, 2)) +
            '%')
        self.label_28.setScaledContents(False)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(875, 257, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_29.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_29.setFont(font)
        self.label_29.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_29.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[r[1]]][1] * 100, 2)) +
            '%')
        self.label_29.setScaledContents(False)
        self.label_29.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(875, 395, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_30.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_30.setFont(font)
        self.label_30.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_30.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[r[2]]][2] * 100, 2)) +
            '%')
        self.label_30.setScaledContents(False)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(875, 533, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_31.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_31.setFont(font)
        self.label_31.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_31.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[r[3]]][3] * 100, 2)) +
            '%')
        self.label_31.setScaledContents(False)
        self.label_31.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(875, 666, 221, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_32.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(18)
        self.label_32.setFont(font)
        self.label_32.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_32.setText(
            "分路胜率：" + str(round(pos_win_rate[heroname[r[4]]][4] * 100, 2)) +
            '%')
        self.label_32.setScaledContents(False)
        self.label_32.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft
                                   | QtCore.Qt.AlignVCenter)
        self.label_32.setObjectName("label_32")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(490, 510, 300, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_17.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(28)
        self.label_17.setFont(font)
        self.label_17.setText("预测胜方：" + str(胜方) + "\n胜率：" +
                              str(round(胜率 * 100, 2)) + "%")
        self.label_17.setScaledContents(False)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(400, 10, 480, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(177, 136, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText,
                         brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText,
                         brush)
        self.label_33.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(24)
        self.label_33.setFont(font)
        self.label_33.setText("参考比赛场数：" + str(len(matchdata)) + "\n游戏版本：" +
                              str(versions['v']))
        self.label_33.setScaledContents(False)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")

        self.shut = QtWidgets.QPushButton(self.centralwidget)
        self.shut.setGeometry(QtCore.QRect(1240, 0, 41, 31))
        self.shut.setText("")
        self.shut.setShortcut("")
        self.shut.setCheckable(False)
        self.shut.setAutoDefault(False)
        self.shut.setFlat(True)
        self.shut.setObjectName("shut")
        self.shut_2 = QtWidgets.QPushButton(self.centralwidget)
        self.shut_2.setGeometry(QtCore.QRect(1172, 2, 41, 31))
        self.shut_2.setText("")
        self.shut_2.setShortcut("")
        self.shut_2.setCheckable(False)
        self.shut_2.setAutoDefault(False)
        self.shut_2.setFlat(True)
        self.shut_2.setObjectName("shut_2")
        self.shut_3 = QtWidgets.QPushButton(self.centralwidget)
        self.shut_3.setGeometry(QtCore.QRect(429, 670, 104, 31))
        self.shut_3.setText("")
        self.shut_3.setShortcut("")
        self.shut_3.setCheckable(False)
        self.shut_3.setAutoDefault(False)
        self.shut_3.setFlat(True)
        self.shut_3.setObjectName("shut_3")
        self.shut_3.setToolTip("退出")

        self.shut.clicked.connect(MainWindow.close)
        self.shut_3.clicked.connect(MainWindow.close)
        self.shut_2.clicked.connect(MainWindow.showMinimized)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setEnabled(False)
        self.statusbar.setMaximumSize(QtCore.QSize(0, 0))
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate(u"Visual Prediction Data", u"Visual Prediction Data"))
        MainWindow.resize(1280, 720)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)


def disp():  # 可视化函数
    if __name__ == '__main__':
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)    # 高清屏适配
        # app = QApplication(sys.argv)
        # font = QtGui.QFont("Microsoft YaHei")
        # pointsize = font.pointSize()
        # font.setPixelSize(pointsize * 90 / 72)
        # app.setFont(font)
        app = QApplication(sys.argv)    # QApplication Contribution
        MainWindow = QMainWindow()  # QMainWindow Contribution
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()   # 显示窗口
        sys.exit(app.exec_())   # 循环窗口


my_api = 'There is no need for this unless u wanna retrieve new data, but I do not advise u do so'  # Riot开发者数据获取Api

lol_watcher = riotwatcher.LolWatcher(my_api)    # LOlWatcher调用
region = 'kr'   # 国服数据不被拳头官方收录，韩服数据一定程度上代表全球数据
Region = 'asia'  # 区域
herodata = {}   # 英雄ID——名称字典初始化
heroes = {}     # 英雄数据字典初始化
heroname = {}   # 英雄名称——ID字典初始化
match4rec = []  # 用于记录的比赛数据
summoner4srch = []  # 用于搜索的召唤师

if False:   # 已有离线数据，在线数据获取关闭
    versions = lol_watcher.data_dragon.versions_for_region(region)  # 获取游戏版本
    champions_version = versions['n']['champion']   # 获取英雄版本
    heroes = lol_watcher.data_dragon.champions(champions_version)   # 获取英雄数据
    for i in tqdm(heroes['data']):  # 遍历英雄数据
        herodata[heroes['data'][i]['key']] = {
            'name': heroes['data'][i]['name'],
            'position': ''
        }   # 更新英雄ID——名称
    for i in herodata:
        heroname[herodata[i]['name']] = eval(i)  # 更新英雄名称——ID
    # open("./heronames.txt",'w+').write(str(heroname))
    summoner_name = 'Hide on bush'  # 初始召唤师名称
    summoner_faker = lol_watcher.summoner.by_name(
        region, summoner_name)    # 初始召唤师数据
    matchlist_faker = lol_watcher.match.matchlist_by_puuid(
        'asia', summoner_faker['puuid'], 0, 10)  # 初始召唤师比赛记录
    # print(match_faker)
    match_1 = lol_watcher.match.by_id(
        'asia', matchlist_faker[0])   # 获取初始召唤师最近的第一场比赛

    match4rec.append(matchlist_faker[0])    # 进入记录比赛列表

    # 将该局比赛所有召唤师放入搜索用召唤师列表
    summoner4srch += match_1['metadata']['participants']
else:
    herodata = eval(
        open(os.path.join(sys.path[0]+"\\Resource", "herodata.txt"), 'r').read())    # 从文件获取英雄ID——名称字典
    heroname = eval(
        open(os.path.join(sys.path[0]+"\\Resource", "heroname.txt"), "r").read())    # 从文件获取英雄名称——ID字典
    versions = eval(
        open(os.path.join(sys.path[0]+"\\Resource", "versions.txt"), 'r').read())    # 从文件获取游戏版本

# print(summoner4srch, '\n')
while False:  # len(summoner4srch) <= 10:
    for temp in range(len(summoner4srch)):      # 遍历搜索用召唤师列表
        tempmatchlist = lol_watcher.match.matchlist_by_puuid(
            Region, summoner4srch[temp], 0, 10)  # 获取该召唤师最近比赛列表
        tempmatchid = tempmatchlist[9]  # 获取每个召唤师的最近第九场比赛，以保证随机性
        tempmatch = lol_watcher.match.by_id(Region, tempmatchid)    # 获取该场比赛数据
        for i in tempmatch['metadata']['participants']:  # 遍历参与该场比赛的召唤师
            if i is not summoner4srch[temp]:    # 排除已在列表中的召唤师
                summoner4srch.append(i)  # 将新召唤师加入搜索用召唤师列表
# summoner4srch = eval(open("./userdata.txt", 'r').read())
# print(summoner4srch, '\n')
if False:   # 已有离线数据，在线数据获取关闭
    jsq = 0  # 初始化计数器
    for i in range(100):
        jsq += 1
        jsq %= 10
        tempmatchlist = lol_watcher.match.matchlist_by_puuid(
            Region, summoner4srch[i], jsq, 1)
        match4rec.append(tempmatchlist[0])
        # print(tempmatchlist[0], ',', end='')
# match4rec = eval(open("./matchid.txt", 'r').read())
# print(match4rec)

matchdata = {}
if False:   # 已有离线数据，在线数据获取关闭
    for i in match4rec:  # 遍历记录比赛列表
        tempmatch = lol_watcher.match.by_id(Region, i)  # 获取该场比赛数据
        B = []  # 初始化蓝方列表
        R = []  # 初始化红方列表
        for j in range(5):  # 获取蓝方英雄数据
            B.append(tempmatch['info']['participants']
                     [j]['championId'])    # 加入蓝方列表
        for j in range(5, 10):  # 获取红方英雄数据
            R.append(tempmatch['info']['participants']
                     [j]['championId'])    # 加入红方列表
        WL = ''  # 初始化胜利方
        if tempmatch['info']['participants'][0]['win']:  # 如果蓝方获胜
            WL = 'B'    # 胜利方赋值为B
        else:
            WL = 'R'    # 胜利方赋值为R
        tempmatchdata = {}  # 初始化临时比赛数据字典
        tempmatchdata['B'] = B  # 记录蓝方英雄数据
        tempmatchdata['R'] = R  # 记录红方英雄数据
        tempmatchdata['res'] = WL   # 记录胜方
        matchdata[i] = tempmatchdata    # 将临时数据字典加入总比赛字典
matchdata = eval(
    open(os.path.join(sys.path[0]+"\\Resource", "matchdata.txt"), 'r').read())  # 从文件获取比赛数据字典
# print(matchdata)


def counterpoint_analyse(pos):  # 对位胜率分析
    if pos == 0:
        cpos = '上单'
    if pos == 1:
        cpos = '打野'
    if pos == 2:
        cpos = '中单'
    if pos == 3:
        cpos = '下路'
    if pos == 4:
        cpos = '辅助'   # 确定分路
    current_position_sumup = {}  # 初始化当前分路英雄总比赛场数字典
    current_position_win_sumup = {}  # 初始化当前分路英雄总胜场字典
    # 初始化两英雄在该分路对位总比赛场数列表
    counterpoint_sumup = [[0 for i in range(10000)] for i in range(10000)]
    counterpoint_win_sumup = [
        [0 for i in range(10000)] for i in range(10000)]  # 初始化两英雄在该分路对位总胜场列表
    for matchnum in tqdm(list(matchdata.keys()),
                         desc="初始化比赛" + cpos + "数据",
                         file=sys.stdout):  # 遍历比赛数据字典
        current_position_sumup[matchdata[matchnum]['B']
                               [pos]] = current_position_sumup.setdefault(
                                   matchdata[matchnum]['B'][pos], 0) + 1    # 蓝方该分路所用英雄比赛场数+1
        current_position_sumup[matchdata[matchnum]['R']
                               [pos]] = current_position_sumup.setdefault(
                                   matchdata[matchnum]['R'][pos], 0) + 1    # 红方该分路所用英雄比赛场数+1
        if matchdata[matchnum]['res'] == 'B':   # 如果胜利方为蓝方
            current_position_win_sumup[matchdata[matchnum]['B'][
                pos]] = current_position_win_sumup.setdefault(
                    matchdata[matchnum]['B'][pos], 0) + 1   # 蓝方该分路所用英雄胜场+1
        else:   # 否则
            current_position_win_sumup[matchdata[matchnum]['R'][
                pos]] = current_position_win_sumup.setdefault(
                    matchdata[matchnum]['R'][pos], 0) + 1   # 红方该分路所用英雄胜场+1
        try:
            counterpoint_sumup[matchdata[matchnum]['B'][pos]][
                matchdata[matchnum]['R'][pos]] += 1
            counterpoint_sumup[matchdata[matchnum]['R'][pos]][
                matchdata[matchnum]['B'][pos]] += 1  # 该分路英雄对位总场数+1
            counterpoint_win_sumup[matchdata[matchnum]['B'][pos]][
                matchdata[matchnum]['R'][pos]] += (
                    matchdata[matchnum]['res'] == 'B')
            counterpoint_win_sumup[matchdata[matchnum]['R'][pos]][
                matchdata[matchnum]['B'][pos]] += (
                    matchdata[matchnum]['res'] == 'R')  # 该分路胜利方英雄对位胜场+1
        except:  # debug
            print(matchdata[matchnum]['B'][pos], matchdata[matchnum]['R'][pos])
            matchdata.pop(matchnum)
        # print("current_position_sumup:", current_position_sumup, '\n')
        # print("current_position_win_sumup", current_position_win_sumup)
    for i in tqdm(herodata.keys(),
                  desc="初始化" + cpos + "英雄数据",
                  file=sys.stdout,
                  leave=False):  # 输出分路英雄对位数据
        temp = current_position_sumup.setdefault(eval(i), 0)
        if temp:    # 判断是否有该英雄比赛记录
            print(herodata[i]['name'],
                  '的',
                  cpos,
                  '胜率：',
                  current_position_win_sumup.setdefault(eval(i), 0) / temp *
                  100,
                  '%',
                  sep='',
                  file=open(os.path.join(
                      sys.path[0]+"\\Resource", "data.txt"), 'a+'),
                  end='')   # 输出该英雄在该分路的胜率，并输出到同目录下data.txt文件中
            pos_win_rate[eval(i)][pos] = current_position_win_sumup.setdefault(
                eval(i), 0) / temp  # 输出该英雄在该分路的胜率
        for j in herodata.keys():
            temp = counterpoint_sumup[eval(i)][eval(j)]
            if temp:    # 判断是否有该英雄比赛记录
                counter_win_rate[eval(i)][eval(
                    j)] = counterpoint_win_sumup[eval(i)][eval(j)] / temp   # 记录该英雄在该分路对位过的所有英雄的胜率
                print(herodata[i]['name'],
                      '与',
                      herodata[j]['name'],
                      '对位的胜率：',
                      counterpoint_win_sumup[eval(i)][eval(j)] / temp * 100,
                      '%',
                      sep='',
                      file=open(os.path.join(sys.path[0]+"\\Resource", "counterdata.txt"),
                                'a+'),
                      end='')  # 记录该英雄在该分路对位过的所有英雄的胜率，并输出到同目录下counterdata.txt中
    # print('\n')


def All_data_analyse():
    for matchnum in tqdm(list(matchdata), desc="初始化比赛数据总览", file=sys.stdout):  # 遍历比赛数据
        for i in range(2):  # 遍历红蓝方
            temp = 'B'
            if i:
                temp = 'R'
            for j in range(5):  # 遍历该方英雄
                for_all_match_count[matchdata[matchnum]
                                    [temp][j]] += 1  # 记录英雄总场次
                if temp == matchdata[matchnum]['res']:
                    # 记录英雄胜场
                    for_all_match_win_count[matchdata[matchnum][temp][j]] += 1
    for i in tqdm(list(herodata.keys()),
                  desc="初始化英雄数据总览",
                  file=sys.stdout,
                  leave=False):  # 遍历英雄数据
        if for_all_match_count[eval(i)]:    # 判断是否存在数据
            print(herodata[i]['name'],
                  '的总胜率为',
                  for_all_match_win_count[eval(i)] /
                  for_all_match_count[eval(i)] * 100,
                  '%',
                  sep='',
                  file=open(os.path.join(
                      sys.path[0]+"\\Resource", "data.txt"), 'a+'),
                  end='')   # 记录该英雄总比赛胜率，并输出到同目录下data.txt文件夹中
            all_pos_win_rate[eval(i)] = for_all_match_win_count[eval(
                i)] / for_all_match_count[eval(i)]  # 记录该英雄总比赛胜率


if __name__ == "__main__":
    # multiprocessing.freeze_support()

    # counter_win_rate = multiprocessing.Manager().list()
    # pos_win_rate = multiprocessing.Manager().list()
    # all_pos_win_rate = multiprocessing.Manager().list()
    # for_all_match_count = multiprocessing.Manager().list()
    # for_all_match_win_count = multiprocessing.Manager().list()
    print("开始执行初始化")
    counter_win_rate = [[0 for i in range(1000)] for i in range(1000)]
    pos_win_rate = [[0.00 for i in range(5)] for i in range(1000)]  # 初始化胜率列表
    open(os.path.join(sys.path[0]+"\\Resource",
         "counterdata.txt"), 'w+').write('')
    open(os.path.join(sys.path[0]+"\\Resource",
         "data.txt"), 'w+').write('')  # 初始化输出文件

    for_all_match_count = [0 for i in range(1000)]
    for_all_match_win_count = [0 for i in range(1000)]
    all_pos_win_rate = [0.00 for i in range(1000)]  # 初始化胜率列表

    print("游戏版本：" + str(versions['v']))    # 输出游戏版本

    threadlist = []  # 初始化线程列表
    for i in range(5):  # 多线程
        t = threading.Thread(target=counterpoint_analyse,
                             args=(i, ))   # 新建线程，分析各分路数据
        # t.setDaemon(True)
        t.start()   # 启动线程
        threadlist.append(t)    # 记录该线程
    t = threading.Thread(target=All_data_analyse)   # 新建线程，分析英雄总胜率
    # t.setDaemon(True)
    t.start()   # 启动线程
    threadlist.append(t)    # 记录该线程
    for i in threadlist:
        i.join()    # 阻塞线程，等待线程执行完毕

    # os.system("cls")
    print("初始化完成！\n")
    if True:
        print("请输入双方阵容,输入该英雄的英文名称(参考Head文件夹)\n")
        for i in range(2):
            if not i:
                print("蓝方：")
            else:
                print("红方：")
            for j in range(5):
                tempinput = input(postn[j] + ':')  # 获取各方各分路英雄
                while not heroname.__contains__(tempinput):
                    tempinput = input("不存在此英雄，请重新输入:")
                if not i:
                    b[j] = tempinput
                else:
                    r[j] = tempinput
        bt = 0
        for i in range(5):
            temp = 0.00
            if not counter_win_rate[heroname[b[i]]][heroname[r[i]]]:
                temp = pos_win_rate[heroname[b[i]]][i]
            if not temp:
                temp = all_pos_win_rate[heroname[b[i]]]
            bt += temp  # 胜率累加
        bt /= 5
        print('蓝方获胜的概率为', round(bt * 100, 2), '%', sep='')
        if bt >= 0.5:
            胜方 = '蓝方'
        else:
            胜方 = '红方'
            bt = 1 - bt
        胜率 = bt   # 记录胜率
    disp()  # 可视化
