import nuke
import os

nuke_operator_module = os.path.join(os.path.dirname(__file__), 'modules')
nuke_operator_icons = os.path.join(os.path.dirname(__file__), 'icons')

nuke.pluginAddPath(nuke_operator_module)
nuke.pluginAddPath(nuke_operator_icons)



