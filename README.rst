Django-firefile
===============

Django helper for saving CSS changes made with Firebug Firefile extension

Requisities
-----------



Installation
------------
    
Download and install::

	git clone https://github.com/k1000/django-firefile.git
	cd firefile
	python setup.py install

or using pip::     

	pip install -e git+https://github.com/k1000/django-firefile.git#egg=firefile


Settings
--------
 
Add to your urls.py::
    
    (r'^firefile/$', 'firefile.views.get_respond'),

Usage
-----

You must be logged as staff member to be able to save changes.

LICENSE
-------

Django-firefile is released under the MIT License. See the _LICENSE file for more
details.

.. _LICENSE: http://github.com/k1000/django-firefile/blob/master/LICENSE
.. _firefile: https://addons.mozilla.org/en-En/firefox/addon/firefile/
.. _Firebug: https://addons.mozilla.org/en-En/firefox/addon/firebug/
