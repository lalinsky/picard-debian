import os.path
import unittest
import shutil
from tempfile import mkstemp
import picard.formats
from PyQt4 import QtCore


class FakeTagger():
    def emit(self, *args):
        pass


class FakeConfig():
    def __init__(self):
        self.setting = {
            'enabled_plugins': '',
            'clear_existing_tags': False,
            'remove_images_from_tags': False,
            'write_id3v1': True,
            'id3v2_encoding': 'utf-8',
            'save_images_to_tags': True,
            'write_id3v23': False,
            'remove_ape_from_mp3': False,
            'remove_id3_from_flac': False
        }


class FormatsTest(unittest.TestCase):

    original = None
    tags = []

    def setUp(self):
        if not self.original:
            return
        fd, self.filename = mkstemp(suffix=os.path.splitext(self.original)[1])
        os.close(fd)
        shutil.copy(self.original, self.filename)
        QtCore.QObject.tagger = FakeTagger()
        QtCore.QObject.config = FakeConfig()

    def tearDown(self):
        if not self.original:
            return
        os.unlink(self.filename)

    def test_simple_tags(self):
        if not self.original:
            return
        for i in self.tags:
            if len(i) == 3:
                n, v, e = i
            else:
                n, v = i
                e = v
            f = picard.formats.open(self.filename)
            f._load()
            f.metadata[n] = v
            f.save()
            f = picard.formats.open(self.filename)
            f._load()
            self.assertEqual(f.metadata.getall(n), e, '%s: %r != %r' % (n, f.metadata.getall(n), e))


class FLACTest(FormatsTest):
    original = os.path.join('test', 'data', 'test.flac')
    tags = [
        ('album', ['Foo', 'Bar']),
        ('album', ['1']),
        ('title', ['Foo']),
        ('artist', ['Foo']),
        ('albumartist', ['Foo']),
        ('date', ['2004-00-00'], ['2004']),
        ('artist', ['Foo']),
        ('composer', ['Foo']),
        ('lyricist', ['Foo']),
        ('conductor', ['Foo']),
        ('performer:guest vocal', ['Foo']),
        ('remixer', ['Foo']),
        ('engineer', ['Foo']),
        ('producer', ['Foo']),
        ('grouping', ['Foo']),
        ('subtitle', ['Foo']),
        ('discsubtitle', ['Foo']),
        ('compilation', ['1']),
        ('comment', ['Foo']),
        ('genre', ['Foo']),
        ('bpm', ['Foo']),
        ('mood', ['Foo']),
        ('isrc', ['Foo']),
        ('copyright', ['Foo']),
        ('lyrics', ['Foo']),
        ('media', ['Foo']),
        ('label', ['Foo']),
        ('catalognumber', ['Foo']),
        ('barcode', ['Foo']),
        ('encodedby', ['Foo']),
        ('albumsort', ['Foo']),
        ('albumartistsort', ['Foo']),
        ('artistsort', ['Foo']),
        ('titlesort', ['Foo']),
        ('musicbrainz_trackid', ['Foo']),
        ('musicbrainz_albumid', ['Foo']),
        ('musicbrainz_artistid', ['Foo']),
        ('musicbrainz_albumartistid', ['Foo']),
        ('musicbrainz_trmid', ['Foo']),
        ('musicbrainz_discid', ['Foo']),
        ('musicip_puid', ['Foo']),
        ('releasestatus', ['Foo']),
        ('releasetype', ['Foo']),
    ]


class MP3Test(FormatsTest):
    original = os.path.join('test', 'data', 'test.mp3')
    tags = [
        ('album', ['Foo', 'Bar']),
        ('album', ['1']),
        ('title', ['Foo']),
        ('artist', ['Foo']),
        ('albumartist', ['Foo']),
        ('date', ['2004-00-00']),
        ('artist', ['Foo']),
        ('composer', ['Foo']),
        ('lyricist', ['Foo']),
        ('conductor', ['Foo']),
        ('performer:guest vocal', ['Foo']),
        ('remixer', ['Foo']),
        ('engineer', ['Foo']),
        ('producer', ['Foo']),
        ('grouping', ['Foo']),
        ('subtitle', ['Foo']),
        ('discsubtitle', ['Foo']),
        ('compilation', ['1']),
        #('comment', ['Foo']),
        ('genre', ['Foo']),
        ('bpm', ['Foo']),
        ('mood', ['Foo']),
        ('isrc', ['Foo']),
        ('copyright', ['Foo']),
        # TODO
        ('lyrics', ['Foo'], []),
        ('media', ['Foo']),
        ('label', ['Foo']),
        ('catalognumber', ['Foo']),
        ('barcode', ['Foo']),
        ('encodedby', ['Foo']),
        ('albumsort', ['Foo']),
        ('albumartistsort', ['Foo']),
        ('artistsort', ['Foo']),
        ('titlesort', ['Foo']),
        ('musicbrainz_trackid', ['Foo']),
        ('musicbrainz_albumid', ['Foo']),
        ('musicbrainz_artistid', ['Foo']),
        ('musicbrainz_albumartistid', ['Foo']),
        ('musicbrainz_trmid', ['Foo']),
        ('musicbrainz_discid', ['Foo']),
        ('musicip_puid', ['Foo']),
        ('releasestatus', ['Foo']),
        ('releasetype', ['Foo']),
    ]


class OggVorbisTest(FormatsTest):
    original = os.path.join('test', 'data', 'test.ogg')
    tags = [
        ('album', ['Foo', 'Bar']),
        ('album', ['1']),
        ('title', ['Foo']),
        ('artist', ['Foo']),
        ('albumartist', ['Foo']),
        ('date', ['2004-00-00'], ['2004']),
        ('artist', ['Foo']),
        ('composer', ['Foo']),
        ('lyricist', ['Foo']),
        ('conductor', ['Foo']),
        ('performer:guest vocal', ['Foo']),
        ('remixer', ['Foo']),
        ('engineer', ['Foo']),
        ('producer', ['Foo']),
        ('grouping', ['Foo']),
        ('subtitle', ['Foo']),
        ('discsubtitle', ['Foo']),
        ('compilation', ['1']),
        ('comment', ['Foo']),
        ('genre', ['Foo']),
        ('bpm', ['Foo']),
        ('mood', ['Foo']),
        ('isrc', ['Foo']),
        ('copyright', ['Foo']),
        ('lyrics', ['Foo']),
        ('media', ['Foo']),
        ('label', ['Foo']),
        ('catalognumber', ['Foo']),
        ('barcode', ['Foo']),
        ('encodedby', ['Foo']),
        ('albumsort', ['Foo']),
        ('albumartistsort', ['Foo']),
        ('artistsort', ['Foo']),
        ('titlesort', ['Foo']),
        ('musicbrainz_trackid', ['Foo']),
        ('musicbrainz_albumid', ['Foo']),
        ('musicbrainz_artistid', ['Foo']),
        ('musicbrainz_albumartistid', ['Foo']),
        ('musicbrainz_trmid', ['Foo']),
        ('musicbrainz_discid', ['Foo']),
        ('musicip_puid', ['Foo']),
        ('releasestatus', ['Foo']),
        ('releasetype', ['Foo']),
    ]


class MP4VorbisTest(FormatsTest):
    original = os.path.join('test', 'data', 'test.m4a')
    tags = [
        ('album', ['Foo', 'Bar']),
        ('album', ['1']),
        ('title', ['Foo']),
        ('artist', ['Foo']),
        ('albumartist', ['Foo']),
        ('date', ['2004-00-00']),
        ('artist', ['Foo']),
        ('composer', ['Foo']),
        ('grouping', ['Foo']),
        ('compilation', ['1']),
        ('musicbrainz_trackid', ['Foo']),
        ('musicbrainz_albumid', ['Foo']),
        ('musicbrainz_artistid', ['Foo']),
        ('musicbrainz_albumartistid', ['Foo']),
        ('musicbrainz_trmid', ['Foo']),
        ('musicbrainz_discid', ['Foo']),
        ('musicip_puid', ['Foo']),
        ('releasestatus', ['Foo']),
        ('releasetype', ['Foo']),
        ('encodedby', ['Foo']),
        ('lyrics', ['Foo']),
        ('copyright', ['Foo']),
    ]


class WavPackTest(FormatsTest):
    original = os.path.join('test', 'data', 'test.wv')
    tags = [
        ('album', ['Foo', 'Bar']),
        ('album', ['1']),
        ('title', ['Foo']),
        ('artist', ['Foo']),
        ('albumartist', ['Foo']),
        ('date', ['2004-00-00'], ['2004']),
        ('artist', ['Foo']),
        ('composer', ['Foo']),
        ('lyricist', ['Foo']),
        ('conductor', ['Foo']),
        ('performer:guest vocal', ['Foo']),
        ('remixer', ['Foo']),
        ('engineer', ['Foo']),
        ('producer', ['Foo']),
        ('grouping', ['Foo']),
        ('subtitle', ['Foo']),
        ('discsubtitle', ['Foo']),
        ('compilation', ['1']),
        ('comment', ['Foo']),
        ('genre', ['Foo']),
        ('bpm', ['Foo']),
        ('mood', ['Foo']),
        ('isrc', ['Foo']),
        ('copyright', ['Foo']),
        ('lyrics', ['Foo']),
        ('media', ['Foo']),
        ('label', ['Foo']),
        ('catalognumber', ['Foo']),
        ('barcode', ['Foo']),
        ('encodedby', ['Foo']),
        ('albumsort', ['Foo']),
        ('albumartistsort', ['Foo']),
        ('artistsort', ['Foo']),
        ('titlesort', ['Foo']),
        ('musicbrainz_trackid', ['Foo']),
        ('musicbrainz_albumid', ['Foo']),
        ('musicbrainz_artistid', ['Foo']),
        ('musicbrainz_albumartistid', ['Foo']),
        ('musicbrainz_trmid', ['Foo']),
        ('musicbrainz_discid', ['Foo']),
        ('musicip_puid', ['Foo']),
        ('releasestatus', ['Foo']),
        ('releasetype', ['Foo']),
    ]


class TestCoverArt(unittest.TestCase):

    def _set_up(self, original):
        fd, self.filename = mkstemp(suffix=os.path.splitext(original)[1])
        os.close(fd)
        shutil.copy(original, self.filename)
        QtCore.QObject.tagger = FakeTagger()
        QtCore.QObject.config = FakeConfig()

    def _tear_down(self):
        os.unlink(self.filename)

    def test_mp3(self):
        self._test_cover_art(os.path.join('test', 'data', 'test.mp3'))

    def test_mp4(self):
        self._test_cover_art(os.path.join('test', 'data', 'test.m4a'))

    def _test_cover_art(self, filename):
        self._set_up(filename)
        try:
            f = picard.formats.open(self.filename)
            f.metadata.clear()
            f.metadata.add_image("image/jpeg", "JFIFfoobar")
            f.save()
            f = picard.formats.open(self.filename)
            f._load()
            self.assertEqual(f.metadata.images[0][0], "image/jpeg")
            self.assertEqual(f.metadata.images[0][1], "JFIFfoobar")
            f = picard.formats.open(self.filename)
            f.metadata.clear()
            f.metadata.add_image("image/png", "PNGfoobar")
            f.save()
            f = picard.formats.open(self.filename)
            f._load()
            self.assertEqual(f.metadata.images[0][0], "image/png")
            self.assertEqual(f.metadata.images[0][1], "PNGfoobar")
        finally:
            self._tear_down()
