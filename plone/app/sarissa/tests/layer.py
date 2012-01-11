from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class SarissaLayer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.sarissa
        self.loadZCML(package=plone.app.sarissa)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'plone.app.sarissa:default')


FIXTURE = SarissaLayer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                                 name="plone.app.sarissa:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                               name="plone.app.sarissa:Functional")
