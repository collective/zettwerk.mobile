zettwerk.mobile
===============

Apply theme by given hostname(s).


Important
=========

This is a really rough prototype. Do not use in production instances. Also, there is no clean uninstall profile. Just for testing.

Usage
=====

Install zettwerk.mobile via quickinstaller. 
A new control panel entry makes it possible to change settings.

Enter the hostnames on which the mobile theme should be applied. It is also possible to give a own theme name. 
As default, the zettwerk.mobile theme is used.
There is also some settings for "redirecting urls", it works like this:

1) A javascript is installed in portal_javascript
2) This javascript redirects urls starting with 'www' to the url set in the control panel.
3) Redirects works for mobile devices.
4) You can choose if you want to redirect iPads and tablets, too.


Example Setup
=============

1) Point www.mydomain.com to "myplonesite"
2) Point m.mydomain.com   to "myplonesite"
3) Add "m.mydomain" as the first entry in the control panel
4) Leave "iPad" and "tablet" settings off unless you have a good reason
5) Visit www.mydomain.com with you phone. It should redirect to "m.mydomain.com" which has the mobile theme.


