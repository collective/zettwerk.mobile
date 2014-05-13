from plone.app.theming.transform import ThemeTransform

from zope.interface import implements
from zope.component import adapts

from zope.component import queryUtility
from zope.component import getUtility

from zope.interface import Interface
from plone.app.theming.interfaces import IThemingLayer
from plone.app.theming.interfaces import IThemeSettings
from plone.app.theming.utils import getAvailableThemes

from plone.app.theming.utils import applyTheme

from plone.app.theming.utils import compileThemeTransform
from plone.app.theming.utils import prepareThemeParameters
from plone.app.theming.utils import findContext
from plone.app.theming.transform import _Cache

from plone.transformchain.interfaces import ITransform
from plone.registry.interfaces import IRegistry


class MobileThemeTransform(ThemeTransform):

    #implements(ITransform)
    ##adapts(Interface, IThemingLayer)

    order = 8850

    def transformIterable(self, result, encoding):
        """Apply the transform if required
        """
        #import pdb; pdb.set_trace()
        active = False
        registry = getUtility(IRegistry)

        base1 = self.request.get('BASE1')
        _xx_, base1 = base1.split('://', 1)
        host = base1.lower()
        serverPort = self.request.get('SERVER_PORT')

        hostnames = registry[
            'zettwerk.mobile.interfaces.IMobileSettings.hostnames'
        ]
        themename = registry[
            'zettwerk.mobile.interfaces.IMobileSettings.themename'
        ]
        if hostnames:
            for hostname in hostnames or ():
                if host == hostname or \
                   hostname == "http://%s" % (host):
                    active = True

        availableThemes = getAvailableThemes()
        mobile = None
        for item in availableThemes:
            if item.__name__ == themename:
                mobile = item
                active = active and True

        if not active:
            ## return the default theme
            result = super(MobileThemeTransform, self) \
                .transformIterable(result, encoding)
            return result

        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IThemeSettings, False)

        class S(object):
            rules = mobile.rules

            doctype = settings.doctype
            absolutePrefix = settings.absolutePrefix
            readNetwork = settings.readNetwork
            parameterExpressions = settings.parameterExpressions

        fake_settings = S()

        return self.transformIterableWithSettings(result, encoding,
                                                  fake_settings)

    def transformIterableWithSettings(self, result, encoding, settings):
        """ """
        result = self.parseTree(result)
        if result is None:
            return None

        if settings.doctype:
            result.doctype = settings.doctype
            if not result.doctype.endswith('\n'):
                result.doctype += '\n'

        transform = compileThemeTransform(settings.rules,
                                          settings.absolutePrefix,
                                          settings.readNetwork,
                                          settings.parameterExpressions)
        if transform is None:
            return None

        cache = _Cache()
        parameterExpressions = settings.parameterExpressions or {}
        params = prepareThemeParameters(findContext(self.request),
                                        self.request,
                                        parameterExpressions,
                                        cache)

        transformed = transform(result.tree, **params)
        error_log = transform.error_log
        if transformed is not None:
            # Transformed worked, swap content with result
            result.tree = transformed

        return result











        # availableThemes = getAvailableThemes()
        # mobile = None
        # orig_item = None
        # for item in availableThemes:
        #     if item.__name__ == u'zettwerk.mobile':
        #         mobile = item
        #     if item.__name__ == orig_theme:
        #         orig_item = item
        # import pdb; pdb.set_trace()
        # applyTheme(mobile)

        # result = super(MobileThemeTransform, self) \
        #     .transformIterable(result, encoding)

        # applyTheme(orig_item)
