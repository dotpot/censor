#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from censor import Censor, NoKeywordProvidedError, BadKeywordProvidedError, NoPatternProvidedError, NonIteratableKeywordsError

__author__ = 'dotpot'

class TestCensorDefault(unittest.TestCase):
    def setUp(self):
        self._censor = Censor()

    def tearDown(self):
        self._censor = None

    def test_init(self):
        self.assertEquals(0, len(self._censor._keywords))
        self.assertEquals(0, len(self._censor._patterns))
        self.assertEquals('*',self._censor._mask)

    def test_keyword_addition(self):
        kw = 'shit'
        self._censor.add_keyword(kw)

        self.assertEqual(kw, self._censor._keywords[0])

    def test_keywords_addition(self):
        kws = ['shit', 'ass', 'turd']
        self._censor.add_keywords(kws)

        for kw in kws:
            self.assertIn(kw, self._censor._keywords)

    def test_keyword_sorting(self):
        kw1 = 'shit'
        kw2 = 'bastard'

        self._censor.add_keyword(kw1)
        self._censor.add_keyword(kw2)

        self.assertEqual(kw2, self._censor._keywords[0])
        self.assertEqual(kw1, self._censor._keywords[1])

    def test_pattern_addition(self):
        pt = r'[0-9]+'
        self._censor.add_pattern(pt)

        self.assertEqual(pt, self._censor._patterns[0].pattern)

    def test_none_keyword_exception(self):
        self.assertRaises(NoKeywordProvidedError, self._censor.add_keyword, None)

    def test_bad_keyword_exception(self):
        self.assertRaises(BadKeywordProvidedError, self._censor.add_keyword, 0.1)

    def test_none_keywords_exception(self):
        self.assertRaises(NonIteratableKeywordsError, self._censor.add_keywords, None)

    def test_wrong_keywords_exception(self):
        self.assertRaises(NonIteratableKeywordsError, self._censor.add_keywords, 0.1)

    def test_wrong_object_in_keywords_exception(self):
        self.assertRaises(BadKeywordProvidedError, self._censor.add_keywords, ['shit', 0.1])

    def test_none_pattern_exception(self):
        self.assertRaises(NoPatternProvidedError, self._censor.add_pattern, None)

    def test_censor(self):
        self._censor.add_keyword('fuck')
        self._censor.add_keyword('dick')
        self._censor.add_keyword('mother-fucker')

        self._censor.add_pattern(r'[0-9]+')

        text_to_censor = '897546974 hello you fuck, how are you dick and mother-fucker? 125'

        censored_expected = '********* hello you ****, how are you **** and *************? ***'
        censored_actual = self._censor.censor(text_to_censor)

        self.assertEqual(censored_expected, censored_actual)
