from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
from PySide2.QtGui import QPixmap, QColor, QFont
from PySide2.QtCore import QSize, Qt
import sys, os
import nuke
import re
from pprint import pprint
window = None

dir_path = os.path.dirname(__file__)
icons_dir_path = os.path.join(dir_path, 'icons')


class NodeOperator(QWidget):
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
        

        self.init()

    # Signal & Slot
    def init(self):
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
        self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        

    def set_ui_header(self):
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

        self.hlay_1 = QHBoxLayout()
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setMinimumWidth(75)
        self.search_line_edit.setPlaceholderText('Find Node')

        self.btn_load = QPushButton(' Load Selected')
        self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
        self.btn_load.setIconSize(QSize(13, 13))

        self.btn_add = QPushButton(' Add')
        self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
        self.btn_add.setIconSize(QSize(13, 13))
        self.btn_add.setEnabled(False)

        self.btn_all = QPushButton(' Load All')
        self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
        self.btn_all.setIconSize(QSize(13, 13))
        rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
        self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

        self.btn_refresh = QPushButton(' Refresh')
        self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
        self.btn_refresh.setIconSize(QSize(13, 13))

        self.btn_selected_clear = QPushButton(' Clear Selected')
        self.btn_selected_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'selected_clear_icon1')))
        self.btn_selected_clear.setIconSize(QSize(13, 13)) 

        self.btn_all_clear = QPushButton(' Clear All')
        self.btn_all_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
        self.btn_all_clear.setIconSize(QSize(13, 13))    

        self.hlay_1.addWidget(self.search_line_edit)
        self.hlay_1.addWidget(self.btn_load)
        self.hlay_1.addWidget(self.btn_add)
        self.hlay_1.addWidget(self.btn_all)
        self.hlay_1.addWidget(self.btn_refresh)
        self.hlay_1.addWidget(self.btn_selected_clear)
        self.hlay_1.addWidget(self.btn_all_clear)
       
        self.mainVlay.addLayout(self.hlay_1)

    def add_font_widget(self):
        self.fontHLay = QHBoxLayout()
        self.label_nodes_added = QLabel('Nodes Added : ')    
        self.label_nodes_count = QLabel('')

        font_spacer = QSpacerItem(2000, 10, QSizePolicy.Maximum)
        self.font_combo = QComboBox()        
        fonts_data = nuke.getFonts()
        all_fonts = []
        for font_nm in fonts_data:
           all_fonts.append(font_nm[0])
        self.font_combo.addItems(all_fonts)
        self.font_combo.setCurrentText('Verdana')


        self.btn_bold = QPushButton('Bold')
        self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
        self.btn_bold.setIconSize(QSize(12, 12))
        self.btn_bold.setMaximumWidth(50)
        self.btn_bold.setCheckable(True)
        self.btn_bold.setChecked(False)
        

        self.btn_italic = QPushButton('Italic')
        self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
        self.btn_italic.setIconSize(QSize(12, 12))
        self.btn_italic.setMaximumWidth(75)
        self.btn_italic.setCheckable(True)
        self.btn_italic.setChecked(False)

        self.font_size = QLineEdit('11')
        self.font_size.setMaximumWidth(30)

        self.btn_color = QPushButton('Color')
        self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
        self.btn_color.setMaximumWidth(75)

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.fontHLay.addWidget(self.label_nodes_added)
        self.fontHLay.addWidget(self.label_nodes_count)
        self.fontHLay.addSpacerItem(font_spacer)
        self.fontHLay.addWidget(self.font_combo)
        self.fontHLay.addWidget(self.btn_bold)
        self.fontHLay.addWidget(self.btn_italic)
        self.fontHLay.addWidget(self.font_size)
        self.fontHLay.addWidget(self.separator)
        self.fontHLay.addWidget(self.btn_color)

        self.mainVlay.addLayout(self.fontHLay)
        
    def add_table(self):

        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.headers = ['Node Name', 'On/Off', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set table header with column count
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)  

        self.table.horizontalHeader().setStretchLastSection(True) 
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.mainVlay.addWidget(self.table, stretch=1)

        # print('=*='*10)
        # for i in dir(self.table):
        #     print(i)
        # print('=*='*10)

    def set_nodes_count(self, nodes_len):
        self.label_nodes_count.setText(str(nodes_len))

    def set_row_count_to_ui(self, nodes_len):
        self.table.setRowCount(nodes_len)
        print('row updated')

    def get_selected_node(self):
        check_nodes_ = nuke.selectedNodes()
        if len(check_nodes_) > 0:
            self.sel_nodes = nuke.selectedNodes()

    def get_nodes_info(self, nodes):     

        self.nodes_data = {}   

        for index, node in enumerate(nodes):

            node_name = node.name()
            if node_name not in self.nodes_data:
                self.nodes_data[node_name] = {}

            for knob in node.allKnobs():

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
        {'Read2': {'bookmark': False,
                   'colorspace': 'default',
                   'disable': False,
                   'label': '',
                   'lifetimeStart': 0.0,
                   'localizationPolicy': 'fromAutoLocalizePath',
                   'node_name': 'Read2',
                   'postage_stamp': True},
         'Roto1': {'bookmark': False,
                   'disable': False,
                   'hide_input': False,
                   'label': '',
                   'lifetimeStart': 0.0,
                   'node_name': 'Roto1',
                   'postage_stamp': False}
        """


        all_node_names = self.nodes_data.keys()

        sorted_all_node_names = sorted(all_node_names)
        for row_index, node_nm in enumerate(sorted_all_node_names):

            if add_row:
               row_index = add_row

            node_nm_widget = QTableWidgetItem(node_nm)
            self.table.setItem(row_index, 0, node_nm_widget)

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

                if life_start != 0 or life_end != 0:
                    lifetime_widget.setBackground(QColor(110, 106, 94))
                self.table.setItem(row_index, 9, lifetime_widget)
  
            self.table.setRowHeight(row_index, (row_index+2) * 16)

    def update_checkbox_status(self,nod_nm, row, column, checkbox, state):
        if state == Qt.Checked:
            checkbox.setText('Enabled')
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
            if column == 1:
                nuke.toNode(nod_nm)['disable'].setValue(False)
            if column == 4:
                nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
            if column == 7:
                nuke.toNode(nod_nm)['bookmark'].setValue(False)
            if column == 8:
                nuke.toNode(nod_nm)['hide_input'].setValue(False)                  

    def set_chekckbox(self, bln, row_index, col):    
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox_layout.setContentsMargins(0,0,0,0)
            checkbox_layout.setAlignment(Qt.AlignCenter)

            changed_val_nod_nm = self.table.item(row_index, 0).text()

            if bln:
                checkbox = QCheckBox('Enabled')
                checkbox.setChecked(True)
            else:
                checkbox = QCheckBox('Disabled')
                checkbox.setChecked(False)

            checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))

            checkbox_layout.addWidget(checkbox)
            self.table.setCellWidget(row_index, col, checkbox_widget)

    def update_node_value(self, nod_nm, c_row, c_col, c_val):
        nuke_node = nuke.toNode(nod_nm)
        
        if c_col == 0:
            pass

        elif c_col == 1:
            pass

        elif c_col == 2: # mix
            if 'mix' in nuke_node.knobs():
                 nuke_node['mix'].setValue(float(c_val))

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
        item = self.table.item(row, column)
        if item:
            changed_row = row
            changed_column =  column
            changed_value = item.text()
            changed_val_nod_nm = self.table.item(row, 0).text()
            self.update_node_value(changed_val_nod_nm, changed_row, changed_column, changed_value)

    def lock_first_last(self):       
        for row in range(self.table.rowCount()):
            read_item = self.table.item(row, 0)
            read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

            lifetime_item = self.table.item(row, 9)
            # lifetime_item.setFlags(lifetime_item.flags() & ~Qt.ItemIsEditable)

    def colorspace_index_changed(self, combo_box):
        # print('combo_box ============= ', dir(combo_box))
        combo_cur_text = combo_box.currentText()
        changed_row = None
        changed_column = None

        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                if self.table.cellWidget(row, column) == combo_box:
                    changed_row = row
                    changed_column = column

        changed_val_nod_nm = self.table.item(changed_row, 0).text()
        self.update_node_value(changed_val_nod_nm, changed_row, changed_column, combo_cur_text)

    def set_combo_companies(self, node_nm, knob_nm, row_index, col):
            self.colorspace_combobox = QComboBox()                
            values = nuke.toNode(node_nm)[knob_nm].values()
            self.colorspace_combobox.addItems(values)
            self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
            value = nuke.toNode(node_nm)[knob_nm].value()
            index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
            self.colorspace_combobox.setCurrentIndex(index)

            # self.colorspace_combobox.currentIndexChanged.connect(lambda state, r=row_index, c=col: self.colorspace_index_changed(r, c, state))
            self.colorspace_combobox.currentIndexChanged.connect(lambda text, combo_box=self.colorspace_combobox: self.colorspace_index_changed(combo_box))

    def btn_load_clicked(self):

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

    def btn_add_clicked(self):        
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
        all_node_names = []
        for row in range(self.table.rowCount()):
            fst_column_data = self.table.item(row, 0)
            all_node_names.append(fst_column_data.text())

        if node.name() in all_node_names:
            return False
        else:
            return True

    def add_new_node(self, index, node):
        current_row_count = self.table.rowCount()
        self.table.insertRow(current_row_count)
        return current_row_count
        
    def btn_all_clicked(self):

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

    def btn_all_clear_clicked(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setColumnCount(10)
        self.btn_add.setEnabled(False)
        self.set_nodes_count('')
        
    def edited_search_line(self, text):
        self.table.setCurrentItem(None)
        if not text:
            return
        matching_items = self.table.findItems(text, Qt.MatchContains) 
        if matching_items:
            for item in matching_items:
                item.setSelected(True)

    def changed_font_size(self, size):
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

        for node_nm in sel_item_nm:
            if nuke.toNode(node_nm):     
                if bold:
                    nuke.toNode(node_nm)['note_font'].setValue('bold')
                else:
                    nuke.toNode(node_nm)['note_font'].setValue("")

    def btn_bold_clicked(self):
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

        for node_nm in sel_item_nm:
            if nuke.toNode(node_nm):     
                if italic:
                    nuke.toNode(node_nm)['note_font'].setValue('italic')
                    print('pressed for italic')
                else:
                    print('released for italic')
                    nuke.toNode(node_nm)['note_font'].setValue("")

    def btn_italic_clicked(self):
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
        if column == 9:
            bln, start_frame, end_frame = self.get_life_frame_range()
            if bln:
                item = QTableWidgetItem(f'{start_frame}.{end_frame}')
                self.table.setItem(row, column, item)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

                changed_val_nod_nm = self.table.item(row, 0).text()
                self.update_node_value(changed_val_nod_nm, row, column, [start_frame, end_frame])

    def btn_refresh_clicked(self):
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

        else:
            nuke.message('Node Operator panel is empty \n Please Load nodes!')
                
    def btn_selected_clear_clicked(self):
        selected_items = self.table.selectedItems()

        remove_nod_nm_lst = []
        for item in selected_items:
            row = item.row()
            column = item.column()

            if column == 0:
                remove_nod_nm_lst.append(item.text())

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


def main():
    global window
#    app = QApplication(sys.argv)
    window = NodeOperator()
    window.show()
#    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

############################################################################



