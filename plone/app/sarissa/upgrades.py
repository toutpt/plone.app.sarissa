from Products.CMFCore.utils import getToolByName

def remove_plone3rdParty_sarissa(context):
    jsregistry = getToolByName('portal_javascripts')
    jsregistry.unregisterResource('sarissa')
    jsregistry.cookResources()
