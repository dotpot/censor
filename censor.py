#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'dotpot'

import re

class NoKeywordProvidedError(Exception): pass
class BadKeywordProvidedError(Exception): pass
class NonIteratableKeywordsError(Exception): pass
class NoPatternProvidedError(Exception): pass

class Censor:
    """
    Censor is a component which helps to censor any text you want, you just populate censor with keywords or patterns,
    and censor() method will return censored text with mask (default - '*').

    Example:
    from censor import Censor

    censor = Censor()
    censor.add_keyword('shit')
    text = 'hello you little shit'
    censored_text = censor.censor(text)
    --
    censored_text is: 'hello you little ****'

    """
    def __init__(self, mask='*', max_len=None):
        """
        initializes Censor object with default values.
        """
        self._mask = mask
        self._max_len = max_len
        self._keywords = []
        self._patterns = []

    def add_keyword(self, keyword):
        """
        adds provided & non duplicate keyword to Censor core.
        if provided None, NoKeywordProvidedError will be raised.
        all unicode keywords are converted to utf-8 and to lower
        also sorted by length so longer words will be replaced first.
        """
        if keyword is None:
            raise NoKeywordProvidedError('keyword must be provided.')
        if not isinstance(keyword, unicode) and not isinstance(keyword, str):
            raise BadKeywordProvidedError('keyword must be either unicode or a string.')
        if not isinstance(keyword, unicode):
            keyword = keyword.decode('utf-8')

        keyword = re.compile('{0}'.format(keyword), re.IGNORECASE)

        if keyword not in self._keywords:
            self._keywords.append(keyword)
             # sort keywords by length so longer words will be replaced first.
            self._keywords.sort(key = lambda s: -len(s.pattern))
            return keyword.pattern
        return None

    def add_keywords(self, keywords):
        """
        adds all keywords from a provided collection to Censor core.
        keywords must be iterable object, with strings or unicode
        strings as it's elements.
        """
        if keywords is None or not hasattr(keywords, '__iter__'):
            raise NonIteratableKeywordsError('keywords must be iterable object.')

        for keyword in keywords:
            self.add_keyword(keyword)

    def add_pattern(self, pattern):
        """
        add provided & non duplicate pattern to Censor core.
        if provided None, NoKeywordProvidedError will be raised.
        """
        if pattern is None:
            raise NoPatternProvidedError('pattern must be provided.')
        
        pattern = re.compile(pattern)

        if pattern not in self._patterns:
            self._patterns.append(pattern)
            return pattern
        return None

    def _make_mask_re(self, match):
        """
        makes mask for regexp match by it's length
        (or by _max_len if provided).
        """
        return self._mask * (self._max_len or len(match.group(0)))

    def _make_mask(self, word):
        """
        makes mask for word by it's length ( or by _max_len if provided ).
        """
        return self._mask * (self._max_len or len(word))

    def censor(self, text):
        """
        censors text and returns censored version.
        """
        for kw in (self._keywords + self._patterns):
            text = kw.sub(self._make_mask_re, text)
        return text

