from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.interface import directlyProvides
from zope.i18nmessageid import MessageFactory

from plone.app.theming import utils 


_ = MessageFactory('zettwerk.mobile')
 

THEMES = ['zettwerk.mobile']
 
                   
def ThemeVocabulary(context):
    """Get a list of all ITheme's available in resource directories and make a vocabulary.
    """

    terms = [SimpleTerm(value=name,
            token=name,
            title=name) for name in THEMES]

    return SimpleVocabulary(terms)

directlyProvides(ThemeVocabulary, IVocabularyFactory)
