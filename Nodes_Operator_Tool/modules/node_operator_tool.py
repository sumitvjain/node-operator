from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
from PySide2.QtGui import QPixmap, Qt
import sys, os
import nuke
from pprint import pprint

dir_path = os.path.dirname(__file__)
icons_dir_path = os.path.join(dir_path, 'icons')


class NodeOperator(QWidget):
    def __init__(self, parent=None):
        super(NodeOperator, self).__init__(parent)
        self.mainVlay = QVBoxLayout()  
        self.setLayout(self.mainVlay)

        self.sel_nodes = None
        self.nodes_data = {}

        self.set_top_btn_widgets()
        self.add_table()
        self.add_font_widget()

        self.init()

    # Signal & Slot
    def init(self):
        self.btn_load.clicked.connect(self.btn_load_clicked)
        
    def set_top_btn_widgets(self):

        self.hlay_1 = QHBoxLayout()
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setMinimumWidth(75)
        self.search_line_edit.setPlaceholderText('Find Node')

        # self.hspacer1 = QSpacerItem(50, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        # self.label_node_counts = QLabel('Nodes Added: ')
        # self.label_node_counts.setMinimumWidth(110)

        # self.hspacer2 = QSpacerItem(50, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.btn_load = QPushButton('Load Selected')
        self.btn_load.setMinimumWidth(80)
        # self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon')))
        # self.btn_load.setMaximumWidth(50)

        self.btn_add = QPushButton('Add')
        # self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))

        self.btn_all = QPushButton('Load All')
        # self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))

        self.btn_refresh = QPushButton('Refresh')
        # self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon')))
        
        self.btn_clear = QPushButton('Clear All')
        # self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))    

        self.hlay_1.addWidget(self.search_line_edit)
        # self.hlay_1.addSpacerItem(self.hspacer1)
        # self.hlay_1.addWidget(self.label_node_counts)
        # self.hlay_1.addSpacerItem(self.hspacer2)
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
        columns = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        for index, col_nm in enumerate(columns):
            table_item = QTableWidgetItem(col_nm)
            self.table.setHorizontalHeaderItem(index, table_item)
            
        
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.table.horizontalHeader().setSectionResizeMode(0, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(5, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(6, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(7, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(8, self.table.horizontalHeader().ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(9, self.table.horizontalHeader().ResizeToContents)
    

        self.table.verticalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # row = 0
        # for index, col_nm in enumerate(columns):
        #     self.table.setItem(row, index, QTableWidgetItem(col_nm))
       


        # self.tableVLay.addWidget(self.table)
        # self.mainVlay.addLayout(self.tableVLay)
        self.mainVlay.addWidget(self.table, stretch=1)

    def add_font_widget(self):
        self.fontHLay = QHBoxLayout()
        self.label_node_counts = QLabel('Nodes Added: ')
        self.label_node_counts.setMinimumWidth(110)

        font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
        self.font_combo = QComboBox()
        self.btn_bold = QPushButton('bold')
        self.btn_italic = QPushButton('italic')
        self.font_size = QLineEdit('11')
        self.font_size.setMaximumWidth(30)
        self.font_color = QPushButton('Color')

        self.fontHLay.addWidget(self.label_node_counts)
        self.fontHLay.addSpacerItem(font_spacer)
        self.fontHLay.addWidget(self.font_combo)
        self.fontHLay.addWidget(self.btn_bold)
        self.fontHLay.addWidget(self.btn_italic)
        self.fontHLay.addWidget(self.font_size)
        self.fontHLay.addWidget(self.font_color)

        self.mainVlay.addLayout(self.fontHLay)

    def set_row_count_to_ui(self):
        self.table.setRowCount(len(nuke.selectedNodes()))
        print('row updated')

    def get_selected_node(self):
        check_nodes_ = nuke.selectedNodes()
        if len(check_nodes_) > 0:
            self.sel_nodes = nuke.selectedNodes()

    def get_nodes_info(self):        
        for index, node in enumerate(self.sel_nodes):

            self.nodes_data['node_name'] = node.name()
            for knob in node.allKnobs():
                if knob.name() == 'disable':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['disable'].value()
                if knob.name() == 'mix':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['mix'].value()
                if knob.name() == 'label':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['label'].value()
                if knob.name() == 'postage_stamp':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['postage_stamp'].value()
                if knob.name() == 'colorspace':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['colorspace'].value()
                if knob.name() == 'localizationPolicy':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['localizationPolicy'].value()
                if knob.name() == 'bookmark':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['bookmark'].value()
                if knob.name() == 'hide_input':
                    self.nodes_data[f'{node.name()}_{knob.name()}'] = node['hide_input'].value()
                if knob.name() == 'lifetimeStart':
                    self.nodes_data[f'{node.name()}_lifetime'] = [node['lifetimeStart'].value(), node['lifetimeEnd'].value()]

            print('-'*50)
            pprint(self.nodes_data)    
            
        
    def set_node_knobs_to_ui(self):
        pass

    def btn_load_clicked(self):

        self.get_selected_node()

        if self.sel_nodes:
            self.set_row_count_to_ui()
            self.get_nodes_info()
            self.set_node_knobs_to_ui()


        else:
            nuke.message('Please Select Nodes')



def main():

    app = QApplication(sys.argv)
    window = NodeOperator()
    window.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()