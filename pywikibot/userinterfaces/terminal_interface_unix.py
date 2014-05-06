# -*- coding: utf-8 -*-
#
# (C) Pywikipedia bot team, 2003-2014
#
# Distributed under the terms of the MIT license.
#
__version__ = '$Id$'

from . import terminal_interface_base

unixColors = {
    'default':     chr(27) + '[0m',     # Unix end tag to switch back to default
    'black':       chr(27) + '[30m',    # Black start tag
    'red':         chr(27) + '[31m',    # Red start tag
    'green':       chr(27) + '[32m',    # Green start tag
    'yellow':      chr(27) + '[33m',    # Yellow start tag
    'blue':        chr(27) + '[34m',    # Blue start tag
    'purple':      chr(27) + '[35m',    # Purple start tag (Magenta)
    'aqua':        chr(27) + '[36m',    # Aqua start tag (Cyan)
    'lightgray':   chr(27) + '[37m',    # Light gray start tag (White)
    'gray':        chr(27) + '[90m',    # Gray start tag
    'lightred':    chr(27) + '[91m',    # Light Red tag
    'lightgreen':  chr(27) + '[92m',    # Light Green tag
    'lightyellow': chr(27) + '[93m',    # Light Yellow tag
    'lightblue':   chr(27) + '[94m',    # Light Blue tag
    'lightpurple': chr(27) + '[95m',    # Light Purple tag (Magenta)
    'lightaqua':   chr(27) + '[96m',    # Light Aqua tag (Cyan)
    'white':       chr(27) + '[97m',    # White start tag (Bright White)
}


class UnixUI(terminal_interface_base.UI):
    def printColorized(self, text, targetStream):
        lastColor = None
        totalcount = 0
        for key, value in unixColors.items():
            ckey = '\03{%s}' % key
            totalcount += text.count(ckey)
            text = text.replace(ckey, value)

        if totalcount > 0:
            # just to be sure, reset the color
            text += unixColors['default']

        if hasattr(targetStream, 'encoding'):
            targetStream.write(text)
        else:
            targetStream.write(text.encode(self.encoding, 'replace'))
