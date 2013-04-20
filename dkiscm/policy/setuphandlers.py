from collective.grok import gs
from dkiscm.policy import MessageFactory as _

@gs.importstep(
    name=u'dkiscm.policy', 
    title=_('dkiscm.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('dkiscm.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
