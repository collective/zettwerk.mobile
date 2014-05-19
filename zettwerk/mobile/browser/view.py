from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

class JavaScript(BrowserView):
    
    def __call__(self, request=None, response=None):
        """Returns configurations."""
        self.registry = getUtility(IRegistry)
        self.request.response.setHeader("Content-type", "text/javascript")
        
        return """\
            var mobile_domain = "%(hostname)s";
            var ipad = %(ipad)s;
            var other_tablets = %(tablets)s;
            document.write(unescape("%%3Cscript src='"+location.protocol+"//s3.amazonaws.com/me.static/js/me.redirect.min.js' type='text/javascript'%%3E%%3C/script%%3E"));
            """ % {
                'hostname': self.hostname,
                'ipad':     self.ipad,
                'tablets':  self.tablets,
            }
    
    @property
    def hostname(self):
        registry = getUtility(IRegistry)
        hostnames = registry[ 'zettwerk.mobile.interfaces.IMobileSettings.hostnames']
        return hostnames[0] or 'mylocalhost'

    @property
    def tablets(self):
        return self.registry['zettwerk.mobile.interfaces.IMobileSettings.tablets']

    @property
    def ipad(self):
        return self.registry['zettwerk.mobile.interfaces.IMobileSettings.ipad']
