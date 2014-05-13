from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory(u"plone")


class IMobileSettings(Interface):
    """A theme, loaded from a resource directory
    """

    hostnames = schema.Tuple(
        title=_('hostnames', 'Hostnames'),
        description=_('hostnames_description',
                      u'Hostnames to apply the mobile theme'),
        value_type=schema.URI(),
        default=(u'http://localhost:8080',),
        )

    themename = schema.TextLine(
        title=_('themename', 'Theme Name'),
        description=_('The name of the mobile theme.'),
        default=u'zettwerk.mobile',
        )
