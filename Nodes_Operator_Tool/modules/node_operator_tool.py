from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
from PySide2.QtGui import QPixmap, Qt
from PySide2.QtCore import QSize
import sys, os
import nuke
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

        self.set_top_btn_widgets()
        self.add_table()
        self.add_font_widget()

        self.init()

    # Signal & Slot
    def init(self):
        self.btn_load.clicked.connect(self.btn_load_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_all.clicked.connect(self.btn_all_clicked)
        self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
    def set_top_btn_widgets(self):

        self.hlay_1 = QHBoxLayout()
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setMinimumWidth(75)
        self.search_line_edit.setPlaceholderText('Find Node')

        self.btn_load = QPushButton('Load Selected')
        self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
        self.btn_load.setIconSize(QSize(13, 13))
#        self.btn_load.setMinimumWidth(80)

        self.btn_add = QPushButton('Add')
        self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
        self.btn_add.setIconSize(QSize(13, 13))
        self.btn_add.setEnabled(False)

        self.btn_all = QPushButton('Load All')
        self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
        self.btn_all.setIconSize(QSize(13, 13))

        self.btn_refresh = QPushButton('Refresh')
        self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
        self.btn_refresh.setIconSize(QSize(13, 13))
        
        self.btn_clear = QPushButton('Clear All')
        self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
        self.btn_clear.setIconSize(QSize(13, 13))    

        self.hlay_1.addWidget(self.search_line_edit)
        self.hlay_1.addWidget(self.btn_load)
        self.hlay_1.addWidget(self.btn_add)
        self.hlay_1.addWidget(self.btn_all)
        self.hlay_1.addWidget(self.btn_refresh)
        self.hlay_1.addWidget(self.btn_clear)
       
        self.mainVlay.addLayout(self.hlay_1)
        
    def add_table(self):

        # self.tableVLay = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # set table header with column count
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)

        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        self.table.horizontalHeader().setStretchLastSection(True)    

        self.table.verticalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.mainVlay.addWidget(self.table, stretch=1)

    def add_font_widget(self):
        self.fontHLay = QHBoxLayout()
        self.label_node_counts = QLabel('Nodes Added: ')
        self.label_node_counts.setMinimumWidth(110)

        font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.font_combo = QComboBox()
        self.btn_bold = QPushButton()
        self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
        self.btn_bold.setIconSize(QSize(12, 12))
        self.btn_bold.setMaximumWidth(50)
        

        self.btn_italic = QPushButton()
        self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
        self.btn_italic.setIconSize(QSize(12, 12))
        self.btn_italic.setMaximumWidth(75)

        self.font_size = QLineEdit('11')
        self.font_size.setMaximumWidth(30)

        self.font_color = QPushButton('Color')
        self.font_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
        self.font_color.setMaximumWidth(75)

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

        self.fontHLay.addWidget(self.label_node_counts)
        self.fontHLay.addSpacerItem(font_spacer)
        self.fontHLay.addWidget(self.font_combo)
        self.fontHLay.addWidget(self.btn_bold)
        self.fontHLay.addWidget(self.btn_italic)
        self.fontHLay.addWidget(self.font_size)
        self.fontHLay.addWidget(self.separator)
        self.fontHLay.addWidget(self.font_color)

        self.mainVlay.addLayout(self.fontHLay)

    def set_row_count_to_ui(self, nodes_len):
#        self.table.setRowCount(len(nuke.selectedNodes()))
        self.table.setRowCount(nodes_len)
        print('row updated')

    def get_selected_node(self):
        check_nodes_ = nuke.selectedNodes()
        if len(check_nodes_) > 0:
            self.sel_nodes = nuke.selectedNodes()

    def get_nodes_info(self, nodes):     

        self.nodes_data = {}   

#        for index, node in enumerate(self.sel_nodes):
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
            
        
    def set_node_knobs_to_ui(self, add_row=None):
#        pprint(self.nodes_data)

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


        # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
        # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

        all_node_names = self.nodes_data.keys()
        print('all_node_names -- ', all_node_names)

        sorted_all_node_names = sorted(all_node_names)
        for row_index, node_nm in enumerate(sorted_all_node_names):

            if add_row:
               row_index = add_row

            node_nm_widget = QTableWidgetItem(node_nm)
            self.table.setItem(row_index, 0, node_nm_widget)

            if 'disable' in self.nodes_data[node_nm]:                
                bln = self.nodes_data[node_nm]['disable']
                disable_widget = QTableWidgetItem('Enabled')  
                self.set_chekckbox(bln, disable_widget, row_index, 1)


            if 'mix' in self.nodes_data[node_nm]:
                mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
                self.table.setItem(row_index, 2, mix_widget)

            if 'label' in self.nodes_data[node_nm]:
                label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
                self.table.setItem(row_index, 3, label_widget)

            if 'postage_stamp' in self.nodes_data[node_nm]:
                bln = self.nodes_data[node_nm]['postage_stamp']
                disable_widget = QTableWidgetItem('Enabled')  
                self.set_chekckbox(bln, disable_widget, row_index, 4)

            if 'colorspace' in self.nodes_data[node_nm]:
                self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

            if 'localizationPolicy' in self.nodes_data[node_nm]:
                self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

            if 'bookmark' in self.nodes_data[node_nm]:
                bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
                self.table.setItem(row_index, 7, bookmark_widget)

            if 'hide_input' in self.nodes_data[node_nm]:
                bln = self.nodes_data[node_nm]['hide_input']
                hide_input_widget = QTableWidgetItem('Enabled')  
                self.set_chekckbox(bln, hide_input_widget, row_index, 8)

            if 'lifetimeStart' in self.nodes_data[node_nm]:
                lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
                self.table.setItem(row_index, 9, lifetime_widget)

    def set_combo_companies(self, node_nm, knob_nm, row_index, col):
            self.colorspace_combobox = QComboBox()                
            values = nuke.toNode(node_nm)[knob_nm].values()
            self.colorspace_combobox.addItems(values)
            self.table.setCellWidget(row_index, col, self.colorspace_combobox)

    def set_chekckbox(self, bln, item_widget, row_index, col):

        item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        if bln:
            item_widget.setCheckState(Qt.CheckState.Checked)  
        else:    
            item_widget.setCheckState(Qt.CheckState.Unchecked)  
        self.table.setItem(row_index, col, item_widget)

        

    def btn_load_clicked(self):

        self.sel_nodes = None
        self.get_selected_node()

        if self.sel_nodes:
            self.btn_clear_clicked()

            nodes_len = len(nuke.selectedNodes())
            self.set_row_count_to_ui(nodes_len)

            nodes = nuke.selectedNodes()
            self.get_nodes_info(nodes)
            self.set_node_knobs_to_ui()
        else:
            nuke.message('Please Select Nodes')

        self.btn_add.setEnabled(True)
        print('row count --- ', self.table.rowCount())


    def btn_add_clicked(self):
        nodes = nuke.selectedNodes()
        for index, node in enumerate(nodes):
            bln = self.check_node_in_table(node)
            if bln:
                add_row = self.add_new_node(index, node)    
                self.get_nodes_info([node])
                self.set_node_knobs_to_ui(add_row)        

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
        self.btn_clear_clicked()

        nodes_len = len(nuke.allNodes())
        self.set_row_count_to_ui(nodes_len)

        nodes = nuke.allNodes()
        self.get_nodes_info(nodes)
        self.set_node_knobs_to_ui()      
        self.btn_add.setEnabled(False)
        print('row count --- ', self.table.rowCount())


    def btn_clear_clicked(self):
        self.table.clearContents()
        self.btn_add.setEnabled(False)
        print('row count --- ', self.table.rowCount())
        
        



def main():
    global window
#    app = QApplication(sys.argv)
    window = NodeOperator()
    window.show()
#    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

############################################################################














