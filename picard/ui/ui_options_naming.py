# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options_naming.ui'
#
# Created: Sun Jan 13 17:42:15 2008
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NamingOptionsPage(object):
    def setupUi(self, NamingOptionsPage):
        NamingOptionsPage.setObjectName("NamingOptionsPage")
        NamingOptionsPage.resize(QtCore.QSize(QtCore.QRect(0,0,396,519).size()).expandedTo(NamingOptionsPage.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(NamingOptionsPage)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.rename_files = QtGui.QGroupBox(NamingOptionsPage)
        self.rename_files.setCheckable(True)
        self.rename_files.setObjectName("rename_files")

        self.gridlayout = QtGui.QGridLayout(self.rename_files)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName("gridlayout")

        self.windows_compatible_filenames = QtGui.QCheckBox(self.rename_files)
        self.windows_compatible_filenames.setObjectName("windows_compatible_filenames")
        self.gridlayout.addWidget(self.windows_compatible_filenames,4,0,1,2)

        self.ascii_filenames = QtGui.QCheckBox(self.rename_files)
        self.ascii_filenames.setObjectName("ascii_filenames")
        self.gridlayout.addWidget(self.ascii_filenames,5,0,1,2)

        self.va_file_naming_format = QtGui.QLineEdit(self.rename_files)
        self.va_file_naming_format.setObjectName("va_file_naming_format")
        self.gridlayout.addWidget(self.va_file_naming_format,3,0,1,1)

        self.va_file_naming_format_default = QtGui.QPushButton(self.rename_files)
        self.va_file_naming_format_default.setObjectName("va_file_naming_format_default")
        self.gridlayout.addWidget(self.va_file_naming_format_default,3,1,1,1)

        self.file_naming_format_default = QtGui.QPushButton(self.rename_files)
        self.file_naming_format_default.setObjectName("file_naming_format_default")
        self.gridlayout.addWidget(self.file_naming_format_default,1,1,1,1)

        self.file_naming_format = QtGui.QLineEdit(self.rename_files)
        self.file_naming_format.setObjectName("file_naming_format")
        self.gridlayout.addWidget(self.file_naming_format,1,0,1,1)

        self.label_4 = QtGui.QLabel(self.rename_files)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,2,0,1,2)

        self.label_3 = QtGui.QLabel(self.rename_files)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,0,0,1,2)
        self.vboxlayout.addWidget(self.rename_files)

        self.move_files = QtGui.QGroupBox(NamingOptionsPage)
        self.move_files.setCheckable(True)
        self.move_files.setObjectName("move_files")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.move_files)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(2)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label_2 = QtGui.QLabel(self.move_files)
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(2)
        self.hboxlayout.setObjectName("hboxlayout")

        self.move_files_to = QtGui.QLineEdit(self.move_files)
        self.move_files_to.setObjectName("move_files_to")
        self.hboxlayout.addWidget(self.move_files_to)

        self.move_files_to_browse = QtGui.QPushButton(self.move_files)
        self.move_files_to_browse.setObjectName("move_files_to_browse")
        self.hboxlayout.addWidget(self.move_files_to_browse)
        self.vboxlayout1.addLayout(self.hboxlayout)

        self.move_additional_files = QtGui.QCheckBox(self.move_files)
        self.move_additional_files.setObjectName("move_additional_files")
        self.vboxlayout1.addWidget(self.move_additional_files)

        self.move_additional_files_pattern = QtGui.QLineEdit(self.move_files)
        self.move_additional_files_pattern.setObjectName("move_additional_files_pattern")
        self.vboxlayout1.addWidget(self.move_additional_files_pattern)

        self.delete_empty_dirs = QtGui.QCheckBox(self.move_files)
        self.delete_empty_dirs.setObjectName("delete_empty_dirs")
        self.vboxlayout1.addWidget(self.delete_empty_dirs)
        self.vboxlayout.addWidget(self.move_files)

        self.groupBox = QtGui.QGroupBox(NamingOptionsPage)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout1 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(2)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label,0,0,1,2)

        self.example_va_filename = QtGui.QLabel(self.groupBox)

        font = QtGui.QFont()
        font.setItalic(True)
        self.example_va_filename.setFont(font)
        self.example_va_filename.setTextFormat(QtCore.Qt.PlainText)
        self.example_va_filename.setWordWrap(True)
        self.example_va_filename.setObjectName("example_va_filename")
        self.gridlayout1.addWidget(self.example_va_filename,3,0,1,2)

        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5,2,0,1,2)

        self.example_filename = QtGui.QLabel(self.groupBox)

        font = QtGui.QFont()
        font.setItalic(True)
        self.example_filename.setFont(font)
        self.example_filename.setTextFormat(QtCore.Qt.PlainText)
        self.example_filename.setWordWrap(True)
        self.example_filename.setObjectName("example_filename")
        self.gridlayout1.addWidget(self.example_filename,1,0,1,2)

        spacerItem = QtGui.QSpacerItem(301,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem,4,1,1,1)

        self.test_button = QtGui.QPushButton(self.groupBox)
        self.test_button.setObjectName("test_button")
        self.gridlayout1.addWidget(self.test_button,4,0,1,1)
        self.vboxlayout.addWidget(self.groupBox)

        spacerItem1 = QtGui.QSpacerItem(311,20,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)
        self.label_4.setBuddy(self.va_file_naming_format)
        self.label_3.setBuddy(self.file_naming_format)
        self.label_2.setBuddy(self.move_files_to_browse)

        self.retranslateUi(NamingOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(NamingOptionsPage)
        NamingOptionsPage.setTabOrder(self.file_naming_format,self.file_naming_format_default)
        NamingOptionsPage.setTabOrder(self.file_naming_format_default,self.va_file_naming_format)
        NamingOptionsPage.setTabOrder(self.va_file_naming_format,self.va_file_naming_format_default)
        NamingOptionsPage.setTabOrder(self.va_file_naming_format_default,self.windows_compatible_filenames)
        NamingOptionsPage.setTabOrder(self.windows_compatible_filenames,self.ascii_filenames)
        NamingOptionsPage.setTabOrder(self.ascii_filenames,self.move_files_to)
        NamingOptionsPage.setTabOrder(self.move_files_to,self.move_files_to_browse)

    def retranslateUi(self, NamingOptionsPage):
        self.rename_files.setTitle(_("Rename Files"))
        self.windows_compatible_filenames.setText(_("Replace Windows-incompatible characters"))
        self.ascii_filenames.setText(_("Replace non-ASCII characters"))
        self.va_file_naming_format_default.setText(_("Default"))
        self.file_naming_format_default.setText(_("Default"))
        self.label_4.setText(_("Multiple artist file naming format:"))
        self.label_3.setText(_("File naming format:"))
        self.move_files.setTitle(_("Move Files"))
        self.label_2.setText(_("Move tagged files to this directory:"))
        self.move_files_to_browse.setText(_("Browse..."))
        self.move_additional_files.setText(_("Move additional files:"))
        self.delete_empty_dirs.setText(_("Delete empty directories"))
        self.groupBox.setTitle(_("Example"))
        self.label.setText(_("File name:"))
        self.label_5.setText(_("Multiple artist file name:"))
        self.test_button.setText(_("&Preview"))

