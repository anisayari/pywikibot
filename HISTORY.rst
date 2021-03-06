Release history
===============

Current release
---------------

* Bugfixes and improvements
* Localisation updates

3.0.20180710
------------

* Enable any LogEntry subclass for each logevent type (T199013)
* Deprecated pagegenerators options -<logtype>log aren't supported any longer (T199013)
* Open RotatingFileHandler with utf-8 encoding (T188231)
* Fix occasional failure of TestLogentries due to hidden namespace (T197506)
* Remove multiple empty sections at once in cosmetic_changes (T196324)
* Fix stub template position by putting it above interwiki comment (T57034)
* Fix handling of API continuation in PropertyGenerator (T196876)
* Use PyMySql as pure-Python MySQL client library instead of oursql, deprecate MySQLdb (T89976, T142021)
* Ensure that BaseBot.treat is always processing a Page object (T196562, T196813)
* Update global bot settings
* New mediawiki projects were provided
* Bugfixes and improvements
* Localisation updates

3.0.20180603
------------

* Move main categories to top in cosmetic_changes
* shell.py always imports pywikibot as default
* New roundrobin_generators in tools
* New BaseBot method "skip_page" to adjust page counting
* Family class is made a singleton class
* New rule 'startcolon' was introduced in textlib
* BaseBot has new methods setup and teardown
* UploadBot got a filename prefix parameter (T170123)
* cosmetic_changes is able to remove empty sections (T140570)
* Pywikibot is following PEP 396 versioning
* pagegenerators AllpagesPageGenerator, CombinedPageGenerator, UnconnectedPageGenerator are deprecated
* Some DayPageGenerator parameters has been renamed
* unicodedata2, httpbin and Flask dependency was removed (T102461, T108068, T178864, T193383)
* New projects were provided
* Bugfixes and improvements
* Documentation updates
* Localisation updates (T194893)
* Translation updates

3.0.20180505
------------

* Enable makepath and datafilepath not to create the directory
* Use API's retry-after value (T144023)
* Provide startprefix parameter for Category.articles() (T74101, T143120)
* Page.put_async() is marked as deprecated (T193494)
* pagegenerators.RepeatingGenerator is marked as deprecated (T192229)
* Deprecate requests-requirements.txt (T193476)
* Bugfixes and improvements
* New mediawiki projects were provided
* Localisation updates

3.0.20180403
------------

* Deprecation warning: support for Python 2.7.2 and 2.7.3 will be dropped (T191192)
* Dropped support for Python 2.6 (T154771)
* Dropped support for Python 3.3 (T184508)
* Bugfixes and improvements
* Localisation updates

3.0.20180304
------------

* Bugfixes and improvements
* Localisation updates

3.0.20180302
------------

* Changed requirements for requests and sseclient
* Bugfixes and improvements
* Localisation updates

3.0.20180204
------------

* Deprecation warning: support for py2.6 and py3.3 will be dropped
* Changed requirements for cryprography, Pillow and pyOpenSSL
* Bugfixes and improvements
* Localisation updates

3.0.20180108
------------

* Maintenance script to download Wikimedia database dump
* Option to auto-create accounts when logging in
* Ship wikimania family file
* Drop battlestarwiki family file
* Bugfixes and improvements
* Localisation updates

3.0.20171212
------------

* Introduce userscripts directory
* Generator settings inside (user-)fixes.py
* BaseUnlinkBot has become part of the framework in specialbots.py
* Decommission of rcstream
* Script files added to https://doc.wikimedia.org/pywikibot/
* Other documentation updates
* Bugfixes and improvements
* Localisation updates

3.0.20170801
------------

* Bugfixes and improvements
* Localisation updates

3.0.20170713
------------

* Implement server side event client EventStreams
* Add thanks log support
* new ndashredir.py script to create hyphenated redirects
* new followlive.py script to flag new articles
* new WbUnknown data type for Wikibase
* Deprecate APISite.newfiles()
* new pagegenerators filter option -titleregexnot
* Inverse of pagegenerators -namespace option
* Bugfixes and improvements
* Localisation updates
* Remove panoramiopicker.py script
* Remove anarchopedia family out of the framework
* CODE_OF_CONDUCT included

3.0.20170521
------------

* Replaced the word 'async' with 'asynchronous' due to python 3.7
* Support for Python 2.6 but higher releases are strictly recommended
* Bugfixes and improvements
* Localisation updates

3.0.20170403
------------

* First major release from master branch
* requests package is mandatory
* Deprecate previous 2.0 branches

2.0rc5
------

* Last stable 2.0 branch

2.0rc4
------

* Remove dependency on pYsearch
* Desupport Python 2.6 for Pywikibot 2.0 release branch

2.0rc3
------

* Bugfixes
* Localisation updates
* i18n: always follow master branch

2.0rc2
------

* Bugfixes and improvements
* Localisation updates


2.0rc1
------

* New scripts patrol.py and piper.py ported from old compat branch
* isbn.py now supports wikibase
* RecentChanges stream (rcstream) support
* Sphinx documentation at https://doc.wikimedia.org/pywikibot/
* Bugfixes and improvements
* Localisation updates

2.0b3
-----

* Bugfixes and improvements

2.0b2
-----

* Bugfixes and improvements

2.0b1
-----

* First stable release branch

1.0 rv 2007-06-19
-----------------
* BeautifulSoup becomes mandatory
* new scripts were added
* new family files were supported
* some scripts were archived

1.0
---

*Sep 26, 2005*

* First PyWikipediaBot framework release
* scripts and libraries for standardizing content
* tools for making minor modifications
* script making interwiki links

