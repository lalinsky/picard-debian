# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options_interface.ui'
#
# Created: Mon Oct 26 21:12:18 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_InterfaceOptionsPage(object):
    def setupUi(self, InterfaceOptionsPage):
        InterfaceOptionsPage.setObjectName("InterfaceOptionsPage")
        InterfaceOptionsPage.resize(287, 200)
        self.vboxlayout = QtGui.QVBoxLayout(InterfaceOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.groupBox_2 = QtGui.QGroupBox(InterfaceOptionsPage)
        self.groupBox_2.setObjectName("groupBox_2")
        self.vboxlayout1 = QtGui.QVBoxLayout(self.groupBox_2)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.toolbar_show_labels = QtGui.QCheckBox(self.groupBox_2)
        self.toolbar_show_labels.setObjectName("toolbar_show_labels")
        self.vboxlayout1.addWidget(self.toolbar_show_labels)
        self.toolbar_multiselect = QtGui.QCheckBox(self.groupBox_2)
        self.toolbar_multiselect.setObjectName("toolbar_multiselect")
        self.vboxlayout1.addWidget(self.toolbar_multiselect)
        self.use_adv_search_syntax = QtGui.QCheckBox(self.groupBox_2)
        self.use_adv_search_syntax.setObjectName("use_adv_search_syntax")
        self.vboxlayout1.addWidget(self.use_adv_search_syntax)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.vboxlayout1.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ui_language = QtGui.QComboBox(self.groupBox_2)
        self.ui_language.setObjectName("ui_language")
        self.horizontalLayout.addWidget(self.ui_language)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.vboxlayout1.addLayout(self.horizontalLayout)
        self.vboxlayout.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(220, 61, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout.addItem(spacerItem1)

        self.retranslateUi(InterfaceOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(InterfaceOptionsPage)

    def retranslateUi(self, InterfaceOptionsPage):
        self.groupBox_2.setTitle(_("Miscellaneous"))
        self.toolbar_show_labels.setText(_("Show text labels under icons"))
        self.toolbar_multiselect.setText(_("Allow selection of multiple directories"))
        self.use_adv_search_syntax.setText(_("Use advanced query syntax"))
        self.label.setText(_("User interface language:"))

