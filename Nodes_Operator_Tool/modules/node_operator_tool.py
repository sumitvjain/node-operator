from PySide2.QtWidgets import QWidget, QApplication, QInputDialog, QFileDialog, QTableWidget, QHeaderView,QFrame,QAbstractItemView, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
from PySide2.QtGui import QPixmap, QColor, QFont
from PySide2.QtCore import QSize, Qt, QRect
import sys, os
import nuke
import nukescripts
import re
import ast
import json
from datetime import datetime
from pprint import pprint

# Global Variable
window = None

# Relative path of icons dir assigned to variable
dir_path = os.path.dirname(__file__)
icons_dir_path = os.path.join(dir_path, 'icons')


class ImportNodeInfoPanel(nukescripts.PythonPanel):
    """
    Custom panel for importing node information in Nuke.
    Param:
        file_items : List of file names to display in the enumeration knob.
    """

    def __init__(self, file_items):
        super(ImportNodeInfoPanel, self).__init__('Selected Operator')

        self.file_items = file_items
        self.enumeration_knob = nuke.Enumeration_Knob('import_panel', 'Select File Name', self.file_items)
        self.addKnob(self.enumeration_knob)

class NodeOperator(QWidget):
    """
    Main UI class for managing and operation on Nuke nodes.
    Attributes:
       self.mainVlay (QVBoxLayout) : main layout of the widget. 
       self.sel_nodes : List of the selected nodes.
       self.nodes_data : Dictionary containing node data.
       self.headers : List of table headers.
    """

    def __init__(self, parent=None):
        super(NodeOperator, self).__init__(parent)
        self.mainVlay = QVBoxLayout()  
        self.setLayout(self.mainVlay)

        self.sel_nodes = None
        self.nodes_data = {}
        self.headers = None

        self.set_ui_header()
        self.set_top_btn_widgets()
        self.add_font_widget()
        self.add_table()
        self.set_author_name()        
        self.init()
  
    def init(self):
        """
        Initialize all signal-slot connections for UI interactions.
        """
        self.btn_load.clicked.connect(self.btn_load_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_all.clicked.connect(self.btn_all_clicked)
        self.btn_selected_clear.clicked.connect(self.btn_selected_clear_clicked)
        self.btn_all_clear.clicked.connect(self.btn_all_clear_clicked)
        self.search_line_edit.textEdited.connect(self.edited_search_line)
        self.font_size.textEdited.connect(self.changed_font_size)
        self.font_combo.currentTextChanged.connect(self.font_changed)        
        self.btn_color.clicked.connect(self.btn_color_clicked)
        self.btn_bold.clicked.connect(self.btn_bold_clicked)
        self.btn_italic.clicked.connect(self.btn_italic_clicked)
        self.table.cellChanged.connect(self.on_cell_changed)
        self.table.cellDoubleClicked.connect(self.on_cellDoubleClicked)
        self.table.cellClicked.connect(self.cell_clicked)
        self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_import.clicked.connect(self.btn_import_clicked)
                
    def set_ui_header(self):
        """
        Set up the header section of the UI with a title and description.
        """
        self.headerHlay = QHBoxLayout()

        horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        headerLabel = QLabel('NODE OPERATOR')
        header_font = QFont()
        header_font.setBold(True)
        header_font.setPointSize(14)
        headerLabel.setFont(header_font)
        headerLabel.setStyleSheet("color: #555555;")
        
        description_label = QLabel(" -  Streamline node management")
        description_font = QFont()
        description_font.setItalic(True)
        description_font.setPointSize(10) 
        description_label.setFont(description_font)
        description_label.setStyleSheet("color: #696969;")

        horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.headerHlay.addSpacerItem(horizontalSpacer1)
        self.headerHlay.addWidget(headerLabel)
        self.headerHlay.addWidget(description_label)
        self.headerHlay.addSpacerItem(horizontalSpacer2)

        self.mainVlay.addLayout(self.headerHlay)
        
    def set_top_btn_widgets(self):
        """
        Configures and adds the top button widgets..
        Includes functionalities for searching nodes, importing/exporting data, and node management.
        """

        self.hlay_1 = QHBoxLayout()
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setMinimumWidth(75)
        self.search_line_edit.setPlaceholderText('Find Node')
        self.search_line_edit.setToolTip('To perform a case-sensitive node search in the Node Operator Tool.')

        self.btn_export = QPushButton('Export')
        self.btn_export.setEnabled(False)
        self.btn_import = QPushButton('Import')

        self.btn_load = QPushButton(' Load Selected')
        self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
        self.btn_load.setIconSize(QSize(13, 13))
        self.btn_load.setToolTip('Selected nodes in the Nuke node graph will be added to the Node Operator Tool..')

        self.btn_add = QPushButton(' Add')
        self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
        self.btn_add.setIconSize(QSize(13, 13))
        self.btn_add.setEnabled(False)
        self.btn_add.setToolTip('Appends the selected node to the Node Operator Tool.')

        self.btn_all = QPushButton(' Load All')
        self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
        self.btn_all.setIconSize(QSize(13, 13))
        rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
        self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")
        self.btn_all.setToolTip('Loads all nodes from the Nuke node graph into the Node Operator Tool.')

        self.btn_refresh = QPushButton(' Refresh')
        self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
        self.btn_refresh.setIconSize(QSize(13, 13))
        self.btn_refresh.setToolTip('Update data for nodes added in the Node Operator Tool based on Nuke node values.')

        self.btn_selected_clear = QPushButton(' Clear Selected')
        self.btn_selected_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'selected_clear_icon1')))
        self.btn_selected_clear.setIconSize(QSize(13, 13)) 
        self.btn_selected_clear.setToolTip('Removes selected node properties from the Node Operator Tool.')

        self.btn_all_clear = QPushButton(' Clear All')
        self.btn_all_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
        self.btn_all_clear.setIconSize(QSize(13, 13))    
        self.btn_all_clear.setToolTip('Removes all node properties from the Node Operator Tool..')

        self.hlay_1.addWidget(self.search_line_edit)
        self.hlay_1.addWidget(self.btn_export)
        self.hlay_1.addWidget(self.btn_import)
        self.hlay_1.addWidget(self.btn_load)
        self.hlay_1.addWidget(self.btn_add)
        self.hlay_1.addWidget(self.btn_all)
        self.hlay_1.addWidget(self.btn_refresh)
        self.hlay_1.addWidget(self.btn_selected_clear)
        self.hlay_1.addWidget(self.btn_all_clear)
       
        self.mainVlay.addLayout(self.hlay_1)

    def add_font_widget(self):
        """
        configures and adds the font customization widgets.
        Allows users to change font type, size and style for the selected nodes in the Node Operator Tool.
        """
        self.fontHLay = QHBoxLayout()

        # Node count labels
        self.label_nodes_added = QLabel('Nodes Added : ')    
        self.label_nodes_count = QLabel('')

        # Selected node name labels (hidden by default)
        self.label_nodes_selected_name = QLabel('Nodes Selected Name : ') 
        self.label_nodes_selected_name.setHidden(True)
        self.label_sel_nods_nm = QLabel()
        self.label_sel_nods_nm.setHidden(True)

        # Font drop-down
        font_spacer = QSpacerItem(2000, 10, QSizePolicy.Maximum)
        self.font_combo = QComboBox()        
        fonts_data = nuke.getFonts()
        all_fonts = []
        for font_nm in fonts_data:
           all_fonts.append(font_nm[0])
        self.font_combo.addItems(all_fonts)
        self.font_combo.setCurrentText('Verdana')

        # Bold button
        self.btn_bold = QPushButton('Bold')
        self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
        self.btn_bold.setIconSize(QSize(12, 12))
        self.btn_bold.setMaximumWidth(50)
        self.btn_bold.setCheckable(True)
        self.btn_bold.setChecked(False)    
        self.btn_bold.setToolTip('Text font will be bold for single or multiple selections in the Node Operator Tool.')    

        # Italic button
        self.btn_italic = QPushButton('Italic')
        self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
        self.btn_italic.setIconSize(QSize(12, 12))
        self.btn_italic.setMaximumWidth(75)
        self.btn_italic.setCheckable(True)
        self.btn_italic.setChecked(False)
        self.btn_italic.setToolTip('Text font will be italic for single or multiple selections in the Node Operator Tool.') 

        # Font size 
        self.font_size = QLineEdit('11')
        self.font_size.setMaximumWidth(30)
        self.font_size.setToolTip('Text font size will be set for single or multiple selections in the Node Operator Tool.') 

        # Color button
        self.btn_color = QPushButton('Color')
        self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
        self.btn_color.setMaximumWidth(75)
        self.btn_color.setToolTip('Node color will be set for single or multiple selections in the Node Operator Tool.') 

        # Separator line
        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        # Adding widget to the layout
        self.fontHLay.addWidget(self.label_nodes_added)
        self.fontHLay.addWidget(self.label_nodes_count)
        self.fontHLay.addWidget(self.separator)
        self.fontHLay.addWidget(self.label_nodes_selected_name)
        self.fontHLay.addWidget(self.label_sel_nods_nm)
        self.fontHLay.addSpacerItem(font_spacer)
        self.fontHLay.addWidget(self.font_combo)
        self.fontHLay.addWidget(self.btn_bold)
        self.fontHLay.addWidget(self.btn_italic)
        self.fontHLay.addWidget(self.font_size)
        self.fontHLay.addWidget(self.separator)
        self.fontHLay.addWidget(self.btn_color)

        self.mainVlay.addLayout(self.fontHLay)
        
    def add_table(self):
        """
        Configures and adds the main table widget to the layout.
        The table widget display information about nodes and allows for editing properties.
        """
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.headers = ['Node Name', 'On/Off', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set table header with column count
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)  

        self.table.horizontalHeader().setStretchLastSection(True) 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  

        self.table.horizontalHeader().sectionResized.connect(self.adjust_combobox_widths)

        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.mainVlay.addWidget(self.table, stretch=1)

    def set_author_name(self):
        """
        Adds autor name lable at bottom layout, displaying tool version and update data.
        """
        self.author_name_Hlay = QHBoxLayout()
        author_name_lbl = QLabel("Created by Sumit Saktepar [1.0.0] - Last update 27 Dec 2024")
        author_name_font = QFont()
        # author_name_font.setItalic(True)
        author_name_font.setPointSize(10) 
        author_name_lbl.setFont(author_name_font)
        author_name_lbl.setStyleSheet("color: #696969;")

        self.author_name_Hlay.addWidget(author_name_lbl)
        self.mainVlay.addLayout(self.author_name_Hlay)

    def set_nodes_count(self, nodes_len):
        """
        Update the label displaying the number of added nodes in the Node Operator Tool.
        Param:
            nodes_len : selected nodes in nuke node graph (int value)
        """
        self.label_nodes_count.setText(str(nodes_len))

    def set_row_count_to_ui(self, nodes_len):
        """
        Sets the row count to the table UI.
        Param:
            nodes_len : selected nodes in nuke node graph (int value)
        """
        self.table.setRowCount(nodes_len)

    def get_selected_node(self):
        """
        Gets the currently selected nodes in Nuke node graph.
        """
        check_nodes_ = nuke.selectedNodes()
        if len(check_nodes_) > 0:
            self.sel_nodes = nuke.selectedNodes()

    def get_nodes_info(self, nodes):     
        """
        Gathers information about selected nodes including specific knob values.
        Param:
            nodes: List of nodes
        """

        # Dictionary to hold Nodes data.
        self.nodes_data = {}   

        for index, node in enumerate(nodes):
            node_name = node.name()
            if node_name not in self.nodes_data:
                self.nodes_data[node_name] = {}

            for knob in node.allKnobs():
                # Populate node data dictionary with specific knob values.
                self.nodes_data[node_name]['node_name'] = node_name
            
                if knob.name() == 'disable':
                    self.nodes_data[node_name]['disable'] = node['disable'].value()
                if knob.name() == 'mix':
                    self.nodes_data[node_name]['mix'] = node['mix'].value()

                if knob.name() == 'label':
                    self.nodes_data[node_name]['label'] = node['label'].value()

                if knob.name() == 'postage_stamp':
                    self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

                if knob.name() == 'colorspace':
                    self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
                    self.colorspace_conbo = QComboBox()

                if knob.name() == 'localizationPolicy':
                    self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

                if knob.name() == 'bookmark':
                    self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

                if knob.name() == 'hide_input':
                    self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

                if knob.name() == 'lifetimeStart':
                    self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()   


                if knob.name() == 'lifetimeEnd':
                    self.nodes_data[node_name]['lifetimeEnd'] = node['lifetimeEnd'].value()
                  
    def set_ui_with_knobs(self, add_row=None):
        """
        Update the UI with node information(specific knob values).
        Param:
            add_row : row index(int) Optional, if None then updates all rows.
        """
        all_node_names = self.nodes_data.keys()

        # sorted_all_node_names = sorted(all_node_names) Temporary off
        for row_index, node_nm in enumerate(all_node_names):

            if add_row:
               row_index = add_row

            # Set node name in the table (first column)
            node_nm_widget = QTableWidgetItem(node_nm)
            self.table.setItem(row_index, 0, node_nm_widget)

            # Populate table cells with node knob values
            if 'disable' in self.nodes_data[node_nm]:           
                bln = self.nodes_data[node_nm]['disable']
                if bln:
                    self.set_chekckbox(True, row_index, 1)
                else:  
                    self.set_chekckbox(False, row_index, 1)                    

            if 'mix' in self.nodes_data[node_nm]:
                mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
                self.table.setItem(row_index, 2, mix_widget)

            if 'label' in self.nodes_data[node_nm]:
                label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
                self.table.setItem(row_index, 3, label_widget)

            if 'postage_stamp' in self.nodes_data[node_nm]:
                bln = self.nodes_data[node_nm]['postage_stamp']
                if bln:
                    self.set_chekckbox(True, row_index, 4)
                else:  
                    self.set_chekckbox(False, row_index, 4)  

            if 'colorspace' in self.nodes_data[node_nm]:
                self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

            if 'localizationPolicy' in self.nodes_data[node_nm]:
                self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

            if 'bookmark' in self.nodes_data[node_nm]:
                bln = self.nodes_data[node_nm]['bookmark']
                if bln:
                    self.set_chekckbox(True, row_index, 7)
                else:  
                    self.set_chekckbox(False, row_index, 7)                  

            if 'hide_input' in self.nodes_data[node_nm]:
                bln = self.nodes_data[node_nm]['hide_input']
                if bln:
                    self.set_chekckbox(True, row_index, 8)
                else:  
                    self.set_chekckbox(False, row_index, 8)  

            if 'lifetimeStart' in self.nodes_data[node_nm]:                
                life_start = int(self.nodes_data[node_nm]['lifetimeStart'])
                life_end = int(self.nodes_data[node_nm]['lifetimeEnd'])
                lifetime_widget = QTableWidgetItem(f'{life_start}.{life_end}')

                # Highlight if lifetime is not default
                if life_start != 0 or life_end != 0:
                    lifetime_widget.setBackground(QColor(110, 106, 94))
                self.table.setItem(row_index, 9, lifetime_widget)

            # Adjust row height
            self.table.setRowHeight(row_index, (row_index+2) * 16)

    def set_fit_to_screen(self, node_name):
        """
        Adjust the Nuke node graph to focus on the Node which is selected in UI.(if single selected)
        Param:
            node_name : single node name(str)
        """
        node = nuke.toNode(node_name)
        xpos = node.xpos()
        ypos = node.ypos()
        nuke.zoom(1, [xpos + node.screenWidth() / 2, ypos + node.screenHeight() / 2])

    def selectNodes(self, sel_nods_nm):
        """
        Select nodes in Nuke node graph based on the selected nodes names in UI
        Param:
            sel_nods_nm : List of selected node name in UI
        """        
        for nod in nuke.allNodes():
            if nod.name() in sel_nods_nm:
                nuke.toNode(nod.name()).setSelected(True)
            else:
                nuke.toNode(nod.name()).setSelected(False)

    def set_selection_nod_nm_Ui(self):
        """
        Update the UI selection to match the currently value of self.label_sel_nodes_nm (Default hidden widget)
        """
        nodes_name = self.label_sel_nods_nm.text()
        print('nodes_name -- ', nodes_name)
        for row in range(self.table.rowCount()):
            item = self.table.item(row, 0)
            node_nm = item.text()
            if node_nm in nodes_name:            
                item.setSelected(True)
            else:
                item.setSelected(False)                

    def cell_clicked(self):
        """
        Handle cell click events in the table.
        """
        items = self.table.selectedItems()
        if items:
            if items[0].column() == 0:
                sel_nods_nm = []
                for index, item in enumerate(items):        
                    if item.column() == 0:
                        sel_nods_nm.append(item.text())

                self.label_sel_nods_nm.setText(f'{sel_nods_nm}')

                self.selectNodes(sel_nods_nm)


                if len(sel_nods_nm) == 1:
                    self.set_fit_to_screen(sel_nods_nm[0])

            if items[0].column() != 0:
                self.set_selection_nod_nm_Ui()

    def update_checkbox_status(self, nod_nm, row, column, checkbox, state):
        """
        Update the checkbox state acording to single or multiple selection in UI
        Param:
            node_nm : node name (str)
            row : row index (int)
            column: column index (int)
            checkbox : checkbox widget instance
            state : checkbox state (checked or unchecked)
        """
        # For single selection
        if state == Qt.Checked:
            checkbox.setText('Enabled')
            checkbox.setChecked(True)
            if column == 1:
                nuke.toNode(nod_nm)['disable'].setValue(True)
            if column == 4:
                nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
            if column == 7:
                nuke.toNode(nod_nm)['bookmark'].setValue(True)
            if column == 8:
                nuke.toNode(nod_nm)['hide_input'].setValue(True)                
        else:
            checkbox.setText('Disabled')
            checkbox.setChecked(False)
            if column == 1:
                nuke.toNode(nod_nm)['disable'].setValue(False)
            if column == 4:
                nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
            if column == 7:
                nuke.toNode(nod_nm)['bookmark'].setValue(False)
            if column == 8:
                nuke.toNode(nod_nm)['hide_input'].setValue(False) 
 
        # For multiple selection
        if not len(self.label_sel_nods_nm.text()) == 0:
            nodes_nm_str = self.label_sel_nods_nm.text()
            nods_nm_lst = ast.literal_eval(nodes_nm_str)

            if nods_nm_lst:                
                for nm in nods_nm_lst:

                    item = self.table.findItems(nm, Qt.MatchExactly)
                    row = item[0].row()
                    checkbox_item = self.table.cellWidget(row, column)

                    if state == Qt.Checked:
                        checkbox_item.setText('Enabled')
                        checkbox_item.setChecked(True)
                        if column == 1:
                            nuke.toNode(nod_nm)['disable'].setValue(True)
                        if column == 4:
                            nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
                        if column == 7:
                            nuke.toNode(nod_nm)['bookmark'].setValue(True)
                        if column == 8:
                            nuke.toNode(nod_nm)['hide_input'].setValue(True)                
                    else:
                        checkbox_item.setText('Disabled')
                        checkbox_item.setChecked(False)
                        # checkbox_item = QCheckBox('Disabled')
                        if column == 1:
                            nuke.toNode(nod_nm)['disable'].setValue(False)
                        if column == 4:
                            nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
                        if column == 7:
                            nuke.toNode(nod_nm)['bookmark'].setValue(False)
                        if column == 8:
                            nuke.toNode(nod_nm)['hide_input'].setValue(False) 

        self.set_selection_nod_nm_Ui()

    def get_sel_ui_nods_nm(self):
        """
        Gets the neame of nodes currently selected in the table.
        """
        selected_items = self.table.selectedItems()
        nod_nm_lst = []
        for item in selected_items:
            row = item.row()
            column = item.column()

            if column == 0:
                nod_nm_lst.append(item.text())

        return nod_nm_lst

    def set_chekckbox(self, bln, row_index, col):    
            """
            Create and set a checkbox widget in the table for specific row and column.
            Param:
                bln : Boolean(True/False)
                row_index : row index (int)
                col : col index (int)
            """
            changed_val_nod_nm = self.table.item(row_index, 0).text()
            if bln:
                checkbox = QCheckBox('Enabled')
                checkbox.setChecked(True)
            else:
                checkbox = QCheckBox('Disabled')
                checkbox.setChecked(False)
            # checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state, nodes_nm))
            checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))
            self.table.setCellWidget(row_index, col, checkbox)

    def update_node_value(self, nod_nm, c_row, c_col, c_val):
        """
        Updae a specific value of nodes knob in Nuke node graph based on table input.
        Param : 
            nod_nm : node name (str)
            c_row : row index (int)
            c_col : column index (int)
            c_val : value for set
        """
        nuke_node = nuke.toNode(nod_nm)
        print('c_col -- ', c_col)
        if c_col == 0:
            pass
        elif c_col == 1:
            pass        
        elif c_col == 2: # mix
            if 'mix' in nuke_node.knobs():
                 nuke_node['mix'].setValue(float(c_val))
            else:
                print('mix knob not found')
        elif c_col == 3: # label
            if 'label' in nuke_node.knobs():
                nuke_node['label'].setValue(c_val)
        elif c_col == 9: # lift time
            if 'lifetimeStart' in nuke_node.knobs():              
                life_start = int(c_val.split('.')[0])
                life_end = int(c_val.split('.')[-1])
                nuke_node['lifetimeStart'].setValue(life_start)
                nuke_node['lifetimeEnd'].setValue(life_end)     
                
                if life_start != 0 or life_end != 0:
                    nuke_node['useLifetime'].setValue(True)
                    lifetime_widget = self.table.item(c_row, c_col)
                    lifetime_widget.setBackground(QColor(110, 106, 94))                     
                else:
                    nuke_node['useLifetime'].setValue(False)
        elif c_col == 5: #
            if 'colorspace' in nuke_node.knobs():
                nuke_node['colorspace'].setValue(c_val)

        elif c_col == 6:
            if 'localizationPolicy' in nuke_node.knobs():
                nuke_node['localizationPolicy'].setValue(c_val)
        else:
            pass     

    def on_cell_changed(self, row, column):
        """
        This is callback func for cell selection change in table
        Param:
            row : int value
            column : int value 
        """
        item = self.table.item(row, column)
        if item:
            changed_row = row
            changed_column =  column
            changed_value = item.text()
            print('changed_value -- ', changed_value)

            changed_val_nod_nm = self.table.item(row, 0).text()
            self.update_node_value(changed_val_nod_nm, changed_row, changed_column, changed_value)

    def lock_first_last(self):   
        """
        Lock editing for the first columns of the table
        """    
        for row in range(self.table.rowCount()):
            read_item = self.table.item(row, 0)
            read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

            # lifetime_item = self.table.item(row, 9)
            # lifetime_item.setFlags(lifetime_item.flags() & ~Qt.ItemIsEditable)

    def colorspace_index_changed(self, combo_box, col):
        """
        This func for color space ComboBox index changed.
        Param:
            combo_box : QComboBox instance whose value changed.
            col : column index (int)
        """
        combo_cur_text = combo_box.currentText()
        changed_row = None
        changed_column = None

        # Find row and column of the combobox
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                if self.table.cellWidget(row, column) == combo_box:
                    changed_row = row
                    changed_column = column

        changed_val_nod_nm = self.table.item(changed_row, 0).text()
        self.update_node_value(changed_val_nod_nm, changed_row, changed_column, combo_cur_text)

        if not len(self.label_sel_nods_nm.text()) == 0:
            nodes_nm_str = self.label_sel_nods_nm.text()
            nods_nm_lst = ast.literal_eval(nodes_nm_str)
            print('nods_nm_lst ***** ', nods_nm_lst)

            if nods_nm_lst:                
                for nm in nods_nm_lst:
                    item = self.table.findItems(nm, Qt.MatchExactly)
                    row = item[0].row()
                    combobox_item = self.table.cellWidget(row, col)
                    self.update_node_value(nm, row, col, combo_cur_text)

                    combobox_item.setCurrentText(combo_cur_text)

    def adjust_combobox_width(self, row, column):
        """
        Adjust ComboBox width to fit the column size.
        """
        widget = self.table.cellWidget(row, column)
        if isinstance(widget, QComboBox):
            column_width = self.table.columnWidth(column)
            widget.setFixedWidth(column_width)

    def adjust_combobox_widths(self):
        """
        Adjust all ComboBoxes in the table(in bulk).
        """
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                self.adjust_combobox_width(row, column)

    def set_combo_companies(self, node_nm, knob_nm, row_index, col):
            """
            Set up a ComboBox for color space and localize policy.
            Param:
                node_nm : node name (str)
                knob_nm : nuke node knob name
                row_index : row index (int)
                col : column index (int)
            """
            self.colorspace_combobox = QComboBox()
                 
            values = nuke.toNode(node_nm)[knob_nm].values()
            self.colorspace_combobox.addItems(values)
            self.table.setCellWidget(row_index, col, self.colorspace_combobox)

            self.adjust_combobox_width(row_index, col)
            
            # Set value
            value = nuke.toNode(node_nm)[knob_nm].value()
            index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
            self.colorspace_combobox.setCurrentIndex(index)

            # Connect comboBox to its handler
            # self.colorspace_combobox.currentIndexChanged.connect(lambda state, r=row_index, c=col: self.colorspace_index_changed(r, c, state))
            self.colorspace_combobox.currentIndexChanged.connect(lambda text, c=col, combo_box=self.colorspace_combobox: self.colorspace_index_changed(combo_box, c))

    def btn_load_clicked(self):
        """
        This is callback func to populate the table with selected nodes information.
        """
        self.sel_nodes = None
        self.get_selected_node()

        if self.sel_nodes:
            self.btn_all_clear_clicked()

            nodes_len = len(nuke.selectedNodes())
            self.set_row_count_to_ui(nodes_len)

            nodes = nuke.selectedNodes()
            self.get_nodes_info(nodes)
            self.set_ui_with_knobs()
            self.lock_first_last()

            self.set_nodes_count(nodes_len)
        else:
            nuke.message('Please Select Nodes')
        self.btn_add.setEnabled(True)
        self.btn_export.setEnabled(True)
        
    def btn_add_clicked(self):  
        """
        This is callback func for add/append in table with selected nodes
        """      
        nodes = nuke.selectedNodes()
        add_count = 0
        for index, node in enumerate(nodes):
            bln = self.check_node_in_table(node)
            if bln:
                add_row = self.add_new_node(index, node)    
                self.get_nodes_info([node])
                self.set_ui_with_knobs(add_row)  
                add_count += 1
        self.lock_first_last()   

        nodes_len = add_count + int(self.label_nodes_count.text())
        self.set_nodes_count(str(nodes_len))

    def check_node_in_table(self, node):
        """
        Check if a node is already present in the table.
        Param:
            node : Nuke node object
        return : 
            bool : True if the node is not in the table, False otherwise.
        """
        all_node_names = []
        for row in range(self.table.rowCount()):
            fst_column_data = self.table.item(row, 0)
            all_node_names.append(fst_column_data.text())

        if node.name() in all_node_names:
            return False
        else:
            return True

    def add_new_node(self, index, node):
        """
        Add a new row to the table for the selected node.
        Param : 
            index :
        return : 
            The index of the newly added row(int).
        """
        current_row_count = self.table.rowCount()
        self.table.insertRow(current_row_count)
        return current_row_count
        
    def btn_all_clicked(self):
        """
        This is callback func to populate the UI with all nodes.
        """
        self.btn_all.setEnabled(False)
        self.btn_all_clear_clicked()

        nodes_len = len(nuke.allNodes())
        self.set_row_count_to_ui(nodes_len)

        nodes = nuke.allNodes()
        self.get_nodes_info(nodes)
        self.set_ui_with_knobs()      
        self.btn_add.setEnabled(False)
        self.lock_first_last()
        self.btn_all.setEnabled(True)

        self.set_nodes_count(nodes_len)
        self.btn_export.setEnabled(True)

    def btn_all_clear_clicked(self):
        """
        Clear the table and reset UI for a fresh start.
        """
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setColumnCount(10)
        self.btn_add.setEnabled(False)
        self.set_nodes_count('')
        self.btn_export.setEnabled(False)
        
    def edited_search_line(self, text):
        """Highlight rows in the table matching the search query."""
        self.table.setCurrentItem(None)
        if not text:
            return
        matching_items = self.table.findItems(text, Qt.MatchContains) 
        if matching_items:
            for item in matching_items:
                item.setSelected(True)

    def changed_font_size(self, size):
        """Update the font size of selected items in UI."""
        if not size:
            return

        sel_items = self.table.selectedItems()
        sel_item_nm = []

        if sel_items:
            for item in sel_items:
                sel_item_nm.append(item.text())
    
            if sel_item_nm: 
                for node_nm in sel_item_nm:
                    if nuke.toNode(node_nm):
                        nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
            else:
                nuke.message('Please select Node Names in Node Operator UI')
        
    def btn_color_clicked(self):
        """Change the tile color of selected items in UI."""
        sel_items = self.table.selectedItems()
        sel_item_nm = []

        if sel_items:
            for item in sel_items:
                sel_item_nm.append(item.text())
    
            usr_sel_color = nuke.getColor() 

            if usr_sel_color: 
                for node_nm in sel_item_nm:
                    if nuke.toNode(node_nm):
                        nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 

    def font_changed(self, font_nm):
        """Update the font of selected items in UI."""
        if not font_nm:
            return

        sel_items = self.table.selectedItems()
        sel_item_nm = []

        if sel_items:
            for item in sel_items:
                sel_item_nm.append(item.text())
    
            if sel_item_nm: 
                for node_nm in sel_item_nm:
                    if nuke.toNode(node_nm):
                        nuke.toNode(node_nm)['note_font'].setValue(font_nm)
            else:
                nuke.message('Please select Node Names in Node Operator UI')

    def update_text_pattern(self, bold=None, sel_item_nm=None):
        """Update text style (bold/regular) for selected items in UI."""

        for node_nm in sel_item_nm:
            if nuke.toNode(node_nm):     
                if bold:
                    nuke.toNode(node_nm)['note_font'].setValue('bold')
                else:
                    nuke.toNode(node_nm)['note_font'].setValue("")

    def btn_bold_clicked(self):
        """Toggle bold font style for selected items in UI."""
        sel_items = self.table.selectedItems()
        sel_item_nm = []

        if sel_items:
            for item in sel_items:
                sel_item_nm.append(item.text())

            if sel_item_nm: 
                if self.btn_bold.isChecked():
                    self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
                else:
                    self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
            else:
                nuke.message('Please select Node Names in Node Operator UI')

    def update_italic_pattern(self, italic=None, sel_item_nm=None):
        """Update text style (italic/regular) for selected items in UI."""
        for node_nm in sel_item_nm:
            if nuke.toNode(node_nm):     
                if italic:
                    nuke.toNode(node_nm)['note_font'].setValue('italic')
                    print('pressed for italic')
                else:
                    print('released for italic')
                    nuke.toNode(node_nm)['note_font'].setValue("")

    def btn_italic_clicked(self):
        """Toggle italic font style for selected items in UI."""
        sel_items = self.table.selectedItems()
        sel_item_nm = []

        if sel_items:
            for item in sel_items:
                sel_item_nm.append(item.text())

            if sel_item_nm: 
                if self.btn_italic.isChecked():
                    self.update_italic_pattern(italic='italic', sel_item_nm=sel_item_nm)            
                else:
                     self.update_italic_pattern(italic=None, sel_item_nm=sel_item_nm)            
            else:
                nuke.message('Please select Node Names in Node Operator UI')

    def get_life_frame_range(self):
        """Prompt user for a frame range input and validate it."""
        frame_range = nuke.getInput('Please Enter frame-range \n example 1009.1050')
        if not '.' in frame_range:
            nuke.message('Invalid frame-range \n Please try again')
            self.get_frame_range()

        start_frame = frame_range.split('.')[0]
        end_frame = frame_range.split('.')[-1]

        if not start_frame <= end_frame:
            nuke.message('Invalid frame-range \n Please try again')
            self.get_frame_range()
        else:
            return True, start_frame, end_frame

    def on_cellDoubleClicked(self, row, column):
        """Handle double-click on a cell to update frame range."""
        if column == 9:
            bln, start_frame, end_frame = self.get_life_frame_range()
            if bln:
                item = QTableWidgetItem(f'{start_frame}.{end_frame}')
                self.table.setItem(row, column, item)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                changed_val_nod_nm = self.table.item(row, 0).text()
                self.update_node_value(changed_val_nod_nm, row, column, [start_frame, end_frame])

    def btn_refresh_clicked(self):
        """Refresh UI to synchronize with current node state."""
        ui_nod_nm_lst = []
        for row in range(self.table.rowCount()):
            node_nm = self.table.item(row, 0).text()
            ui_nod_nm_lst.append(node_nm)

        if ui_nod_nm_lst:
            self.btn_all_clear_clicked()

            nodes_len = len(ui_nod_nm_lst)
            self.set_row_count_to_ui(nodes_len)

            nodes = []
            for nod in ui_nod_nm_lst:
                nodes.append(nuke.toNode(nod))

            self.get_nodes_info(nodes)
            self.set_ui_with_knobs()
            self.lock_first_last()

            self.set_nodes_count(nodes_len)

            self.label_sel_nods_nm.setText('')

        else:
            nuke.message('Node Operator panel is empty \n Please Load nodes!')
                
    def btn_selected_clear_clicked(self):
        """Remove selected nodes from the UI."""
        remove_nod_nm_lst = self.get_sel_ui_nods_nm()

        if remove_nod_nm_lst:
            ui_nod_nm_lst = []
            for row in range(self.table.rowCount()):
                node_nm = self.table.item(row, 0).text()
                ui_nod_nm_lst.append(node_nm)  

            nod_nm_lst_for_add = [ele for ele in ui_nod_nm_lst]
            for a in remove_nod_nm_lst:
                if a in ui_nod_nm_lst:
                    nod_nm_lst_for_add.remove(a)

            if nod_nm_lst_for_add:
                self.btn_all_clear_clicked()   

                nodes_len = len(nod_nm_lst_for_add)
                self.set_row_count_to_ui(nodes_len)

                nodes = []
                for nod in nod_nm_lst_for_add:
                    nodes.append(nuke.toNode(nod))    

                self.get_nodes_info(nodes)
                self.set_ui_with_knobs()
                self.lock_first_last()

                self.set_nodes_count(nodes_len)

            else:
                self.btn_all_clear_clicked()

        if not self.table.rowCount() == 0:
            print('self.table.rowCount() -- ', self.table.rowCount())
            self.btn_export.setEnabled(True)
    
    def btn_export_clicked(self):
        """Export node information to a JSON file."""
        all_ui_nod_nm_lst = []
        for row in range(self.table.rowCount()):
            node_nm = self.table.item(row, 0).text()
            all_ui_nod_nm_lst.append(node_nm)  

        if all_ui_nod_nm_lst:                   
            file_nm, ok = QInputDialog.getText(self,'Node Export Dialog', 'Enter File Name : ')

            if ok:
                if not file_nm:
                    self.btn_export_clicked()
                else:
                    home_dir = os.path.expanduser("~")
                    current_datetime = datetime.now()
                    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
                    # formatted_datetime_new = formatted_datetime.replace(" ", "-")
                    export_path = os.path.join(home_dir, '.nuke', 'node_operator_data', f"{formatted_datetime}_{file_nm}" )
           
                        
                    if export_path:  # Ensure the user didn't cancel the dialog
                        print('export_path -- ', export_path)
                        os.makedirs(os.path.dirname(export_path), exist_ok=True)
                        
                        try:
                            with open(export_path, 'w') as json_file:
                                json.dump(all_ui_nod_nm_lst, json_file, indent=4)
                            nuke.message(f"Node information saved to : {export_path}")
                        except Exception as e:
                            nuke.message(f"Failed to save file: {e}")
                    else:
                        nuke.message("Save operation was canceled.")               
        


    def btn_import_clicked(self):
        """Import node information from a JSON file."""
        home_dir = os.path.expanduser("~")
        import_path = os.path.join(home_dir, '.nuke', 'node_operator_data')

        file_items = os.listdir(import_path)
        if file_items:

            panel = ImportNodeInfoPanel(file_items)
            if panel.showModalDialog():
                selected_value = panel.enumeration_knob.value()
                print("Selected Option:", selected_value)
                import_file_path = os.path.join(import_path, selected_value)

                data = None
                if os.path.exists(import_file_path):
                    try:
                        with open(import_file_path, 'r') as f:
                            data = json.load(f)
                            print('data -- ', data)
                    except Exception as e:
                            nuke.message(f"Error reading JSON file: {e}")

                    all_nuke_nod_nm = []
                    for nuke_nod in nuke.allNodes():
                        all_nuke_nod_nm.append(nuke_nod.name())

                    new_nod_nm_data = []
                    for nod_nm in data:
                        if nod_nm in all_nuke_nod_nm:
                            new_nod_nm_data.append(nod_nm)

                    if new_nod_nm_data:
                        self.btn_all_clear_clicked()
                        nodes_len = len(new_nod_nm_data)
                        self.set_row_count_to_ui(nodes_len)

                        nodes = []
                        for nod_nm in new_nod_nm_data:
                            nodes.append(nuke.toNode(nod_nm))

                        self.get_nodes_info(nodes)
                        self.set_ui_with_knobs()
                        self.lock_first_last()

                        self.set_nodes_count(nodes_len)
                    else:
                        nuke.message('Please Select Nodes')
                    self.btn_add.setEnabled(True)
                    self.btn_export.setEnabled(True)
                else:
                    print('Path does not exists -- ', import_file_path)

            else:
                print("Panel operation was canceled.")            
        else:
            nuke.message("Exported node information does not exist.")



def main():
    global window
#    app = QApplication(sys.argv)
    window = NodeOperator()
    window.show()
#    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

############################################################################
