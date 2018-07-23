===============
zettwerk.mobile
===============


Introduction
============

Apply `jQuery Mobile`_ (jquery.mobile library) based themes to Plone.

``zettwerk.mobile`` package contains the following diazo implementations: 

- **zettwerk.mobile theme**, a diazo theme based for *jquery.mobile* library.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``zettwerk.mobiletheming`` package (*will be installed as dependency of this package*)


Features
========

- Provides the *jQuery Mobile* v1.4.2 resources.
- Provides the `Diazo`_ rules for *zettwerk.mobile* theme.
- It's an installable `Plone`_ package.
- After installation from ``Add-ons`` control panel, this package is enabled automatically.


Examples
========

This add-on can be seen in action at the following links:

- `A zettwerk.mobile example integrates with a PhoneGap App`_.
- `A zettwerk.mobile example with ThemeRoller support`_.


Translations
============

This product has been translated into

- German (thanks, Joerg Kubaile aka jkubaile).
- Spanish (thanks, Leonardo J. Caballero G. aka macagua).


Installation
============


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``zettwerk.mobile`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        zettwerk.mobile


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'zettwerk.mobile',
    ],


Enabling
--------

Select and enable the ``zettwerk.mobile`` package (it also installs 
``zettwerk.mobiletheming`` package for url based theme switching) from the 
``Add-ons`` control panel. That's it!


Resources
=========

zettwerk.mobile theme
---------------------

The resources of this theme can be reached through

    ``/++theme++zettwerk.mobile``

There are placed at ``zettwerk.mobile/zettwerk/mobile/static/`` 
directory with following resources files:

::

    _ static
      Provides the resources from "zettwerk.mobile theme".
      _ blank.html
      _ jquery-1.9.1.min.js
      _ jquery.mobile-1.4.2
        _ demos
        _ images
          _ ajax-loader.gif
          _ icons-png
          _ icons-svg
        _ jquery.mobile-1.4.2.css
        _ jquery.mobile-1.4.2.js
        _ jquery.mobile-1.4.2.min.css
        _ jquery.mobile-1.4.2.min.js
        _ jquery.mobile-1.4.2.min.map
        _ jquery.mobile.external-png-1.4.2.css
        _ jquery.mobile.external-png-1.4.2.min.css
        _ jquery.mobile.icons-1.4.2.css
        _ jquery.mobile.icons-1.4.2.min.css
        _ jquery.mobile.inline-png-1.4.2.css
        _ jquery.mobile.inline-png-1.4.2.min.css
        _ jquery.mobile.inline-svg-1.4.2.css
        _ jquery.mobile.inline-svg-1.4.2.min.css
        _ jquery.mobile.structure-1.4.2.css
        _ jquery.mobile.structure-1.4.2.min.css
        _ jquery.mobile.theme-1.4.2.css
        _ jquery.mobile.theme-1.4.2.min.css
        _ themes
          _ images
          _ jquery.mobile.icons.min.css
          _ sunburst.css
          _ sunburst.min.css
      _ manifest.cfg
      _ plone-jquery-mobile.css
      _ preview.png
      _ rules.xml


Usage
=====

Go to the plone control panel to ``Mobile theming`` panel (from ``zettwerk.mobiletheming`` 
package) and set up a hostname, under which the theme should be applied.


Themes
======

There is support for *jquery.mobile* based themes. Just open the themeroller 
and create your theme. Then download and upload it in the ``zettwerk.mobile Themes`` 
Control panel.


Contribute
==========

- Issue Tracker: https://github.com/collective/zettwerk.mobile/issues
- Source Code: https://github.com/collective/zettwerk.mobile
- jQuery Mobile: https://jquerymobile.com/


Support
=======

If you are having issues, please let us know via `our Issue Tracker`_.


License
=======

- The project is licensed under the GPLv2.
- The *jQuery Mobile* project v1.4.2  is licensed under the MIT.


Credits
-------

Really thanks to :

- Jörg Kubaile at zettwerk GmbH. (jk at zettwerk dot com).


Amazing contributions
---------------------

- Leonardo J. Caballero G. aka macagua (leonardocaballero at gmail dot com).

You can find an updated list of package contributors on https://github.com/collective/zettwerk.mobile/contributors

.. _`jQuery Mobile`: https://jquerymobile.com/
.. _`A zettwerk.mobile example integrates with a PhoneGap App`: https://www.youtube.com/watch?v=Q2ID86XkiQQ
.. _`A zettwerk.mobile example with ThemeRoller support`: https://www.youtube.com/watch?v=s7n0IMjltzU
.. _`Plone`: http://plone.org
.. _`Diazo`: http://diazo.org
.. _`our Issue Tracker`: https://github.com/collective/zettwerk.mobile/issues
