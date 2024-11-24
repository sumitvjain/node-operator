import nuke
import os


nuke_operator_module = os.path.join(os.path.dirname(__file__), 'modules')
nuke.pluginAddPath(nuke_operator_module)



