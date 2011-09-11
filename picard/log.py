# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2007 Lukáš Lalinský
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

from PyQt4 import QtCore
import picard
from picard.util import thread


def _stdout_receiver(prefix, msg):
    print prefix, QtCore.QThread.currentThreadId(), QtCore.QTime.currentTime().toString(), msg


class Log(object):

    def __init__(self):
        self.entries = []
        self.receivers = [_stdout_receiver]
        picard.log.log = self
        picard.log.debug = self.debug
        picard.log.info = self.info
        picard.log.warning = self.warning
        picard.log.error = self.error

    def _message(self, prefix, message, args, kwargs):
        if args:
            message = message % args
        if isinstance(message, unicode):
            message = message.encode("utf-8", "replace")
        self.entries.append((prefix, message))
        for func in self.receivers:
            try:
                func(prefix, message)
            except Exception, e:
                print e

    def add_receiver(self, receiver):
        self.receivers.append(receiver)

    def debug(self, message, *args, **kwargs):
        pass

    def info(self, message, *args, **kwargs):
        thread.proxy_to_main(self._message, "I:", message, args, kwargs)

    def warning(self, message, *args, **kwargs):
        thread.proxy_to_main(self._message, "W:", message, args, kwargs)

    def error(self, message, *args, **kwargs):
        thread.proxy_to_main(self._message, "E:", message, args, kwargs)


class DebugLog(Log):

    def debug(self, message, *args, **kwargs):
        thread.proxy_to_main(self._message, "D:", message, args, kwargs)
