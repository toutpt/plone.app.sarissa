from Products.CMFCore.utils import getToolByName

def remove_plone3rdParty_sarissa(context):
    """This is the future upgrade that will be applied to Plone"""
    jsregistry = getToolByName(context, 'portal_javascripts')
    jsregistry.unregisterResource('sarissa.js')
    jsregistry.cookResources()
