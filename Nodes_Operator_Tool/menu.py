import nuke
import os
import sys
import nukescripts
import node_operator_tool

import imp

imp.reload(node_operator_tool)

# Register the pane as a Nuke pane
nukescripts.registerWidgetAsPanel(
    "node_operator_tool.NodeOperator", 
    "Node Operator", 
    "uk.co.example.CustomPanel", 
    create=True,
)



