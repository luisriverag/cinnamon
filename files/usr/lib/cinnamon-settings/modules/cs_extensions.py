#!/usr/bin/env python

from ExtensionCore import ExtensionSidePage

class Module:
    def __init__(self, content_box):
        keywords = _("extension, addon")
        self.name = "extensions"
        self.comment = _("Manage your Cinnamon extensions")            
        # we do not translate Cinnamon
        target = "Cinnamon"
        sidePage = ExtensionViewSidePage(_("Extensions"), "cs-extensions", keywords, content_box, "extension", target, self)
        self.sidePage = sidePage
        self.category = "prefs"

    def on_module_selected(self):
        if not self.loaded:
            print "Loading Extensions module"
            self.sidePage.load()

    def _setParentRef(self, window, builder):
        self.sidePage.window = window
        self.sidePage.builder = builder


class ExtensionViewSidePage (ExtensionSidePage):
    def __init__(self, name, icon, keywords, content_box, collection_type, target, module):
        self.RemoveString = ""
        ExtensionSidePage.__init__(self, name, icon, keywords, content_box, collection_type, target, module)

    def toSettingString(self, uuid, instanceId):
        return uuid

    def fromSettingString(self, string):
        return string

    def getAdditionalPage(self):
        return None

