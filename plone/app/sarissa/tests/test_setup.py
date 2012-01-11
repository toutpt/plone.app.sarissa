from plone.app.sarissa.tests import base

JS = '++resource++plone.app.sarissa/sarissa.js'
PROFILE = 'plone.app.sarissa:default'

class TestIntegration(base.TestCase):

    def test_jsregistry(self):
        jsregistry = self.portal.portal_javascripts
        sarissa = jsregistry.getResource('sarissa.js')
        self.failUnless(not sarissa.getEnabled())
        new_sarissa = jsregistry.getResource(JS)
        self.failUnless(new_sarissa.getEnabled())

    def test_upgrade(self):
        from Products.GenericSetup.upgrade import listUpgradeSteps
        setup = self.portal.portal_setup
        steps = listUpgradeSteps(setup, PROFILE, None)
        step_id = steps[0]['id']
        request = self.portal.REQUEST
        request.form['upgrades'] = [step_id]
        request.form['profile_id'] = PROFILE
        setup.manage_doUpgrades()
        
        jsregistry = self.portal.portal_javascripts
        sarissa = jsregistry.getResource('sarissa.js')
        self.failUnless(sarissa is None)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return base.build_test_suite((TestIntegration,))
