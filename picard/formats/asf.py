# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
# Copyright (C) 2006-2007 Lukáš Lalinský
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

from picard.file import File
from picard.util import encode_filename
from picard.metadata import Metadata
from mutagen.asf import ASF

class ASFFile(File):
    """ASF (WMA) metadata reader/writer"""
    EXTENSIONS = [".wma"]
    NAME = "Windows Media Audio"

    __TRANS = {
        'album': 'WM/AlbumTitle',
        'title': 'Title',
        'artist': 'Author',
        'albumartist': 'WM/AlbumArtist',
        'date': 'WM/Year',
        'composer': 'WM/Composer',
        # FIXME performer
        'lyricist': 'WM/Writer',
        'conductor': 'WM/Conductor',
        'remixer': 'WM/ModifiedBy',
        # FIXME engineer
        'engineer': 'WM/Producer',
        'grouping': 'WM/ContentGroupDescription',
        'subtitle': 'WM/SubTitle',
        'album_subtitle': 'WM/SetSubTitle',
        'tracknumber': 'WM/TrackNumber',
        'discnumber': 'WM/PartOfSet',
        # FIXME compilation
        'comment:': 'Description',
        'genre': 'WM/Genre',
        'bpm': 'WM/BeatsPerMinute',
        'mood': 'WM/Mood',
        'isrc': 'WM/ISRC',
        'copyright': 'WM/Copyright',
        'lyrics': 'WM/Lyrics',
        # FIXME media, catalognumber, barcode
        'label': 'WM/Publisher',
        'encodedby': 'WM/EncodedBy',
        'albumsort': 'WM/AlbumSortOrder',
        'albumartistsort': 'WM/AlbumArtistSortOrder',
        'artistsort': 'WM/ArtistSortOrder',
        'titlesort': 'WM/TitleSortOrder',
        'musicbrainz_trackid': 'MusicBrainz/Track Id',
        'musicbrainz_albumid': 'MusicBrainz/Album Id',
        'musicbrainz_artistid': 'MusicBrainz/Artist Id',
        'musicbrainz_albumartistid': 'MusicBrainz/Album Artist Id',
        'musicbrainz_trmid': 'MusicBrainz/TRM Id',
        'musicbrainz_discid': 'MusicBrainz/Disc Id',
        'musicip_puid': 'MusicIP/PUID',
        'releasestatus': 'MusicBrainz/Album Status',
        'releasetype': 'MusicBrainz/Album Type',
        'releasecountry': 'MusicBrainz/Album Release Country',
    }
    __RTRANS = dict([(b, a) for a, b in __TRANS.items()])

    def _load(self, filename):
        self.log.debug("Loading file %r", filename)
        file = ASF(encode_filename(filename))
        metadata = Metadata()
        for name, values in file.tags.items():
            if name not in self.__RTRANS:
                continue
            name = self.__RTRANS[name]
            values = filter(bool, map(unicode, values))
            if values:
                metadata[name] = values
        self._info(metadata, file)
        return metadata

    def _save(self, filename, metadata, settings):
        self.log.debug("Saving file %r", filename)
        file = ASF(encode_filename(filename))
        for name, values in metadata.rawitems():
            if name.startswith('lyrics:'):
                name = 'lyrics'
            if name not in self.__TRANS:
                continue
            name = self.__TRANS[name]
            file.tags[name] = map(unicode, values)
        file.save()

    def supports_tag(self, name):
        return name in self.__TRANS
