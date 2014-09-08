#! /usr/bin/env python

from material import Material

class Audio(Material):
    def __init__(self):
        self.quality = None
        self.sound = None
        self.startPosition = None
        self.durationOfEffectiveSpeech = None
        self.externalReference = None
        self.audioFileFormat = None
        self.transcription = None
