from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from zettwerk.mobile.interfaces import IMobileSettings
from plone.z3cform import layout
from z3c.form import form


class SettingsControlPanelForm(RegistryEditForm):

    form.extends(RegistryEditForm)
    schema = IMobileSettings


ZooControlPanelView = layout.wrap_form(SettingsControlPanelForm,
                                       ControlPanelFormWrapper)
ZooControlPanelView.label = u"zettwerk.mobile settings"
