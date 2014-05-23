from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import directlyProvides
from zope.i18nmessageid import MessageFactory

from plone.app.theming import utils 


_ = MessageFactory('zettwerk.mobile')
 



import Globals

import pkg_resources

from StringIO import StringIO
from ConfigParser import SafeConfigParser

from urlparse import urlsplit

from lxml import etree
 

from zope.component import getUtility
from zope.component import queryUtility
from zope.component import queryMultiAdapter
from zope.globalrequest import getRequest

from plone.subrequest import subrequest

from plone.resource.interfaces import IResourceDirectory
from plone.resource.utils import queryResourceDirectory
from plone.resource.utils import cloneResourceDirectory
from plone.resource.manifest import getManifest
from plone.resource.manifest import extractManifestFromZipFile
from plone.resource.manifest import getAllResources
from plone.resource.manifest import getZODBResources
from plone.resource.manifest import MANIFEST_FILENAME

from plone.registry.interfaces import IRegistry

from plone.i18n.normalizer.interfaces import IURLNormalizer

from plone.app.theming.interfaces import THEME_RESOURCE_NAME
from plone.app.theming.interfaces import MANIFEST_FORMAT
from plone.app.theming.interfaces import RULE_FILENAME
from plone.app.theming.interfaces import IThemeSettings

from plone.app.theming.theme import Theme
 

from Products.PageTemplates.Expressions import getEngine
from Products.CMFPlone.utils import safe_unicode




def getPortal():
    """Return the portal object
        """
    request = getRequest()
    context = findContext(request)
    portalState = queryMultiAdapter((context, request), name=u"plone_portal_state")
    if portalState is None:
        return None
    return portalState.portal()


def findContext(request):
    """Find the context from the request
        """
    published = request.get('PUBLISHED', None)
    context = getattr(published, '__parent__', None)
    if context is None:
        context = request.PARENTS[0]
    return context


def expandAbsolutePrefix(prefix):
    """Prepend the Plone site URL to the prefix if it starts with /
        """
    if not prefix or not prefix.startswith('/'):
        return prefix
    portal = getPortal()
    if portal is None:
        return ''
    path = portal.absolute_url_path()
    if path and path.endswith('/'):
        path = path[:-1]
    return path + prefix


def getOrCreatePersistentResourceDirectory():
    """Obtain the 'theme' persistent resource directory, creating it if
        necessary.
        """
    
    persistentDirectory = getUtility(IResourceDirectory, name="persistent")
    if THEME_RESOURCE_NAME not in persistentDirectory:
        persistentDirectory.makeDirectory(THEME_RESOURCE_NAME)
    
    return persistentDirectory[THEME_RESOURCE_NAME]


def createExpressionContext(context, request):
    """Create an expression context suitable for evaluating parameter
        expressions.
        """
    
    contextState = queryMultiAdapter((context, request), name=u"plone_context_state")
    portalState = queryMultiAdapter((context, request), name=u"plone_portal_state")
                                                                     
    data = {'context': context,
             'request': request,
             'portal': portalState.portal(),
            'context_state': contextState,
             'portal_state': portalState,
              'nothing': None,}
                                                                     
    return getEngine().getContext(data)


def compileExpression(text):
    """Compile the given expression. The returned value is suitable for
        caching in a volatile attribute
        """
    return getEngine().compile(text.strip())


def isValidThemeDirectory(directory):
    """Determine if the given plone.resource directory is a valid theme
        directory
        """
    return directory.isFile(MANIFEST_FILENAME) or \
        directory.isFile(RULE_FILENAME)



def getTheme(name, manifest=None, resources=None):
    if manifest is None:
        if resources is None:
            resources = getAllResources(
                                        MANIFEST_FORMAT, filter=isValidThemeDirectory)
        if name not in resources:
            return None
        manifest = resources[name]
    title = name.capitalize().replace('-', ' ').replace('.', ' ')
    description = None
    rules = u"/++%s++%s/%s" % (THEME_RESOURCE_NAME, name, RULE_FILENAME,)
    prefix = u"/++%s++%s" % (THEME_RESOURCE_NAME, name,)
    params = {}
    doctype = ""
    preview = None
    
    if manifest is not None:
        title = manifest['title'] or title
        description = manifest['description'] or description
        rules = manifest['rules'] or rules
        prefix = manifest['prefix'] or prefix
        params = manifest['parameters'] or params
        doctype = manifest['doctype'] or doctype
        preview = manifest['preview'] or preview
    
    if isinstance(rules, str):
        rules = rules.decode('utf-8')
    if isinstance(prefix, str):
        prefix = prefix.decode('utf-8')
    
    return Theme(name, rules,
                 title=title,
                 description=description,
                 absolutePrefix=prefix,
                 parameterExpressions=params,
                 doctype=doctype,
                 preview=preview,
                 )


def getAvailableThemes():
    """Get a list of all ITheme's available in resource directories.
        """
    
    resources = getAllResources(MANIFEST_FORMAT, filter=isValidThemeDirectory)
    themes = []
    for name, manifest in resources.items():
        themes.append(getTheme(name, manifest))
    
    themes.sort(key=lambda x: safe_unicode(x.title))
    return themes


def getThemeFromResourceDirectory(resourceDirectory):
    """Return a Theme object from a resource directory
        """
    
    name = resourceDirectory.__name__
    
    title = name.capitalize().replace('-', ' ').replace('.', ' ')
    description = None
    rules = u"/++%s++%s/%s" % (THEME_RESOURCE_NAME, name, RULE_FILENAME,)
    prefix = u"/++%s++%s" % (THEME_RESOURCE_NAME, name,)
    params = {}
    doctype = ""
    
    if resourceDirectory.isFile(MANIFEST_FILENAME):
        manifest = getManifest(resourceDirectory.openFile(MANIFEST_FILENAME), MANIFEST_FORMAT)
                               
        title = manifest['title'] or title
        description = manifest['description'] or description
        rules = manifest['rules'] or rules
        prefix = manifest['prefix'] or prefix
        params = manifest['parameters'] or params
        doctype = manifest['doctype'] or doctype
    
    if isinstance(rules, str):
        rules = rules.decode('utf-8')
    if isinstance(prefix, str):
        prefix = prefix.decode('utf-8')
    
    return Theme(name, rules,
                 title=title,
                 description=description,
                 absolutePrefix=prefix,
                 parameterExpressions=params,
                 doctype=doctype,
                 )


def getZODBThemes():
    """Get a list of ITheme's stored in the ZODB.
    """

    resources = getZODBResources(MANIFEST_FORMAT, filter=isValidThemeDirectory)
    themes = []
    for name, manifest in resources.items():
        themes.append(getTheme(name, manifest))

    themes.sort(key=lambda x: x.title)
    return themes



 


                   
def ThemeVocabulary(context):
    """Get a list of all ITheme's available in resource directories and make a vocabulary.
    """
    
    themes = getAvailableThemes()
    
    #import pdb; pdb.set_trace()
    
    terms = [SimpleTerm(value=theme.__name__,
            token=theme.__name__,
            title=theme.title) for theme in themes]

    return SimpleVocabulary(terms)

directlyProvides(ThemeVocabulary, IVocabularyFactory)
