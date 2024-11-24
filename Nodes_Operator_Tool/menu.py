import nuke
import os
import sys
import nukescripts
import node_operator_tool




# add_node_operation_panel()
custom_widget = node_operator_tool.NodeOperator()

# Register the pane as a Nuke pane
nukescripts.registerWidgetAsPanel(
    "node_operator_tool.NodeOperator", 
    "Node Operation", 
    "uk.co.example.CustomPanel", 
    create=True
)