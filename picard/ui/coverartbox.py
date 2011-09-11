# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2006 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

from PyQt4 import QtCore, QtGui
from picard.util import webbrowser2
from picard.const import AMAZON_STORE_ASSOCIATE_IDS


class ActiveLabel(QtGui.QLabel):
    """Clickable QLabel."""

    def __init__(self, active=True, *args):
        QtGui.QLabel.__init__(self, *args)
        self.setActive(active)

    def setActive(self, active):
        self.active = active
        if self.active:
            self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        else:
            self.setCursor(QtGui.QCursor())

    def mouseReleaseEvent(self, event):
        if self.active:
            self.emit(QtCore.SIGNAL("clicked()"))


class CoverArtBox(QtGui.QGroupBox):

    def __init__(self, parent):
        QtGui.QGroupBox.__init__(self, " ")
        self.layout = QtGui.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins (7,7,0,0)
        # Kills off any borders
        self.setStyleSheet('''QGroupBox{background-color:none;border:1px;}''')
        self.setFlat(True)
        self.asin = None
        self.data = None
        self.shadow = QtGui.QPixmap(":/images/CoverArtShadow.png")
        self.coverArt = ActiveLabel(False, parent)
        self.coverArt.setPixmap(self.shadow)
        self.coverArt.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        self.connect(self.coverArt, QtCore.SIGNAL("clicked()"), self.open_amazon)
        self.layout.addWidget(self.coverArt, 0)
        self.setLayout(self.layout)
        

    def show(self):
        self.__set_data(self.data, True)
        QtGui.QGroupBox.show(self)

    def __set_data(self, data, force=False):
        if not force and self.data == data:
            return

        self.data = data
        if not force and self.isHidden():
            return

        cover = self.shadow
        if self.data:
            pixmap = QtGui.QPixmap(121, 121)
            format = self.data[1] == "image/png" and "PNG" or "JPG"
            if pixmap.loadFromData(self.data[1], format):
                cover = QtGui.QPixmap(self.shadow)
                pixmap = pixmap.scaled(121,121 , QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
                painter = QtGui.QPainter(cover)
                painter.drawPixmap(1, 1, pixmap)
                painter.end()
        self.coverArt.setPixmap(cover)

    def set_metadata(self, metadata):
        data = None
        if metadata and metadata.images:
            data = metadata.images[0]
        self.__set_data(data)
        if metadata:
            asin = metadata.get("asin", None)
        else:
            asin = None
        if asin != self.asin:
            if asin:
                self.coverArt.setActive(True)
                self.coverArt.setToolTip(_(u"Buy the album on Amazon"))
            else:
                self.coverArt.setActive(False)
                self.coverArt.setToolTip("")
            self.asin = asin

    def open_amazon(self):
        # TODO: make this configurable
        store = "amazon.com"
        url = "http://%s/exec/obidos/ASIN/%s/%s?v=glance&s=music" % (
            store, self.asin, AMAZON_STORE_ASSOCIATE_IDS[store])
        webbrowser2.open(url)

