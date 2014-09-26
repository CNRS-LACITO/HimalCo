#! /usr/bin/env python

from startup import *
from resources.audio import Audio

## Test Audio class

class TestAudioFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an Audio object
        self.audio = Audio()

    def tearDown(self):
        # Release instantiated objects
        del self.audio

    def test_init(self):
        self.assertIsNone(self.audio.mediaType)
        self.assertIsNone(self.audio.fileName)
        self.assertIsNone(self.audio.author)
        self.assertIsNone(self.audio.quality)
        self.assertIsNone(self.audio.sound)
        self.assertIsNone(self.audio.startPosition)
        self.assertIsNone(self.audio.durationOfEffectiveSpeech)
        self.assertIsNone(self.audio.externalReference)
        self.assertIsNone(self.audio.audioFileFormat)
        self.assertIsNone(self.audio.transcription)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAudioFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
