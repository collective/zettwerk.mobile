from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class ZettwerkMobile(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import zettwerk.mobile
        xmlconfig.file('configure.zcml',
                       zettwerk.mobile,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'zettwerk.mobile:default')

ZETTWERK_MOBILE_FIXTURE = ZettwerkMobile()
ZETTWERK_MOBILE_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(ZETTWERK_MOBILE_FIXTURE, ),
                       name="ZettwerkMobile:Integration")