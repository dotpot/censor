#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'dotpot'

import re

class NoKeywordProvidedError(Exception): pass
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
        self._keywords = list()
        self._patterns = list()

    def add_keyword(self, keyword):
        """
        adds provided & non duplicate keyword to Censor core.
        if provided None, NoKeywordProvidedError will be raised.
        all unicode keywords are converted to utf-8 and to lower
        also sorted by length so longer words will be replaced first.
        """
        if keyword is None:
            raise NoKeywordProvidedError('keyword must be provided.')
        if not isinstance(keyword, unicode):
            keyword = keyword.decode('utf-8')

        keyword = keyword.lower()

        if keyword not in self._keywords:
            self._keywords.append(keyword)
             # sort keywords by length so longer words will be replaced first.
            self._keywords.sort(key = lambda s: -len(s))
            return keyword
        return None

    def add_pattern(self, pattern):
        """
        add provided & non duplicate pattern to Censor core.
        if provided None, NoKeywordProvidedError will be raised.
        """
        if pattern is None:
            raise NoKeywordProvidedError('pattern must be provided.')

        if pattern not in self._patterns:
            self._patterns.append(pattern)
            return pattern
        return None

    def make_mask(self, word):
        """
        makes mask for word by it's length ( or by _max_len if provided ).
        """
        mask = ''
        count = len(word) if self._max_len is None else self._max_len
        for i in range(count): mask += self._mask
        return mask

    def censor(self, text):
        """
        censors text and returns censored version.
        """
        for kw in self._keywords:
            text = text.replace(kw, self.make_mask(kw))
        for pt in self._patterns:
            for m in re.findall(pt, text):
                text = text.replace(m, self.make_mask(m))
        return text

