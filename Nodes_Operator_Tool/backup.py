# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# import sys, os
# import nuke
# from pprint import pprint

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         # self.hspacer1 = QSpacerItem(50, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

#         # self.label_node_counts = QLabel('Nodes Added: ')
#         # self.label_node_counts.setMinimumWidth(110)

#         # self.hspacer2 = QSpacerItem(50, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setMinimumWidth(80)
#         # self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon')))
#         # self.btn_load.setMaximumWidth(50)

#         self.btn_add = QPushButton('Add')
#         # self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))

#         self.btn_all = QPushButton('Load All')
#         # self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))

#         self.btn_refresh = QPushButton('Refresh')
#         # self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon')))
        
#         self.btn_clear = QPushButton('Clear All')
#         # self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         # self.hlay_1.addSpacerItem(self.hspacer1)
#         # self.hlay_1.addWidget(self.label_node_counts)
#         # self.hlay_1.addSpacerItem(self.hspacer2)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)

        
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         columns = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         for index, col_nm in enumerate(columns):
#             table_item = QTableWidgetItem(col_nm)
#             self.table.setHorizontalHeaderItem(index, table_item)
            
        
#         self.table.horizontalHeader().setStretchLastSection(True)
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.table.horizontalHeader().setSectionResizeMode(0, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(1, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(2, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(3, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(4, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(5, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(6, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(7, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(8, self.table.horizontalHeader().ResizeToContents)
#         self.table.horizontalHeader().setSectionResizeMode(9, self.table.horizontalHeader().ResizeToContents)
    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         # row = 0
#         # for index, col_nm in enumerate(columns):
#         #     self.table.setItem(row, index, QTableWidgetItem(col_nm))
       


#         # self.tableVLay.addWidget(self.table)
#         # self.mainVlay.addLayout(self.tableVLay)
#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton('bold')
#         self.btn_italic = QPushButton('italic')

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)
#         self.font_color = QPushButton('Color')

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self):
#         self.table.setRowCount(len(nuke.selectedNodes()))
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self):        
#         # for index, node in enumerate(self.sel_nodes):

#         #     self.nodesself.nodes_data['node_name'] = node.name()
#         #     for knob in node.allKnobs():
#         #         if knob.name() == 'disable':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['disable'].value()
#         #         if knob.name() == 'mix':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['mix'].value()
#         #         if knob.name() == 'label':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['label'].value()
#         #         if knob.name() == 'postage_stamp':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['postage_stamp'].value()
#         #         if knob.name() == 'colorspace':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['colorspace'].value()
#         #         if knob.name() == 'localizationPolicy':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['localizationPolicy'].value()
#         #         if knob.name() == 'bookmark':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['bookmark'].value()
#         #         if knob.name() == 'hide_input':
#         #             self.nodesself.nodes_data[f'{node.name()}_{knob.name()}'] = node['hide_input'].value()
#         #         if knob.name() == 'lifetimeStart':
#         #             self.nodesself.nodes_data[f'{node.name()}_lifetime'] = [node['lifetimeStart'].value(), node['lifetimeEnd'].value()]

#         #     print('-'*50)
#         #     pprint(self.nodesself.nodes_data)    
#         for index, node in enumerate(self.sel_nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self):
#         pass

#     def btn_load_clicked(self):

#         self.get_selected_node()

#         if self.sel_nodes:
#             self.set_row_count_to_ui()
#             self.get_nodes_info()
#             self.set_node_knobs_to_ui()


#         else:
#             nuke.message('Please Select Nodes')



# def main():

#     app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
#     sys.exit(app.exec_())

# # if __name__ == '__main__':
# #     main()

# ####################################################################################################################################


# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         # self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))

#         self.btn_all = QPushButton('Load All')
#         # self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))

#         self.btn_refresh = QPushButton('Refresh')
#         # self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon')))
        
#         self.btn_clear = QPushButton('Clear All')
#         # self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton('bold')
#         self.btn_italic = QPushButton('italic')

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)
#         self.font_color = QPushButton('Color')

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self):
#         self.table.setRowCount(len(nuke.selectedNodes()))
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()
#         print('self.sel_nodes -- ', self.sel_nodes)

#     def get_nodes_info(self):     

#         self.nodes_data = {}   

#         for index, node in enumerate(self.sel_nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """

#         all_node_names = self.nodes_data.keys()
# #        row = 0
        
#         for index, key in enumerate(all_node_names):

#             for node_nm 
            
# #            for header_count, header_nm in enumerate(self.headers):
# #                QTableWidgetItem()


# #                node_nm = QTableWidgetItem(key)
# ##                self.table.setItem(row, 0, node_nm)
# ##                row += 1
# #                self.table.setItem(index, header_count, node_nm)
            

#     def btn_load_clicked(self):

#         self.get_selected_node()

#         if self.sel_nodes:
#             self.set_row_count_to_ui()
#             self.get_nodes_info()
#             self.set_node_knobs_to_ui()

#         else:
#             nuke.message('Please Select Nodes')



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# a = {'Read2': {'bookmark': False,
#            'colorspace': 'default',
#            'disable': False,
#            'label': '',
#            'lifetimeStart': 0.0,
#            'localizationPolicy': 'fromAutoLocalizePath',
#            'node_name': 'Read2',
#            'postage_stamp': True},
#  'Roto1': {'bookmark': False,
#            'disable': False,
#            'hide_input': False,
#            'label': '',
#            'lifetimeStart': 0.0,
#            'node_name': 'Roto1',
#            'postage_stamp': False}
# }


# for node_nm in a.keys():
#     if node_nm == 'Read2':
#         if 'colorspace' in a[node_nm]:
#             print(a[node_nm]['colorspace'])
#         else:
#             print('colorspace not available')




# ####################################################################################################

# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)

#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         # self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))

#         self.btn_all = QPushButton('Load All')
#         # self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))

#         self.btn_refresh = QPushButton('Refresh')
#         # self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon')))
        
#         self.btn_clear = QPushButton('Clear All')
#         # self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton('bold')
#         self.btn_italic = QPushButton('italic')

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)
#         self.font_color = QPushButton('Color')

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self):
#         self.table.setRowCount(len(nuke.selectedNodes()))
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()
# #        print('self.sel_nodes -- ', self.sel_nodes)

#     def get_nodes_info(self):     

#         self.nodes_data = {}   

#         for index, node in enumerate(self.sel_nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self):
#         pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'
#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:
# #                print('disable -- ', node_nm)
#                 disable_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['disable']))
#                 self.table.setItem(row_index, 1, disable_widget)

#             if 'colorspace' in self.nodes_data[node_nm]:
# #                print('colorspace  -- ', node_nm)
#                 colorspace_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['colorspace']))
#                 self.table.setItem(row_index, 5, colorspace_widget)
# #            print('--'*10)

# #            for key in b.keys():
# #                if 'hide_input' in b[key]:
# #                    print(f'Available -- {key}')
# #                else:
# #                    print(f'Not Available -- {key}')



# #        row = 0

# #        for index, key in enumerate(all_node_names):
# #
# #            for node_nm 
            
# #            for header_count, header_nm in enumerate(self.headers):
# #                QTableWidgetItem()


# #                node_nm = QTableWidgetItem(key)
# ##                self.table.setItem(row, 0, node_nm)
# ##                row += 1
# #                self.table.setItem(index, header_count, node_nm)
            

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

# #        print('self.sel_nodes --- ', self.sel_nodes)
#         if self.sel_nodes:
#             self.btn_clear_clicked()
#             self.set_row_count_to_ui()
#             self.get_nodes_info()
#             self.set_node_knobs_to_ui()

#         else:
#             nuke.message('Please Select Nodes')

#     def btn_clear_clicked(self):
#         self.table.clearContents()
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# #a = {'Read2': {'bookmark': False,
# #           'colorspace': 'default',
# #           'disable': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'localizationPolicy': 'fromAutoLocalizePath',
# #           'node_name': 'Read2',
# #           'postage_stamp': True},
# # 'Roto1': {'bookmark': False,
# #           'disable': False,
# #           'hide_input': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'node_name': 'Roto1',
# #           'postage_stamp': False}
# #}
# #
# #
# #for node_nm in a.keys():
# #    if node_nm == 'Read2':
# #        if 'colorspace' in a[node_nm]:
# #            print(a[node_nm]['colorspace'])
# #        else:
# #            print('colorspace not available')

# #
# #b = {'CheckerBoard2': {'bookmark': False,
# #                   'disable': False,
# #                   'label': '',
# #                   'lifetimeStart': 0.0,
# #                   'node_name': 'CheckerBoard2',
# #                   'postage_stamp': True},
# # 'Read3': {'bookmark': False,
# #           'colorspace': 'default',
# #           'disable': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'localizationPolicy': 'fromAutoLocalizePath',
# #           'node_name': 'Read3',
# #           'postage_stamp': True},
# # 'Write2': {'bookmark': False,
# #            'colorspace': 'default',
# #            'disable': False,
# #            'hide_input': False,
# #            'label': '',
# #            'lifetimeStart': 0.0,
# #            'node_name': 'Write2',
# #            'postage_stamp': False}}
# #
# #
# #for key in b.keys():
# #    if 'hide_input' in b[key]:
# #        print(f'Available -- {key}')
# #    else:
# #        print(f'Not Available -- {key}')


# #############################################################################################################################


# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)

#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
# #        self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton('bold')
#         self.btn_italic = QPushButton('italic')

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)
#         self.font_color = QPushButton('Color')

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self):
#         self.table.setRowCount(len(nuke.selectedNodes()))
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()
# #        print('self.sel_nodes -- ', self.sel_nodes)

#     def get_nodes_info(self):     

#         self.nodes_data = {}   

#         for index, node in enumerate(self.sel_nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self):
#         pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'
#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:
# #                print('disable -- ', node_nm)
#                 disable_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['disable']))
#                 self.table.setItem(row_index, 1, disable_widget)

#             if 'colorspace' in self.nodes_data[node_nm]:
# #                print('colorspace  -- ', node_nm)
#                 colorspace_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['colorspace']))
#                 self.table.setItem(row_index, 5, colorspace_widget)
# #            print('--'*10)

# #            for key in b.keys():
# #                if 'hide_input' in b[key]:
# #                    print(f'Available -- {key}')
# #                else:
# #                    print(f'Not Available -- {key}')



# #        row = 0

# #        for index, key in enumerate(all_node_names):
# #
# #            for node_nm 
            
# #            for header_count, header_nm in enumerate(self.headers):
# #                QTableWidgetItem()


# #                node_nm = QTableWidgetItem(key)
# ##                self.table.setItem(row, 0, node_nm)
# ##                row += 1
# #                self.table.setItem(index, header_count, node_nm)
            

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

# #        print('self.sel_nodes --- ', self.sel_nodes)
#         if self.sel_nodes:
#             self.btn_clear_clicked()
#             self.set_row_count_to_ui()
#             self.get_nodes_info()
#             self.set_node_knobs_to_ui()

#         else:
#             nuke.message('Please Select Nodes')

#     def btn_clear_clicked(self):
#         self.table.clearContents()
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# #a = {'Read2': {'bookmark': False,
# #           'colorspace': 'default',
# #           'disable': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'localizationPolicy': 'fromAutoLocalizePath',
# #           'node_name': 'Read2',
# #           'postage_stamp': True},
# # 'Roto1': {'bookmark': False,
# #           'disable': False,
# #           'hide_input': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'node_name': 'Roto1',
# #           'postage_stamp': False}
# #}
# #
# #
# #for node_nm in a.keys():
# #    if node_nm == 'Read2':
# #        if 'colorspace' in a[node_nm]:
# #            print(a[node_nm]['colorspace'])
# #        else:
# #            print('colorspace not available')

# #
# #b = {'CheckerBoard2': {'bookmark': False,
# #                   'disable': False,
# #                   'label': '',
# #                   'lifetimeStart': 0.0,
# #                   'node_name': 'CheckerBoard2',
# #                   'postage_stamp': True},
# # 'Read3': {'bookmark': False,
# #           'colorspace': 'default',
# #           'disable': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'localizationPolicy': 'fromAutoLocalizePath',
# #           'node_name': 'Read3',
# #           'postage_stamp': True},
# # 'Write2': {'bookmark': False,
# #            'colorspace': 'default',
# #            'disable': False,
# #            'hide_input': False,
# #            'label': '',
# #            'lifetimeStart': 0.0,
# #            'node_name': 'Write2',
# #            'postage_stamp': False}}
# #
# #
# #for key in b.keys():
# #    if 'hide_input' in b[key]:
# #        print(f'Available -- {key}')
# #    else:
# #        print(f'Not Available -- {key}')



# #####################################################################################################

# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)

#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
# #        self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton('bold')
#         self.btn_italic = QPushButton('italic')

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)
#         self.font_color = QPushButton('Color')

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self):
#         self.table.setRowCount(len(nuke.selectedNodes()))
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()
# #        print('self.sel_nodes -- ', self.sel_nodes)

#     def get_nodes_info(self):     

#         self.nodes_data = {}   

#         for index, node in enumerate(self.sel_nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self):
#         pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'
#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)
# #                disable_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
# #                if bln:
# #                    disable_widget.setCheckState(Qt.CheckState.Checked)  
# #                else:    
# #                    disable_widget.setCheckState(Qt.CheckState.Unchecked)  
# #                self.table.setItem(row_index, 1, disable_widget) 

#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
# #                thumb_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['postage_stamp']))
# #                self.table.setItem(row_index, 4, thumb_widget)
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 colorspace_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['colorspace']))
#                 self.table.setItem(row_index, 5, colorspace_widget)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 localize_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['localizationPolicy']))
#                 self.table.setItem(row_index, 6, localize_widget)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
# #                hide_input_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['hide_input']))
# #                self.table.setItem(row_index, 8, hide_input_widget)
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)


#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)

# #            print('--'*10)

# #            for key in b.keys():
# #                if 'hide_input' in b[key]:
# #                    print(f'Available -- {key}')
# #                else:
# #                    print(f'Not Available -- {key}')



# #        row = 0

# #        for index, key in enumerate(all_node_names):
# #
# #            for node_nm 
            
# #            for header_count, header_nm in enumerate(self.headers):
# #                QTableWidgetItem()


# #                node_nm = QTableWidgetItem(key)
# ##                self.table.setItem(row, 0, node_nm)
# ##                row += 1
# #                self.table.setItem(index, header_count, node_nm)
            

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

# #        print('self.sel_nodes --- ', self.sel_nodes)
#         if self.sel_nodes:
#             self.btn_clear_clicked()
#             self.set_row_count_to_ui()
#             self.get_nodes_info()
#             self.set_node_knobs_to_ui()

#         else:
#             nuke.message('Please Select Nodes')

#     def btn_clear_clicked(self):
#         self.table.clearContents()
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# #a = {'Read2': {'bookmark': False,
# #           'colorspace': 'default',
# #           'disable': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'localizationPolicy': 'fromAutoLocalizePath',
# #           'node_name': 'Read2',
# #           'postage_stamp': True},
# # 'Roto1': {'bookmark': False,
# #           'disable': False,
# #           'hide_input': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'node_name': 'Roto1',
# #           'postage_stamp': False}
# #}
# #
# #
# #for node_nm in a.keys():
# #    if node_nm == 'Read2':
# #        if 'colorspace' in a[node_nm]:
# #            print(a[node_nm]['colorspace'])
# #        else:
# #            print('colorspace not available')

# #
# #b = {'CheckerBoard2': {'bookmark': False,
# #                   'disable': False,
# #                   'label': '',
# #                   'lifetimeStart': 0.0,
# #                   'node_name': 'CheckerBoard2',
# #                   'postage_stamp': True},
# # 'Read3': {'bookmark': False,
# #           'colorspace': 'default',
# #           'disable': False,
# #           'label': '',
# #           'lifetimeStart': 0.0,
# #           'localizationPolicy': 'fromAutoLocalizePath',
# #           'node_name': 'Read3',
# #           'postage_stamp': True},
# # 'Write2': {'bookmark': False,
# #            'colorspace': 'default',
# #            'disable': False,
# #            'hide_input': False,
# #            'label': '',
# #            'lifetimeStart': 0.0,
# #            'node_name': 'Write2',
# #            'postage_stamp': False}}
# #
# #
# #for key in b.keys():
# #    if 'hide_input' in b[key]:
# #        print(f'Available -- {key}')
# #    else:
# #        print(f'Not Available -- {key}')


# ####################################################################################################


# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)

#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
# #        self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton('bold')
#         self.btn_italic = QPushButton('italic')

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)
#         self.font_color = QPushButton('Color')

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self):
#         self.table.setRowCount(len(nuke.selectedNodes()))
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()
# #        print('self.sel_nodes -- ', self.sel_nodes)

#     def get_nodes_info(self):     

#         self.nodes_data = {}   

#         for index, node in enumerate(self.sel_nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self):
#         pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'
#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)
# #                disable_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
# #                if bln:
# #                    disable_widget.setCheckState(Qt.CheckState.Checked)  
# #                else:    
# #                    disable_widget.setCheckState(Qt.CheckState.Unchecked)  
# #                self.table.setItem(row_index, 1, disable_widget) 

#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
# #                thumb_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['postage_stamp']))
# #                self.table.setItem(row_index, 4, thumb_widget)
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
# #                colorspace_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['colorspace']))
# #                self.table.setItem(row_index, 5, colorspace_widget)
# #                self.colorspace_combobox = QComboBox()                
# #                values = nuke.toNode(node_nm)['colorspace'].values()
# #                self.colorspace_combobox.addItems(values)
# #                self.table.setCellWidget(row_index, 5, self.colorspace_combobox)
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
# #                localize_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['localizationPolicy']))
# #                self.table.setItem(row_index, 6, localize_widget)
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
# #                hide_input_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['hide_input']))
# #                self.table.setItem(row_index, 8, hide_input_widget)
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)

# #            print('--'*10)

# #            for key in b.keys():
# #                if 'hide_input' in b[key]:
# #                    print(f'Available -- {key}')
# #                else:
# #                    print(f'Not Available -- {key}')



# #        row = 0

# #        for index, key in enumerate(all_node_names):
# #
# #            for node_nm 
            
# #            for header_count, header_nm in enumerate(self.headers):
# #                QTableWidgetItem()


# #                node_nm = QTableWidgetItem(key)
# ##                self.table.setItem(row, 0, node_nm)
# ##                row += 1
# #                self.table.setItem(index, header_count, node_nm)
            

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

# #        print('self.sel_nodes --- ', self.sel_nodes)
#         if self.sel_nodes:
#             self.btn_clear_clicked()
#             self.set_row_count_to_ui()
#             self.get_nodes_info()
#             self.set_node_knobs_to_ui()

#         else:
#             nuke.message('Please Select Nodes')

#     def btn_clear_clicked(self):
#         self.table.clearContents()
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################




# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# from PySide2.QtCore import QSize
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)

#         self.btn_all.clicked.connect(self.btn_all_clicked)

#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))
# #        self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.font_color = QPushButton('Color')
#         self.font_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.font_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self):
#         pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)

            

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#         else:
#             nuke.message('Please Select Nodes')

#         self.btn_add.setEnabled(True)
#         print('row count --- ', self.table.rowCount())



#     def btn_all_clicked(self):
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         print('row count --- ', self.table.rowCount())


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)
#         print('row count --- ', self.table.rowCount())
        
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################






# from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget, QInputDialog

# class TableExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Main Widget and Layout
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)
#         self.layout = QVBoxLayout(self.central_widget)

#         # QTableWidget
#         self.table = QTableWidget(3, 3)  # Start with 3 rows and 3 columns
#         self.table.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

#         # Add some initial items
#         self.table.setItem(0, 0, QTableWidgetItem("Item 1"))
#         self.table.setItem(1, 1, QTableWidgetItem("Item 2"))
#         self.table.setItem(2, 2, QTableWidgetItem("Item 3"))

#         # Add QPushButton
#         self.add_button = QPushButton("Add New Rows")
#         self.add_button.clicked.connect(self.add_new_rows)

#         # Layout management
#         self.layout.addWidget(self.table)
#         self.layout.addWidget(self.add_button)

#     def add_new_rows(self):
#         # Get user input for the number of rows to add
#         count, ok = QInputDialog.getInt(self, "Add Rows", "Enter the number of rows to add:", 1, 1, 100, 1)
#         if ok:  # If user clicks OK
#             for _ in range(count):
#                 self.add_new_row()

#     def add_new_row(self):
#         # Add a new row to the table
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)  # Insert a new row at the end

#         # Populate the new row with default values or empty items
# #        for col in range(self.table.columnCount()):
# #            self.table.setItem(current_row_count, col, QTableWidgetItem(f"New Item {current_row_count + 1}, {col + 1}"))

# if __name__ == "__main__":
# #    app = QApplication([])
#     window = TableExample()
#     window.show()
# #    app.exec_()


# ###############################################################################################################

# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# from PySide2.QtCore import QSize
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))
# #        self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.font_color = QPushButton('Color')
#         self.font_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.font_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()
#         print('all_node_names -- ', all_node_names)

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)

        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#         else:
#             nuke.message('Please Select Nodes')

#         self.btn_add.setEnabled(True)
#         print('row count --- ', self.table.rowCount())


#     def btn_add_clicked(self):
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             add_row = self.add_new_node(index, node)    
#             self.get_nodes_info([node])
#             print('working here --------------- ')
#             self.set_node_knobs_to_ui(add_row)        


#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         print('row count --- ', self.table.rowCount())


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)
#         print('row count --- ', self.table.rowCount())
        
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, Qt
# from PySide2.QtCore import QSize
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))
# #        self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()
#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.font_color = QPushButton('Color')
#         self.font_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.font_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()
#         print('all_node_names -- ', all_node_names)

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)

        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#         else:
#             nuke.message('Please Select Nodes')

#         self.btn_add.setEnabled(True)
#         print('row count --- ', self.table.rowCount())


#     def btn_add_clicked(self):
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)        

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         print('row count --- ', self.table.rowCount())


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)
#         print('row count --- ', self.table.rowCount())
        
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget,QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton, QFontComboBox
# from PySide2.QtGui import QPixmap, Qt
# from PySide2.QtCore import QSize
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))
# #        self.btn_load.setMinimumWidth(80)

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)
        
#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()

#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.font_color = QPushButton('Color')
#         self.font_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.font_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.font_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)        

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
        



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################


# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor
# from PySide2.QtCore import QSize
# import sys, os
# import nuke
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)

        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton('Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))
# #        color = QColor(101, 122, 255, 64)
# #        color = QColor(101, 255, 122, 64)
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_load.setStyleSheet(f"background-color: {rgba_style}; color: white;")
#         # 1080392447

#         self.btn_add = QPushButton('Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton('Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))

#         self.btn_refresh = QPushButton('Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton('Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)        

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font_size'].setValue(int(size))
#         else:
#             nuke.message('Please select node')

        
#     def btn_color_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             usr_sel_color = nuke.getColor() 
#             if usr_sel_color: 
#                 for node in nuke.selectedNodes():
#                     node['tile_color'].setValue(usr_sel_color)     
#         else:
#             nuke.message('Please select node')

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font'].setValue(font_nm)
#         else:
#             nuke.message('Please select node')

#     def btn_bold_clicked(self):

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             if self.btn_bold.isChecked():
#                 for node in nuke.selectedNodes():
#                     label_text = node['label'].value()                    
#                     bold_text = f"<b>{label_text}</b>"
#                     node['label'].setValue('')
#                     node['label'].setValue(bold_text)
#             else:
#                 for node in nuke.selectedNodes():
#                     label_text = node['label'].value()
#                     plane_text = label_text[3:-4]
#                     node['label'].setValue('')
#                     node['label'].setValue(plane_text)
#         else:
#             nuke.message('Please select node')



# #        if not self.btn_bold.isDown():
# #            self.btn_bold.setDown(False)
# #        else:
# #            self.btn_bold.setDown(False)
            
# #        n = nuke.selectedNode()
# #        bold_text = "<b>This is bold text</b>"
# #        n['label'].setValue(bold_text)
        

# #    def btn_bold_released(self):
# #        n = nuke.selectedNode()        
# #        n['label'].setValue('This is simple text')

# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################


# #n = nuke.selectedNode()
# #b = n['note_font']
# #b.setValueAt(False, 1)
# #
# #nuke.Font_Knob()
# #
# #
# #bold_text = "<b>This is bold text</b>"
# #n['label'].setValue(bold_text)
# #n['label'].setValue('This is bold text')
# #


# ######################################################################################################################


# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)

        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)
#             else:
#                 self.set_cur_table_item_read_only(row_index, 2)

#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#     def set_cur_table_item_read_only(self, row_index, col):
#         read_item = self.table.item(row_index, col)
#         print('read_item ----------- ', read_item)
# #        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#     def make_first_column_read_only(self):
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
#             print('read_item ================== ', read_item)


#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#         self.make_first_column_read_only()      

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font_size'].setValue(int(size))
#         else:
#             nuke.message('Please select node')

        
#     def btn_color_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             usr_sel_color = nuke.getColor() 
#             if usr_sel_color: 
#                 for node in nuke.selectedNodes():
#                     node['tile_color'].setValue(usr_sel_color)     
#         else:
#             nuke.message('Please select node')

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font'].setValue(font_nm)
#         else:
#             nuke.message('Please select node')

#     def btn_bold_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             if self.btn_bold.isChecked():
#                 self.update_text_pattern('bold')
#             else:
#                 self.update_text_pattern()
#         else:
#             nuke.message('Please select node')

#     def update_text_pattern(self, bold=None):
#         for node in nuke.selectedNodes():
#             label_text = node['label'].value()    
#             pattern = r"</?b>"
#             cleaned_string = re.sub(pattern, "", label_text) 

#             if bold:
#                 bold_text = f"<b>{cleaned_string}</b>"
#                 node['label'].setValue('')
#                 node['label'].setValue(bold_text)
#             else:
#                 node['label'].setValue('')
#                 node['label'].setValue(cleaned_string)


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################





# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)

        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

# #    def set_cur_table_item_read_only(self, row_index, col):
# #        read_item = self.table.item(row_index, col)
# #        print('read_item ----------- ', read_item)
# ##        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#     def make_first_column_read_only(self):
        
#         for row in range(self.table.rowCount()):
# #            read_item = self.table.item(row, 3)
# #            read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #            print('read_item ================== ', read_item)

#             for col in range(self.table.columnCount()):
#                 if not col == 3:
#                     read_item = self.table.item(row, col)
#                     read_item.whatsThis
#                     # read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

# #                    read_item = self.table.item(row, col)
# ##                    print('read item value -- ', read_item)
# #                    if read_item == None:
# #                        print(f'{row} - {col}')
# #                        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #
# ##                print('read item value -- ', read_item)
# #            print('=*='*25)


#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#         self.make_first_column_read_only()      

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()
#         self.btn_all.setEnabled(True)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font_size'].setValue(int(size))
#         else:
#             nuke.message('Please select node')

        
#     def btn_color_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             usr_sel_color = nuke.getColor() 
#             if usr_sel_color: 
#                 for node in nuke.selectedNodes():
#                     node['tile_color'].setValue(usr_sel_color)     
#         else:
#             nuke.message('Please select node')

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font'].setValue(font_nm)
#         else:
#             nuke.message('Please select node')

#     def btn_bold_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             if self.btn_bold.isChecked():
#                 self.update_text_pattern('bold')
#             else:
#                 self.update_text_pattern()
#         else:
#             nuke.message('Please select node')

#     def update_text_pattern(self, bold=None):
#         for node in nuke.selectedNodes():
#             label_text = node['label'].value()    
#             pattern = r"</?b>"
#             cleaned_string = re.sub(pattern, "", label_text) 

#             if bold:
#                 bold_text = f"<b>{cleaned_string}</b>"
#                 node['label'].setValue('')
#                 node['label'].setValue(bold_text)
#             else:
#                 node['label'].setValue('')
#                 node['label'].setValue(cleaned_string)


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################







# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_top_btn_widgets()
#         self.add_table()
#         self.add_font_widget()

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)

        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

# #    def set_cur_table_item_read_only(self, row_index, col):
# #        read_item = self.table.item(row_index, col)
# #        print('read_item ----------- ', read_item)
# ##        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#     def make_first_column_read_only(self):
        
#         for row in range(self.table.rowCount()):
#            read_item = self.table.item(row, 3)
#            read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #            print('read_item ================== ', read_item)

#             # for col in range(self.table.columnCount()):
#             #     if not col == 3:
#             #         read_item = self.table.item(row, col)
#                     # read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

# #                    read_item = self.table.item(row, col)
# ##                    print('read item value -- ', read_item)
# #                    if read_item == None:
# #                        print(f'{row} - {col}')
# #                        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #
# ##                print('read item value -- ', read_item)
# #            print('=*='*25)


#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#         self.make_first_column_read_only()      

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()
#         self.btn_all.setEnabled(True)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font_size'].setValue(int(size))
#         else:
#             nuke.message('Please select node')

        
#     def btn_color_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             usr_sel_color = nuke.getColor() 
#             if usr_sel_color: 
#                 for node in nuke.selectedNodes():
#                     node['tile_color'].setValue(usr_sel_color)     
#         else:
#             nuke.message('Please select node')

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font'].setValue(font_nm)
#         else:
#             nuke.message('Please select node')

#     def btn_bold_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             if self.btn_bold.isChecked():
#                 self.update_text_pattern('bold')
#             else:
#                 self.update_text_pattern()
#         else:
#             nuke.message('Please select node')

#     def update_text_pattern(self, bold=None):
#         for node in nuke.selectedNodes():
#             label_text = node['label'].value()    
#             pattern = r"</?b>"
#             cleaned_string = re.sub(pattern, "", label_text) 

#             if bold:
#                 bold_text = f"<b>{cleaned_string}</b>"
#                 node['label'].setValue('')
#                 node['label'].setValue(bold_text)
#             else:
#                 node['label'].setValue('')
#                 node['label'].setValue(cleaned_string)


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()    

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         headerSpacer1 = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)

#         headerLabel = QLabel('NODE OPERATIOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel("Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         self.headerSpacer2 = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)

#         self.headerHlay.addSpacerItem(headerSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)



#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

# #    def set_cur_table_item_read_only(self, row_index, col):
# #        read_item = self.table.item(row_index, col)
# #        print('read_item ----------- ', read_item)
# ##        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#     def make_first_column_read_only(self):
        
#         for row in range(self.table.rowCount()):
#            read_item = self.table.item(row, 3)
#            read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #            print('read_item ================== ', read_item)

#             # for col in range(self.table.columnCount()):
#             #     if not col == 3:
#             #         read_item = self.table.item(row, col)
#                     # read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

# #                    read_item = self.table.item(row, col)
# ##                    print('read item value -- ', read_item)
# #                    if read_item == None:
# #                        print(f'{row} - {col}')
# #                        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #
# ##                print('read item value -- ', read_item)
# #            print('=*='*25)


#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#         self.make_first_column_read_only()      

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()
#         self.btn_all.setEnabled(True)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font_size'].setValue(int(size))
#         else:
#             nuke.message('Please select node')

        
#     def btn_color_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             usr_sel_color = nuke.getColor() 
#             if usr_sel_color: 
#                 for node in nuke.selectedNodes():
#                     node['tile_color'].setValue(usr_sel_color)     
#         else:
#             nuke.message('Please select node')

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font'].setValue(font_nm)
#         else:
#             nuke.message('Please select node')

#     def btn_bold_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             if self.btn_bold.isChecked():
#                 self.update_text_pattern('bold')
#             else:
#                 self.update_text_pattern()
#         else:
#             nuke.message('Please select node')

#     def update_text_pattern(self, bold=None):
#         for node in nuke.selectedNodes():
#             label_text = node['label'].value()    
#             pattern = r"</?b>"
#             cleaned_string = re.sub(pattern, "", label_text) 

#             if bold:
#                 bold_text = f"<b>{cleaned_string}</b>"
#                 node['label'].setValue('')
#                 node['label'].setValue(bold_text)
#             else:
#                 node['label'].setValue('')
#                 node['label'].setValue(cleaned_string)


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################








# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         headerSpacer1 = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)

#         headerLabel = QLabel('NODE OPERATIOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel("Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         self.headerSpacer2 = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)

#         self.headerHlay.addSpacerItem(headerSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton()
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton()
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
#         self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.verticalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.mainVlay.addWidget(self.table, stretch=1)



#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

# #    def set_cur_table_item_read_only(self, row_index, col):
# #        read_item = self.table.item(row_index, col)
# #        print('read_item ----------- ', read_item)
# ##        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#     def make_first_column_read_only(self):
        
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
#             print('read_item ================== ', read_item)

# #            for col in range(self.table.columnCount()):
# #                if not col == 3:
# #                    read_item = self.table.item(row, col)
# #                    read_item.whatsThis
#                     # read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

# #                    read_item = self.table.item(row, col)
# ##                    print('read item value -- ', read_item)
# #                    if read_item == None:
# #                        print(f'{row} - {col}')
# #                        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #
# ##                print('read item value -- ', read_item)
# #            print('=*='*25)


#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#         self.make_first_column_read_only()      

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()
#         self.btn_all.setEnabled(True)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font_size'].setValue(int(size))
#         else:
#             nuke.message('Please select node')

        
#     def btn_color_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             usr_sel_color = nuke.getColor() 
#             if usr_sel_color: 
#                 for node in nuke.selectedNodes():
#                     node['tile_color'].setValue(usr_sel_color)     
#         else:
#             nuke.message('Please select node')

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             for node in nuke.selectedNodes():
#                  node['note_font'].setValue(font_nm)
#         else:
#             nuke.message('Please select node')

#     def btn_bold_clicked(self):
#         nodes_len = len(nuke.selectedNodes())
#         if nodes_len:
#             if self.btn_bold.isChecked():
#                 self.update_text_pattern('bold')
#             else:
#                 self.update_text_pattern()
#         else:
#             nuke.message('Please select node')

#     def update_text_pattern(self, bold=None):
#         for node in nuke.selectedNodes():
#             label_text = node['label'].value()    
#             pattern = r"</?b>"
#             cleaned_string = re.sub(pattern, "", label_text) 

#             if bold:
#                 bold_text = f"<b>{cleaned_string}</b>"
#                 node['label'].setValue('')
#                 node['label'].setValue(bold_text)
#             else:
#                 node['label'].setValue('')
#                 node['label'].setValue(cleaned_string)


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################






# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         # headerSpacer1 = QSpacerItem(100, 2, QSizePolicy.Maximum)
#         horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         headerLabel = QLabel('NODE OPERATOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel(" -  Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         # headerSpacer2 = QSpacerItem(100, 2, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         # headerSpacer2 = QSpacerItem(100, 2, QSizePolicy.Maximum)
#         horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         self.headerHlay.addSpacerItem(horizontalSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)
#         self.headerHlay.addSpacerItem(horizontalSpacer2)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

# #        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
# #        self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.horizontalHeader().setStretchLastSection(True) 
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


# #        self.table.verticalHeader().setStretchLastSection(False)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

#         self.mainVlay.addWidget(self.table, stretch=1)

#         print('=*='*10)
#         for i in dir(self.table):
#             print(i)
#         print('=*='*10)


#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#             self.table.setRowHeight(row_index, (row_index+2) * 16)

 

# #    def set_cur_table_item_read_only(self, row_index, col):
# #        read_item = self.table.item(row_index, col)
# #        print('read_item ----------- ', read_item)
# ##        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)a

#     def make_first_column_read_only(self):
        
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
#             print('read_item ================== ', read_item)

# #            for col in range(self.table.columnCount()):
# #                if not col == 3:
# #                    read_item = self.table.item(row, col)
# #                    read_item.whatsThis
#                     # read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

# #                    read_item = self.table.item(row, col)
# ##                    print('read item value -- ', read_item)
# #                    if read_item == None:
# #                        print(f'{row} - {col}')
# #                        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #
# ##                print('read item value -- ', read_item)
# #            print('=*='*25)


#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#         self.make_first_column_read_only()      

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()
#         self.btn_all.setEnabled(True)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

# #        nodes_len = len(nuke.selectedNodes())
# #        if nodes_len:
# #            for node in nuke.selectedNodes():
# #                 node['note_font_size'].setValue(int(size))
# #        else:
# #            nuke.message('Please select node')

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')
        
#     def btn_color_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             usr_sel_color = nuke.getColor() 

#             if usr_sel_color: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 
# ############################################################################################

# #        nodes_len = len(nuke.selectedNodes())
# #        if nodes_len:
# #            usr_sel_color = nuke.getColor() 
# #            if usr_sel_color: 
# #                for node in nuke.selectedNodes():
# #                    node['tile_color'].setValue(usr_sel_color)     
# #        else:
# #            nuke.message('Please select node')

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

# #        nodes_len = len(nuke.selectedNodes())
# #        if nodes_len:
# #            for node in nuke.selectedNodes():
# #                 node['note_font'].setValue(font_nm)
# #        else:
# #            nuke.message('Please select node')
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font'].setValue(font_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def btn_bold_clicked(self):
# #        nodes_len = len(nuke.selectedNodes())
# #        if nodes_len:
# #            if self.btn_bold.isChecked():
# #                self.update_text_pattern('bold')
# #            else:
# #                self.update_text_pattern()
# #        else:
# #            nuke.message('Please select node')

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_bold.isChecked():
#                     self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
#                 else:
#                     self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_text_pattern(self, bold=None, sel_item_nm=None):
# #        for node in nuke.selectedNodes():
# #            label_text = node['label'].value()    
# #            pattern = r"</?b>"
# #            cleaned_string = re.sub(pattern, "", label_text) 
# #
# #            if bold:
# #                bold_text = f"<b>{cleaned_string}</b>"
# #                node['label'].setValue('')
# #                node['label'].setValue(bold_text)
# #            else:
# #                node['label'].setValue('')
# #                node['label'].setValue(cleaned_string)

# #        for node in nuke.selectedNodes():

# #        for node_nm in sel_item_nm:
# #            if nuke.toNode(node_nm):
# #                label_text = nuke.toNode(node_nm)['label'].value()   
# #                pattern = r"</?b>"
# #                cleaned_string = re.sub(pattern, "", label_text) 
# #    
# #                if bold:
# #                    bold_text = f"<b>{cleaned_string}</b>"
# #                    nuke.toNode(node_nm)['label'].setValue('')
# #                    nuke.toNode(node_nm)['label'].setValue(bold_text)
# #                else:
# #                    nuke.toNode(node_nm)['label'].setValue('')
# #                    nuke.toNode(node_nm)['label'].setValue(cleaned_string)


#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):
# #                label_text = nuke.toNode(node_nm)['label'].value()   
# #                pattern = r"</?b>"
# #                cleaned_string = re.sub(pattern, "", label_text) 
    
#                 if bold:
# #                    bold_text = f"<b>{cleaned_string}</b>"
#                     nuke.toNode(node_nm)['note_font'].setValue('bold')
# #                    nuke.toNode(node_nm)['label'].setValue(bold_text)
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")
# #                    nuke.toNode(node_nm)['label'].setValue(cleaned_string)


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################





# #n = nuke.selectedNode()
# #
# #n_node_font = n['note_font']
# #n_node_font.setValue('bold')
# #n_node_font.setValue('')
# #
# #
# #import nuke
# #
# ## Get the selected node
# #n = nuke.selectedNode()
# #
# ## Check if the selected node has the 'note_font' knob
# #if 'note_font' in n.knobs():
# #    # Set the note font to italic
# #    # Available font styles can include "italic", "bold", etc., depending on the environment
# #    n['note_font'].setValue("italic")
# #    # Set a label as an example
# #    n['label'].setValue("This is an italic label")
# #    print("Node label set to italic.")
# #else:
# #    print("The selected node does not have a 'note_font' knob.")
# #


# ##############################################################################################

# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)
#         self.btn_italic.clicked.connect(self.btn_italic_clicked)

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         # headerSpacer1 = QSpacerItem(100, 2, QSizePolicy.Maximum)
#         horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         headerLabel = QLabel('NODE OPERATOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel(" -  Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         # headerSpacer2 = QSpacerItem(100, 2, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         # headerSpacer2 = QSpacerItem(100, 2, QSizePolicy.Maximum)
#         horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         self.headerHlay.addSpacerItem(horizontalSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)
#         self.headerHlay.addSpacerItem(horizontalSpacer2)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_node_counts = QLabel('Nodes Added: ')
#         self.label_node_counts.setMinimumWidth(110)

#         font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)
#         self.btn_italic.setCheckable(True)
#         self.btn_italic.setChecked(False)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_node_counts)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

# #        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
# #        self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.horizontalHeader().setStretchLastSection(True) 
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


# #        self.table.verticalHeader().setStretchLastSection(False)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

#         self.mainVlay.addWidget(self.table, stretch=1)

#         print('=*='*10)
#         for i in dir(self.table):
#             print(i)
#         print('=*='*10)


#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:                
#                 bln = self.nodes_data[node_nm]['disable']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 1)


#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 disable_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, disable_widget, row_index, 4)

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 self.table.setItem(row_index, 7, bookmark_widget)

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 hide_input_widget = QTableWidgetItem('Enabled')  
#                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#             self.table.setRowHeight(row_index, (row_index+2) * 16)

 

# #    def set_cur_table_item_read_only(self, row_index, col):
# #        read_item = self.table.item(row_index, col)
# #        print('read_item ----------- ', read_item)
# ##        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)a

#     def make_first_column_read_only(self):
        
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
#             print('read_item ================== ', read_item)

# #            for col in range(self.table.columnCount()):
# #                if not col == 3:
# #                    read_item = self.table.item(row, col)
# #                    read_item.whatsThis
#                     # read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

# #                    read_item = self.table.item(row, col)
# ##                    print('read item value -- ', read_item)
# #                    if read_item == None:
# #                        print(f'{row} - {col}')
# #                        read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)
# #
# ##                print('read item value -- ', read_item)
# #            print('=*='*25)


#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)
            

#     def set_chekckbox(self, bln, item_widget, row_index, col):

#         item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         if bln:
#             item_widget.setCheckState(Qt.CheckState.Checked)  
#         else:    
#             item_widget.setCheckState(Qt.CheckState.Unchecked)  
#         self.table.setItem(row_index, col, item_widget)
        

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#         self.make_first_column_read_only()      

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()
#         self.btn_all.setEnabled(True)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.btn_add.setEnabled(False)

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')
        
#     def btn_color_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             usr_sel_color = nuke.getColor() 

#             if usr_sel_color: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 


#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font'].setValue(font_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_text_pattern(self, bold=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if bold:
#                     nuke.toNode(node_nm)['note_font'].setValue('bold')
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_bold_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_bold.isChecked():
#                     self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
#                 else:
#                     self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')


#     def update_italic_pattern(self, italic=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if italic:
#                     nuke.toNode(node_nm)['note_font'].setValue('italic')
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_italic_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_italic.isChecked():
#                     self.update_italic_pattern(italic='italic', sel_item_nm=sel_item_nm)            
#                 else:
#                      self.update_italic_pattern(italic=None, sel_item_nm=sel_item_nm)            
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################





# #n = nuke.selectedNode()
# #
# #n_node_font = n['note_font']
# #n_node_font.setValue('bold')
# #n_node_font.setValue('')
# #
# #
# #import nuke
# #
# ## Get the selected node
# #n = nuke.selectedNode()
# #
# ## Check if the selected node has the 'note_font' knob
# #if 'note_font' in n.knobs():
# #    # Set the note font to italic
# #    # Available font styles can include "italic", "bold", etc., depending on the environment
# #    n['note_font'].setValue("italic")
# #    # Set a label as an example
# #    n['label'].setValue("This is an italic label")
# #    print("Node label set to italic.")
# #else:
# #    print("The selected node does not have a 'note_font' knob.")
# #





# ##########################################################################################################################

# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')




# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)
#         self.btn_italic.clicked.connect(self.btn_italic_clicked)
#         self.table.cellChanged.connect(self.on_cell_changed)

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         # headerSpacer1 = QSpacerItem(100, 2, QSizePolicy.Maximum)
#         horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         headerLabel = QLabel('NODE OPERATOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel(" -  Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         # headerSpacer2 = QSpacerItem(100, 2, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         # headerSpacer2 = QSpacerItem(100, 2, QSizePolicy.Maximum)
#         horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         self.headerHlay.addSpacerItem(horizontalSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)
#         self.headerHlay.addSpacerItem(horizontalSpacer2)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_nodes_added = QLabel('Nodes Added : ')    
#         self.label_nodes_count = QLabel('')
#         # self.label_nodes_count.setMinimumWidth(110)

#         # font_spacer = QSpacerItem(50, 5, QSizePolicy.Maximum, QSizePolicy.Expanding)
#         font_spacer = QSpacerItem(2000, 10, QSizePolicy.Maximum)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)
#         self.btn_italic.setCheckable(True)
#         self.btn_italic.setChecked(False)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_nodes_added)
#         self.fontHLay.addWidget(self.label_nodes_count)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         # self.tableVLay = QVBoxLayout()
#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'On/Off', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)

# #        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
# #        self.table.horizontalHeader().setStretchLastSection(True)    

#         self.table.horizontalHeader().setStretchLastSection(True) 
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


# #        self.table.verticalHeader().setStretchLastSection(False)
#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

#         self.mainVlay.addWidget(self.table, stretch=1)

#         print('=*='*10)
#         for i in dir(self.table):
#             print(i)
#         print('=*='*10)

#     def set_nodes_count(self, nodes_len):
#         self.label_nodes_count.setText(str(nodes_len))

#     def set_row_count_to_ui(self, nodes_len):
# #        self.table.setRowCount(len(nuke.selectedNodes()))
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

# #        for index, node in enumerate(self.sel_nodes):
#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()
            
        
#     def set_node_knobs_to_ui(self, add_row=None):
# #        pprint(self.nodes_data)

#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         # 'Node Name', 'Disabled', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime'
#         # 'disable', 'mix', 'label', 'postage_stamp', 'colorspace', 'localizationPolicy', 'bookmark', 'hide_input', 'lifetimeStart'

#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:    
#                 pass            
#                 # bln = self.nodes_data[node_nm]['disable']
#                 # if bln:
#                 #     disable_widget = QTableWidgetItem('Enabled')
#                 # else:  
#                 #     disable_widget = QTableWidgetItem('Disabled') 
#                 # self.set_chekckbox(bln, disable_widget, row_index, 1)

#                 bln = self.nodes_data[node_nm]['disable']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 1)
#                 else:  
#                     self.set_chekckbox(False, row_index, 1)                    

#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 # bln = self.nodes_data[node_nm]['postage_stamp']  # ['postage_stamp'].value()
#                 # if bln:
#                 #     disable_widget = QTableWidgetItem('Enabled')
#                 # else:  
#                 #     disable_widget = QTableWidgetItem('Disabled')
#                 # self.set_chekckbox(bln, disable_widget, row_index, 4)
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 4)
#                 else:  
#                     self.set_chekckbox(False, row_index, 4)  

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 # bookmark_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['bookmark']))
#                 # self.table.setItem(row_index, 7, bookmark_widget)
#                 bln = self.nodes_data[node_nm]['bookmark']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 7)
#                 else:  
#                     self.set_chekckbox(False, row_index, 7)                  

#             if 'hide_input' in self.nodes_data[node_nm]:
# #                 bln = self.nodes_data[node_nm]['hide_input']
# # #                hide_input_widget = QTableWidgetItem('Enabled')  
# #                 if bln:
# #                     hide_input_widget = QTableWidgetItem('Enabled')
# #                 else:  
# #                     hide_input_widget = QTableWidgetItem('Disabled')
# #                 self.set_chekckbox(bln, hide_input_widget, row_index, 8)

#                 bln = self.nodes_data[node_nm]['hide_input']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 8)
#                 else:  
#                     self.set_chekckbox(False, row_index, 8)  

#             if 'lifetimeStart' in self.nodes_data[node_nm]:
#                 lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 self.table.setItem(row_index, 9, lifetime_widget)

#             self.table.setRowHeight(row_index, (row_index+2) * 16)

#     def update_checkbox_status(self,nod_nm, row, column, checkbox, state):
#         # print('cb -- ', cb)
#         # print('state -- ', state)
#         # print('row -- ', row)
#         # print('column -- ', column)
#         if state == Qt.Checked:
#             checkbox.setText('Enabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(True)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(True)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(True)                

#         else:
#             checkbox.setText('Disabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(False)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(False)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(False)                  

#     def set_chekckbox(self, bln, row_index, col):    
#             checkbox_widget = QWidget()
#             checkbox_layout = QHBoxLayout(checkbox_widget)
#             checkbox_layout.setContentsMargins(0,0,0,0)
#             checkbox_layout.setAlignment(Qt.AlignCenter)

#             changed_val_nod_nm = self.table.item(row_index, 0).text()

#             if bln:
#                 checkbox = QCheckBox('Enabled')
#                 checkbox.setChecked(True)
#             else:
#                 checkbox = QCheckBox('Disabled')
#                 checkbox.setChecked(False)

#             checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))

#             checkbox_layout.addWidget(checkbox)
#             self.table.setCellWidget(row_index, col, checkbox_widget)


#     # def set_chekckbox(self, bln, item_widget, row_index, col):

#     #     item_widget.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#     #     if bln:
#     #         item_widget.setCheckState(Qt.CheckState.Checked)  
#     #     else:    
#     #         item_widget.setCheckState(Qt.CheckState.Unchecked)  
#     #     self.table.setItem(row_index, col, item_widget)

#     #    checkbox_widget = QCheckBox()
#     #    checkbox_widget.stateChanged.connect(lambda state, r=row_index: self.on_checkbox_changed(r, col, state))
#     #    self.table.setCellWidget(row_index, col, checkbox_widget)


#     def update_node_value(self, nod_nm, c_row, c_col, c_val):
#         nuke_node = nuke.toNode(nod_nm)
# #        print('c_col type -- ', type(c_col))
# #        print('not name   ', nuke_node.name())
#         if c_col == 0:
#             pass
#         elif c_col == 1:
#             pass
#         elif c_col == 2: # mix
#             if nuke_node['mix']:
#                 nuke_node['mix'].setValue(float(c_val))
#         else:
#             pass     

#     def on_cell_changed(self, row, column):
#         item = self.table.item(row, column)
#         if item:
#             changed_row = row
#             changed_column =  column
#             changed_value = item.text()
#             changed_val_nod_nm = self.table.item(row, 0).text()

# #            print('changed_val_nod_nm -- ', changed_val_nod_nm)
# #            print('changed_row -- ', changed_row)
# #            print('changed_column -- ', changed_column)
# #            print('changed_value -- ', changed_value)
#             self.update_node_value(changed_val_nod_nm, changed_row, changed_column, changed_value)



#     def make_first_column_read_only(self):
        
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_node_knobs_to_ui()
#             self.make_first_column_read_only()

#             self.set_nodes_count(nodes_len)
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)


#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         add_count = 0
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_node_knobs_to_ui(add_row)  
#                 add_count += 1
#         self.make_first_column_read_only()   

#         nodes_len = add_count + int(self.label_nodes_count.text())
#         self.set_nodes_count(str(nodes_len))

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        

#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_node_knobs_to_ui()      
#         self.btn_add.setEnabled(False)
#         self.make_first_column_read_only()
#         self.btn_all.setEnabled(True)

#         self.set_nodes_count(nodes_len)


#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.table.setRowCount(0)
#         self.table.setColumnCount(10)
#         self.btn_add.setEnabled(False)
#         self.set_nodes_count('')

        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')
        
#     def btn_color_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             usr_sel_color = nuke.getColor() 

#             if usr_sel_color: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 


#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font'].setValue(font_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_text_pattern(self, bold=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if bold:
#                     nuke.toNode(node_nm)['note_font'].setValue('bold')
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_bold_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_bold.isChecked():
#                     self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
#                 else:
#                     self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')


#     def update_italic_pattern(self, italic=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if italic:
#                     nuke.toNode(node_nm)['note_font'].setValue('italic')
#                     print('pressed for italic')
#                 else:
#                     print('released for italic')
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_italic_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_italic.isChecked():
#                     self.update_italic_pattern(italic='italic', sel_item_nm=sel_item_nm)            
#                 else:
#                      self.update_italic_pattern(italic=None, sel_item_nm=sel_item_nm)            
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')


    
            



# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################




# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)
#         self.btn_italic.clicked.connect(self.btn_italic_clicked)
#         self.table.cellChanged.connect(self.on_cell_changed)
#         self.table.cellDoubleClicked.connect(self.on_cellDoubleClicked)

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         headerLabel = QLabel('NODE OPERATOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel(" -  Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         self.headerHlay.addSpacerItem(horizontalSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)
#         self.headerHlay.addSpacerItem(horizontalSpacer2)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_nodes_added = QLabel('Nodes Added : ')    
#         self.label_nodes_count = QLabel('')

#         font_spacer = QSpacerItem(2000, 10, QSizePolicy.Maximum)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)
#         self.btn_italic.setCheckable(True)
#         self.btn_italic.setChecked(False)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_nodes_added)
#         self.fontHLay.addWidget(self.label_nodes_count)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'On/Off', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)  

#         self.table.horizontalHeader().setStretchLastSection(True) 
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

#         self.mainVlay.addWidget(self.table, stretch=1)

#         # print('=*='*10)
#         # for i in dir(self.table):
#         #     print(i)
#         # print('=*='*10)

#     def set_nodes_count(self, nodes_len):
#         self.label_nodes_count.setText(str(nodes_len))

#     def set_row_count_to_ui(self, nodes_len):
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()    

#                 if knob.name() == 'lifetimeEnd':
#                     self.nodes_data[node_name]['lifetimeEnd'] = node['lifetimeEnd'].value()
                  
#     def set_ui_with_knobs(self, add_row=None):
#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:           
#                 bln = self.nodes_data[node_nm]['disable']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 1)
#                 else:  
#                     self.set_chekckbox(False, row_index, 1)                    

#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 4)
#                 else:  
#                     self.set_chekckbox(False, row_index, 4)  

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['bookmark']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 7)
#                 else:  
#                     self.set_chekckbox(False, row_index, 7)                  

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 8)
#                 else:  
#                     self.set_chekckbox(False, row_index, 8)  

#             if 'lifetimeStart' in self.nodes_data[node_nm]:

#                 # if self.nodes_data[node_nm]['lifetimeStart'] == 0.0:
#                 #     lifetime_widget = QTableWidgetItem('default')
#                 # else:
#                 #     lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))

#                 life_start = int(self.nodes_data[node_nm]['lifetimeStart'])
#                 life_end = int(self.nodes_data[node_nm]['lifetimeEnd'])
#                 # lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeStart']))
#                 # lifetime_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['lifetimeEnd']))
#                 lifetime_widget = QTableWidgetItem(f'{life_start}.{life_end}')
#                 if life_start != 0 or life_end != 0:
#                     lifetime_widget.setBackground(QColor(110, 106, 94))
#                 self.table.setItem(row_index, 9, lifetime_widget)
  

#             self.table.setRowHeight(row_index, (row_index+2) * 16)

#     def update_checkbox_status(self,nod_nm, row, column, checkbox, state):
#         if state == Qt.Checked:
#             checkbox.setText('Enabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(True)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(True)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(True)                

#         else:
#             checkbox.setText('Disabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(False)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(False)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(False)                  

#     def set_chekckbox(self, bln, row_index, col):    
#             checkbox_widget = QWidget()
#             checkbox_layout = QHBoxLayout(checkbox_widget)
#             checkbox_layout.setContentsMargins(0,0,0,0)
#             checkbox_layout.setAlignment(Qt.AlignCenter)

#             changed_val_nod_nm = self.table.item(row_index, 0).text()

#             if bln:
#                 checkbox = QCheckBox('Enabled')
#                 checkbox.setChecked(True)
#             else:
#                 checkbox = QCheckBox('Disabled')
#                 checkbox.setChecked(False)

#             checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))

#             checkbox_layout.addWidget(checkbox)
#             self.table.setCellWidget(row_index, col, checkbox_widget)

#     def update_node_value(self, nod_nm, c_row, c_col, c_val):
#         nuke_node = nuke.toNode(nod_nm)
        
#         if c_col == 0:
#             pass

#         elif c_col == 1:
#             pass

#         elif c_col == 2: # mix
#             if 'mix' in nuke_node.knobs():
#             # if nuke_node['mix']:
#                 nuke_node['mix'].setValue(float(c_val))

#         elif c_col == 3: # label
#             if 'label' in nuke_node.knobs():
#                 nuke_node['label'].setValue(c_val)

#         elif c_col == 9: # lift time
#             # print('c_val -- ', c_val)
#             # print("c_val[0] -- ", c_val[0])
#             # print("c_val[-1] -- ", c_val[-1])
#             # print(" type c_val[-1] -- ", type(c_val[-1]))
#             if 'lifetimeStart' in nuke_node.knobs():                
#                 life_start = int(c_val.split('.')[0])
#                 life_end = int(c_val.split('.')[-1])
#                 nuke_node['lifetimeStart'].setValue(life_start)
#                 nuke_node['lifetimeEnd'].setValue(life_end)     
                
#                 if life_start != 0 or life_end != 0:
#                     nuke_node['useLifetime'].setValue(True)
#                     lifetime_widget = self.table.item(c_row, c_col)
#                     lifetime_widget.setBackground(QColor(110, 106, 94))  
                    
#                 else:
#                     nuke_node['useLifetime'].setValue(False)
                             
#         else:
#             pass     

#     def on_cell_changed(self, row, column):
#         item = self.table.item(row, column)
#         if item:
#             changed_row = row
#             changed_column =  column
#             changed_value = item.text()
#             changed_val_nod_nm = self.table.item(row, 0).text()
#             self.update_node_value(changed_val_nod_nm, changed_row, changed_column, changed_value)

#     def lock_first_last(self):       
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#             lifetime_item = self.table.item(row, 9)
#             lifetime_item.setFlags(lifetime_item.flags() & ~Qt.ItemIsEditable)
            

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_ui_with_knobs()
#             self.lock_first_last()

#             self.set_nodes_count(nodes_len)
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)

#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         add_count = 0
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_ui_with_knobs(add_row)  
#                 add_count += 1
#         self.lock_first_last()   

#         nodes_len = add_count + int(self.label_nodes_count.text())
#         self.set_nodes_count(str(nodes_len))

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        
#     def btn_all_clicked(self):
#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_ui_with_knobs()      
#         self.btn_add.setEnabled(False)
#         self.lock_first_last()
#         self.btn_all.setEnabled(True)

#         self.set_nodes_count(nodes_len)

#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.table.setRowCount(0)
#         self.table.setColumnCount(10)
#         self.btn_add.setEnabled(False)
#         self.set_nodes_count('')
        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')
        
#     def btn_color_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             usr_sel_color = nuke.getColor() 

#             if usr_sel_color: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font'].setValue(font_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_text_pattern(self, bold=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if bold:
#                     nuke.toNode(node_nm)['note_font'].setValue('bold')
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_bold_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_bold.isChecked():
#                     self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
#                 else:
#                     self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_italic_pattern(self, italic=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if italic:
#                     nuke.toNode(node_nm)['note_font'].setValue('italic')
#                     print('pressed for italic')
#                 else:
#                     print('released for italic')
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_italic_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_italic.isChecked():
#                     self.update_italic_pattern(italic='italic', sel_item_nm=sel_item_nm)            
#                 else:
#                      self.update_italic_pattern(italic=None, sel_item_nm=sel_item_nm)            
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def get_life_frame_range(self):
#         frame_range = nuke.getInput('Please Enter frame-range \n example 1009.1050')
#         if not '.' in frame_range:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()

#         start_frame = frame_range.split('.')[0]
#         end_frame = frame_range.split('.')[-1]

#         if not start_frame <= end_frame:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()
#         else:
#             return True, start_frame, end_frame

#     def on_cellDoubleClicked(self, row, column):
#         if column == 9:
#             bln, start_frame, end_frame = self.get_life_frame_range()
#             if bln:
#                 item = QTableWidgetItem(f'{start_frame}.{end_frame}')
#                 self.table.setItem(row, column, item)
#                 item.setFlags(item.flags() & ~Qt.ItemIsEditable)

#                 changed_val_nod_nm = self.table.item(row, 0).text()
#                 self.update_node_value(changed_val_nod_nm, row, column, [start_frame, end_frame])
                

# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# import sys
# from PySide2.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QComboBox, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QCheckBox
# from PySide2.QtCore import Signal, QObject, Qt

# class ComboBoxSignalMapper(QObject):
#     value_changed = Signal(str, int, int)

#     def __init__(self, table_widget):
#         super().__init__()
#         self.table_widget = table_widget

#     def handle_value_change(self, combo_box):
#         row, col = self.get_cell_position(combo_box)
#         self.value_changed.emit(combo_box.currentText(), row, col)

#     def get_cell_position(self, combo_box):
#         for row in range(self.table_widget.rowCount()):
#             for col in range(self.table_widget.columnCount()):
#                 if self.table_widget.cellWidget(row, col) == combo_box:
#                     return row, col
#         return -1, -1

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QTableWidget with ComboBoxes and CheckBoxes")

#         # Create QTableWidget
#         self.table_widget = QTableWidget(5, 3)  # Multiple rows and columns
#         self.table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])

#         # Signal Mapper
#         self.signal_mapper = ComboBoxSignalMapper(self.table_widget)
#         self.signal_mapper.value_changed.connect(self.on_value_changed)

#         # Layout
#         main_layout = QVBoxLayout()

#         # Add ComboBoxes and CheckBoxes to multiple cells
#         for row in range(5):
#             for col in range(3):
#                 if (row + col) % 2 == 0:  # Add ComboBox to alternate cells
#                     combo_box = QComboBox()
#                     combo_box.addItems(["Option A", "Option B", "Option C"])
#                     combo_box.currentTextChanged.connect(lambda text, combo_box=combo_box: self.signal_mapper.handle_value_change(combo_box))
#                     self.table_widget.setCellWidget(row, col, combo_box)
#                 else:
#                     checkbox = QCheckBox(f"Check {row + 1}, {col + 1}")
#                     checkbox.setChecked(False)
#                     self.table_widget.setCellWidget(row, col, checkbox)

#         # Add button to toggle checkboxes
#         toggle_button = QPushButton("Toggle Selected Checkboxes")
#         toggle_button.clicked.connect(self.toggle_selected_checkboxes)

#         # Add widgets to layout
#         main_layout.addWidget(self.table_widget)
#         main_layout.addWidget(toggle_button)
#         self.setLayout(main_layout)

#     def on_value_changed(self, value, row, col):
#         print(f"Value changed to: {value} at Row: {row}, Column: {col}")

#     def toggle_selected_checkboxes(self):
#         selected_ranges = self.table_widget.selectedRanges()
#         for selected_range in selected_ranges:
#             for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
#                 for col in range(selected_range.leftColumn(), selected_range.rightColumn() + 1):
#                     cell_widget = self.table_widget.cellWidget(row, col)
#                     if isinstance(cell_widget, QCheckBox):
#                         cell_widget.setChecked(not cell_widget.isChecked())
#                         state = "Checked" if cell_widget.isChecked() else "Unchecked"
#                         print(f"{state}: Row {row}, Column {col}")

# if __name__ == "__main__":

#     window = MainWindow()
#     window.show()


# #######################################################################################


# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_clear.clicked.connect(self.btn_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)
#         self.btn_italic.clicked.connect(self.btn_italic_clicked)
#         self.table.cellChanged.connect(self.on_cell_changed)
#         self.table.cellDoubleClicked.connect(self.on_cellDoubleClicked)
#         self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         headerLabel = QLabel('NODE OPERATOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel(" -  Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         self.headerHlay.addSpacerItem(horizontalSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)
#         self.headerHlay.addSpacerItem(horizontalSpacer2)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))
        
#         self.btn_clear = QPushButton(' Clear All')
#         self.btn_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_nodes_added = QLabel('Nodes Added : ')    
#         self.label_nodes_count = QLabel('')

#         font_spacer = QSpacerItem(2000, 10, QSizePolicy.Maximum)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)
#         self.btn_italic.setCheckable(True)
#         self.btn_italic.setChecked(False)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_nodes_added)
#         self.fontHLay.addWidget(self.label_nodes_count)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'On/Off', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)  

#         self.table.horizontalHeader().setStretchLastSection(True) 
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

#         self.mainVlay.addWidget(self.table, stretch=1)

#         # print('=*='*10)
#         # for i in dir(self.table):
#         #     print(i)
#         # print('=*='*10)

#     def set_nodes_count(self, nodes_len):
#         self.label_nodes_count.setText(str(nodes_len))

#     def set_row_count_to_ui(self, nodes_len):
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()   


#                 if knob.name() == 'lifetimeEnd':
#                     self.nodes_data[node_name]['lifetimeEnd'] = node['lifetimeEnd'].value()
                  
#     def set_ui_with_knobs(self, add_row=None):
#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:           
#                 bln = self.nodes_data[node_nm]['disable']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 1)
#                 else:  
#                     self.set_chekckbox(False, row_index, 1)                    

#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 4)
#                 else:  
#                     self.set_chekckbox(False, row_index, 4)  

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['bookmark']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 7)
#                 else:  
#                     self.set_chekckbox(False, row_index, 7)                  

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 8)
#                 else:  
#                     self.set_chekckbox(False, row_index, 8)  

#             if 'lifetimeStart' in self.nodes_data[node_nm]:                
#                 life_start = int(self.nodes_data[node_nm]['lifetimeStart'])
#                 life_end = int(self.nodes_data[node_nm]['lifetimeEnd'])
#                 lifetime_widget = QTableWidgetItem(f'{life_start}.{life_end}')

#                 if life_start != 0 or life_end != 0:
#                     lifetime_widget.setBackground(QColor(110, 106, 94))
#                 self.table.setItem(row_index, 9, lifetime_widget)
  
#             self.table.setRowHeight(row_index, (row_index+2) * 16)

#     def update_checkbox_status(self,nod_nm, row, column, checkbox, state):
#         if state == Qt.Checked:
#             checkbox.setText('Enabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(True)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(True)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(True)                

#         else:
#             checkbox.setText('Disabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(False)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(False)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(False)                  

#     def set_chekckbox(self, bln, row_index, col):    
#             checkbox_widget = QWidget()
#             checkbox_layout = QHBoxLayout(checkbox_widget)
#             checkbox_layout.setContentsMargins(0,0,0,0)
#             checkbox_layout.setAlignment(Qt.AlignCenter)

#             changed_val_nod_nm = self.table.item(row_index, 0).text()

#             if bln:
#                 checkbox = QCheckBox('Enabled')
#                 checkbox.setChecked(True)
#             else:
#                 checkbox = QCheckBox('Disabled')
#                 checkbox.setChecked(False)

#             checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))

#             checkbox_layout.addWidget(checkbox)
#             self.table.setCellWidget(row_index, col, checkbox_widget)

#     def update_node_value(self, nod_nm, c_row, c_col, c_val):
#         nuke_node = nuke.toNode(nod_nm)
        
#         if c_col == 0:
#             pass

#         elif c_col == 1:
#             pass

#         elif c_col == 2: # mix
#             if 'mix' in nuke_node.knobs():
#                  nuke_node['mix'].setValue(float(c_val))

#         elif c_col == 3: # label
#             if 'label' in nuke_node.knobs():
#                 nuke_node['label'].setValue(c_val)

#         elif c_col == 9: # lift time

#             if 'lifetimeStart' in nuke_node.knobs():              
#                 life_start = int(c_val.split('.')[0])
#                 life_end = int(c_val.split('.')[-1])
#                 nuke_node['lifetimeStart'].setValue(life_start)
#                 nuke_node['lifetimeEnd'].setValue(life_end)     
                
#                 if life_start != 0 or life_end != 0:
#                     nuke_node['useLifetime'].setValue(True)
#                     lifetime_widget = self.table.item(c_row, c_col)
#                     lifetime_widget.setBackground(QColor(110, 106, 94))  
                    
#                 else:
#                     nuke_node['useLifetime'].setValue(False)

#         elif c_col == 5: #
#             if 'colorspace' in nuke_node.knobs():
#                 nuke_node['colorspace'].setValue(c_val)

#         elif c_col == 6:
#             if 'localizationPolicy' in nuke_node.knobs():
#                 nuke_node['localizationPolicy'].setValue(c_val)

#         else:
#             pass     

#     def on_cell_changed(self, row, column):
#         item = self.table.item(row, column)
#         if item:
#             changed_row = row
#             changed_column =  column
#             changed_value = item.text()
#             changed_val_nod_nm = self.table.item(row, 0).text()
#             self.update_node_value(changed_val_nod_nm, changed_row, changed_column, changed_value)

#     def lock_first_last(self):       
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#             lifetime_item = self.table.item(row, 9)
#             # lifetime_item.setFlags(lifetime_item.flags() & ~Qt.ItemIsEditable)

#     def colorspace_index_changed(self, combo_box):
#         # print('combo_box ============= ', dir(combo_box))
#         combo_cur_text = combo_box.currentText()
#         changed_row = None
#         changed_column = None

#         for row in range(self.table.rowCount()):
#             for column in range(self.table.columnCount()):
#                 if self.table.cellWidget(row, column) == combo_box:
#                     changed_row = row
#                     changed_column = column

#         changed_val_nod_nm = self.table.item(changed_row, 0).text()
#         self.update_node_value(changed_val_nod_nm, changed_row, changed_column, combo_cur_text)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)

#             # self.colorspace_combobox.currentIndexChanged.connect(lambda state, r=row_index, c=col: self.colorspace_index_changed(r, c, state))
#             self.colorspace_combobox.currentIndexChanged.connect(lambda text, combo_box=self.colorspace_combobox: self.colorspace_index_changed(combo_box))

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_ui_with_knobs()
#             self.lock_first_last()

#             self.set_nodes_count(nodes_len)
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)

#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         add_count = 0
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_ui_with_knobs(add_row)  
#                 add_count += 1
#         self.lock_first_last()   

#         nodes_len = add_count + int(self.label_nodes_count.text())
#         self.set_nodes_count(str(nodes_len))

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        
#     def btn_all_clicked(self):

#         self.btn_all.setEnabled(False)
#         self.btn_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_ui_with_knobs()      
#         self.btn_add.setEnabled(False)
#         self.lock_first_last()
#         self.btn_all.setEnabled(True)

#         self.set_nodes_count(nodes_len)

#     def btn_clear_clicked(self):
#         self.table.clearContents()
#         self.table.setRowCount(0)
#         self.table.setColumnCount(10)
#         self.btn_add.setEnabled(False)
#         self.set_nodes_count('')
        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')
        
#     def btn_color_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             usr_sel_color = nuke.getColor() 

#             if usr_sel_color: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font'].setValue(font_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_text_pattern(self, bold=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if bold:
#                     nuke.toNode(node_nm)['note_font'].setValue('bold')
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_bold_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_bold.isChecked():
#                     self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
#                 else:
#                     self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_italic_pattern(self, italic=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if italic:
#                     nuke.toNode(node_nm)['note_font'].setValue('italic')
#                     print('pressed for italic')
#                 else:
#                     print('released for italic')
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_italic_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_italic.isChecked():
#                     self.update_italic_pattern(italic='italic', sel_item_nm=sel_item_nm)            
#                 else:
#                      self.update_italic_pattern(italic=None, sel_item_nm=sel_item_nm)            
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def get_life_frame_range(self):
#         frame_range = nuke.getInput('Please Enter frame-range \n example 1009.1050')
#         if not '.' in frame_range:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()

#         start_frame = frame_range.split('.')[0]
#         end_frame = frame_range.split('.')[-1]

#         if not start_frame <= end_frame:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()
#         else:
#             return True, start_frame, end_frame

#     def on_cellDoubleClicked(self, row, column):
#         if column == 9:
#             bln, start_frame, end_frame = self.get_life_frame_range()
#             if bln:
#                 item = QTableWidgetItem(f'{start_frame}.{end_frame}')
#                 self.table.setItem(row, column, item)
#                 item.setFlags(item.flags() & ~Qt.ItemIsEditable)

#                 changed_val_nod_nm = self.table.item(row, 0).text()
#                 self.update_node_value(changed_val_nod_nm, row, column, [start_frame, end_frame])

#     def btn_refresh_clicked(self):
#         ui_nod_nm_lst = []
#         for row in range(self.table.rowCount()):
#             node_nm = self.table.item(row, 0).text()
#             ui_nod_nm_lst.append(node_nm)

#         if ui_nod_nm_lst:
#             self.btn_clear_clicked()

#             nodes_len = len(ui_nod_nm_lst)
#             self.set_row_count_to_ui(nodes_len)

#             nodes = []
#             for nod in ui_nod_nm_lst:
#                 nodes.append(nuke.toNode(nod))

#             self.get_nodes_info(nodes)
#             self.set_ui_with_knobs()
#             self.lock_first_last()

#             self.set_nodes_count(nodes_len)

#         else:
#             nuke.message('Node Operator panel is empty \n Please Load nodes!')
                

# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_selected_clear.clicked.connect(self.btn_selected_clear_clicked)
#         self.btn_all_clear.clicked.connect(self.btn_all_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)
#         self.btn_italic.clicked.connect(self.btn_italic_clicked)
#         self.table.cellChanged.connect(self.on_cell_changed)
#         self.table.cellDoubleClicked.connect(self.on_cellDoubleClicked)
#         self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         headerLabel = QLabel('NODE OPERATOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel(" -  Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         self.headerHlay.addSpacerItem(horizontalSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)
#         self.headerHlay.addSpacerItem(horizontalSpacer2)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))

#         self.btn_selected_clear = QPushButton(' Clear Selected')
#         self.btn_selected_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'selected_clear_icon1')))
#         self.btn_selected_clear.setIconSize(QSize(13, 13)) 

#         self.btn_all_clear = QPushButton(' Clear All')
#         self.btn_all_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_all_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_selected_clear)
#         self.hlay_1.addWidget(self.btn_all_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_nodes_added = QLabel('Nodes Added : ')    
#         self.label_nodes_count = QLabel('')

#         font_spacer = QSpacerItem(2000, 10, QSizePolicy.Maximum)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)
#         self.btn_italic.setCheckable(True)
#         self.btn_italic.setChecked(False)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_nodes_added)
#         self.fontHLay.addWidget(self.label_nodes_count)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'On/Off', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)  

#         self.table.horizontalHeader().setStretchLastSection(True) 
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

#         self.mainVlay.addWidget(self.table, stretch=1)

#         # print('=*='*10)
#         # for i in dir(self.table):
#         #     print(i)
#         # print('=*='*10)

#     def set_nodes_count(self, nodes_len):
#         self.label_nodes_count.setText(str(nodes_len))

#     def set_row_count_to_ui(self, nodes_len):
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()   


#                 if knob.name() == 'lifetimeEnd':
#                     self.nodes_data[node_name]['lifetimeEnd'] = node['lifetimeEnd'].value()
                  
#     def set_ui_with_knobs(self, add_row=None):
#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:           
#                 bln = self.nodes_data[node_nm]['disable']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 1)
#                 else:  
#                     self.set_chekckbox(False, row_index, 1)                    

#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 4)
#                 else:  
#                     self.set_chekckbox(False, row_index, 4)  

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['bookmark']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 7)
#                 else:  
#                     self.set_chekckbox(False, row_index, 7)                  

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 8)
#                 else:  
#                     self.set_chekckbox(False, row_index, 8)  

#             if 'lifetimeStart' in self.nodes_data[node_nm]:                
#                 life_start = int(self.nodes_data[node_nm]['lifetimeStart'])
#                 life_end = int(self.nodes_data[node_nm]['lifetimeEnd'])
#                 lifetime_widget = QTableWidgetItem(f'{life_start}.{life_end}')

#                 if life_start != 0 or life_end != 0:
#                     lifetime_widget.setBackground(QColor(110, 106, 94))
#                 self.table.setItem(row_index, 9, lifetime_widget)
  
#             self.table.setRowHeight(row_index, (row_index+2) * 16)

#     def update_checkbox_status(self,nod_nm, row, column, checkbox, state):
#         if state == Qt.Checked:
#             checkbox.setText('Enabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(True)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(True)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(True)                

#         else:
#             checkbox.setText('Disabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(False)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(False)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(False)                  

#     def set_chekckbox(self, bln, row_index, col):    
#             checkbox_widget = QWidget()
#             checkbox_layout = QHBoxLayout(checkbox_widget)
#             checkbox_layout.setContentsMargins(0,0,0,0)
#             checkbox_layout.setAlignment(Qt.AlignCenter)

#             changed_val_nod_nm = self.table.item(row_index, 0).text()

#             if bln:
#                 checkbox = QCheckBox('Enabled')
#                 checkbox.setChecked(True)
#             else:
#                 checkbox = QCheckBox('Disabled')
#                 checkbox.setChecked(False)

#             checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))

#             checkbox_layout.addWidget(checkbox)
#             self.table.setCellWidget(row_index, col, checkbox_widget)

#     def update_node_value(self, nod_nm, c_row, c_col, c_val):
#         nuke_node = nuke.toNode(nod_nm)
        
#         if c_col == 0:
#             pass

#         elif c_col == 1:
#             pass

#         elif c_col == 2: # mix
#             if 'mix' in nuke_node.knobs():
#                  nuke_node['mix'].setValue(float(c_val))

#         elif c_col == 3: # label
#             if 'label' in nuke_node.knobs():
#                 nuke_node['label'].setValue(c_val)

#         elif c_col == 9: # lift time

#             if 'lifetimeStart' in nuke_node.knobs():              
#                 life_start = int(c_val.split('.')[0])
#                 life_end = int(c_val.split('.')[-1])
#                 nuke_node['lifetimeStart'].setValue(life_start)
#                 nuke_node['lifetimeEnd'].setValue(life_end)     
                
#                 if life_start != 0 or life_end != 0:
#                     nuke_node['useLifetime'].setValue(True)
#                     lifetime_widget = self.table.item(c_row, c_col)
#                     lifetime_widget.setBackground(QColor(110, 106, 94))  
                    
#                 else:
#                     nuke_node['useLifetime'].setValue(False)

#         elif c_col == 5: #
#             if 'colorspace' in nuke_node.knobs():
#                 nuke_node['colorspace'].setValue(c_val)

#         elif c_col == 6:
#             if 'localizationPolicy' in nuke_node.knobs():
#                 nuke_node['localizationPolicy'].setValue(c_val)

#         else:
#             pass     

#     def on_cell_changed(self, row, column):
#         item = self.table.item(row, column)
#         if item:
#             changed_row = row
#             changed_column =  column
#             changed_value = item.text()
#             changed_val_nod_nm = self.table.item(row, 0).text()
#             self.update_node_value(changed_val_nod_nm, changed_row, changed_column, changed_value)

#     def lock_first_last(self):       
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#             lifetime_item = self.table.item(row, 9)
#             # lifetime_item.setFlags(lifetime_item.flags() & ~Qt.ItemIsEditable)

#     def colorspace_index_changed(self, combo_box):
#         # print('combo_box ============= ', dir(combo_box))
#         combo_cur_text = combo_box.currentText()
#         changed_row = None
#         changed_column = None

#         for row in range(self.table.rowCount()):
#             for column in range(self.table.columnCount()):
#                 if self.table.cellWidget(row, column) == combo_box:
#                     changed_row = row
#                     changed_column = column

#         changed_val_nod_nm = self.table.item(changed_row, 0).text()
#         self.update_node_value(changed_val_nod_nm, changed_row, changed_column, combo_cur_text)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)

#             # self.colorspace_combobox.currentIndexChanged.connect(lambda state, r=row_index, c=col: self.colorspace_index_changed(r, c, state))
#             self.colorspace_combobox.currentIndexChanged.connect(lambda text, combo_box=self.colorspace_combobox: self.colorspace_index_changed(combo_box))

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_all_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_ui_with_knobs()
#             self.lock_first_last()

#             self.set_nodes_count(nodes_len)
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)

#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         add_count = 0
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_ui_with_knobs(add_row)  
#                 add_count += 1
#         self.lock_first_last()   

#         nodes_len = add_count + int(self.label_nodes_count.text())
#         self.set_nodes_count(str(nodes_len))

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        
#     def btn_all_clicked(self):

#         self.btn_all.setEnabled(False)
#         self.btn_all_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_ui_with_knobs()      
#         self.btn_add.setEnabled(False)
#         self.lock_first_last()
#         self.btn_all.setEnabled(True)

#         self.set_nodes_count(nodes_len)

#     def btn_all_clear_clicked(self):
#         self.table.clearContents()
#         self.table.setRowCount(0)
#         self.table.setColumnCount(10)
#         self.btn_add.setEnabled(False)
#         self.set_nodes_count('')
        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')
        
#     def btn_color_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             usr_sel_color = nuke.getColor() 

#             if usr_sel_color: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font'].setValue(font_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_text_pattern(self, bold=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if bold:
#                     nuke.toNode(node_nm)['note_font'].setValue('bold')
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_bold_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_bold.isChecked():
#                     self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
#                 else:
#                     self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_italic_pattern(self, italic=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if italic:
#                     nuke.toNode(node_nm)['note_font'].setValue('italic')
#                     print('pressed for italic')
#                 else:
#                     print('released for italic')
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_italic_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_italic.isChecked():
#                     self.update_italic_pattern(italic='italic', sel_item_nm=sel_item_nm)            
#                 else:
#                      self.update_italic_pattern(italic=None, sel_item_nm=sel_item_nm)            
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def get_life_frame_range(self):
#         frame_range = nuke.getInput('Please Enter frame-range \n example 1009.1050')
#         if not '.' in frame_range:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()

#         start_frame = frame_range.split('.')[0]
#         end_frame = frame_range.split('.')[-1]

#         if not start_frame <= end_frame:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()
#         else:
#             return True, start_frame, end_frame

#     def on_cellDoubleClicked(self, row, column):
#         if column == 9:
#             bln, start_frame, end_frame = self.get_life_frame_range()
#             if bln:
#                 item = QTableWidgetItem(f'{start_frame}.{end_frame}')
#                 self.table.setItem(row, column, item)
#                 item.setFlags(item.flags() & ~Qt.ItemIsEditable)

#                 changed_val_nod_nm = self.table.item(row, 0).text()
#                 self.update_node_value(changed_val_nod_nm, row, column, [start_frame, end_frame])

#     def btn_refresh_clicked(self):
#         ui_nod_nm_lst = []
#         for row in range(self.table.rowCount()):
#             node_nm = self.table.item(row, 0).text()
#             ui_nod_nm_lst.append(node_nm)

#         if ui_nod_nm_lst:
#             self.btn_all_clear_clicked()

#             nodes_len = len(ui_nod_nm_lst)
#             self.set_row_count_to_ui(nodes_len)

#             nodes = []
#             for nod in ui_nod_nm_lst:
#                 nodes.append(nuke.toNode(nod))

#             self.get_nodes_info(nodes)
#             self.set_ui_with_knobs()
#             self.lock_first_last()

#             self.set_nodes_count(nodes_len)

#         else:
#             nuke.message('Node Operator panel is empty \n Please Load nodes!')
                
#     def btn_selected_clear_clicked(self):
#         selected_items = self.table.selectedItems()

#         remove_nod_nm_lst = []
#         for item in selected_items:
#             row = item.row()
#             column = item.column()

#             if column == 0:
#                 remove_nod_nm_lst.append(item.text())

#         if remove_nod_nm_lst:
#             ui_nod_nm_lst = []
#             for row in range(self.table.rowCount()):
#                 node_nm = self.table.item(row, 0).text()
#                 ui_nod_nm_lst.append(node_nm)  

#             nod_nm_lst_for_add = [ele for ele in ui_nod_nm_lst]
#             for a in remove_nod_nm_lst:
#                 if a in ui_nod_nm_lst:
#                     nod_nm_lst_for_add.remove(a)

#             if nod_nm_lst_for_add:
#                 self.btn_all_clear_clicked()   

#                 nodes_len = len(nod_nm_lst_for_add)
#                 self.set_row_count_to_ui(nodes_len)

#                 nodes = []
#                 for nod in nod_nm_lst_for_add:
#                     nodes.append(nuke.toNode(nod))    

#                 self.get_nodes_info(nodes)
#                 self.set_ui_with_knobs()
#                 self.lock_first_last()

#                 self.set_nodes_count(nodes_len)

#             else:
#                 self.btn_all_clear_clicked()


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################




# from PySide2.QtWidgets import QWidget, QApplication, QTableWidget, QHeaderView,QFrame, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
# from PySide2.QtGui import QPixmap, QColor, QFont
# from PySide2.QtCore import QSize, Qt
# import sys, os
# import nuke
# import re
# from pprint import pprint
# window = None

# dir_path = os.path.dirname(__file__)
# icons_dir_path = os.path.join(dir_path, 'icons')


# class NodeOperator(QWidget):
#     def __init__(self, parent=None):
#         super(NodeOperator, self).__init__(parent)
#         self.mainVlay = QVBoxLayout()  
#         self.setLayout(self.mainVlay)

#         self.sel_nodes = None
#         self.nodes_data = {}
#         self.headers = None

#         self.set_ui_header()
#         self.set_top_btn_widgets()
#         # self.configure_multi_ops()
#         self.add_font_widget()
#         self.add_table()
        

#         self.init()

#     # Signal & Slot
#     def init(self):
#         self.btn_load.clicked.connect(self.btn_load_clicked)
#         self.btn_add.clicked.connect(self.btn_add_clicked)
#         self.btn_all.clicked.connect(self.btn_all_clicked)
#         self.btn_selected_clear.clicked.connect(self.btn_selected_clear_clicked)
#         self.btn_all_clear.clicked.connect(self.btn_all_clear_clicked)
#         self.search_line_edit.textEdited.connect(self.edited_search_line)
#         self.font_size.textEdited.connect(self.changed_font_size)
#         self.font_combo.currentTextChanged.connect(self.font_changed)        
#         self.btn_color.clicked.connect(self.btn_color_clicked)
#         self.btn_bold.clicked.connect(self.btn_bold_clicked)
#         self.btn_italic.clicked.connect(self.btn_italic_clicked)
#         self.table.cellChanged.connect(self.on_cell_changed)
#         self.table.cellDoubleClicked.connect(self.on_cellDoubleClicked)
#         self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        

#     def set_ui_header(self):
#         self.headerHlay = QHBoxLayout()

#         horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         headerLabel = QLabel('NODE OPERATOR')
#         header_font = QFont()
#         header_font.setBold(True)
#         header_font.setPointSize(14)
#         headerLabel.setFont(header_font)
#         headerLabel.setStyleSheet("color: #555555;")
        
#         description_label = QLabel(" -  Streamline node management")
#         description_font = QFont()
#         description_font.setItalic(True)
#         description_font.setPointSize(10) 
#         description_label.setFont(description_font)
#         description_label.setStyleSheet("color: #696969;")

#         horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         self.headerHlay.addSpacerItem(horizontalSpacer1)
#         self.headerHlay.addWidget(headerLabel)
#         self.headerHlay.addWidget(description_label)
#         self.headerHlay.addSpacerItem(horizontalSpacer2)

#         self.mainVlay.addLayout(self.headerHlay)
        
#     def set_top_btn_widgets(self):

#         self.hlay_1 = QHBoxLayout()
#         self.search_line_edit = QLineEdit()
#         self.search_line_edit.setMinimumWidth(75)
#         self.search_line_edit.setPlaceholderText('Find Node')

#         self.btn_export = QPushButton('Export')
#         self.btn_import = QPushButton('Import')

#         self.btn_load = QPushButton(' Load Selected')
#         self.btn_load.setIcon(QPixmap(os.path.join(icons_dir_path, 'load_icon.png')))
#         self.btn_load.setIconSize(QSize(13, 13))

#         self.btn_add = QPushButton(' Add')
#         self.btn_add.setIcon(QPixmap(os.path.join(icons_dir_path, 'add_icon')))
#         self.btn_add.setIconSize(QSize(13, 13))
#         self.btn_add.setEnabled(False)

#         self.btn_all = QPushButton(' Load All')
#         self.btn_all.setIcon(QPixmap(os.path.join(icons_dir_path, 'all_icon')))
#         self.btn_all.setIconSize(QSize(13, 13))
#         rgba_style = f"rgba({101}, {175}, {225}, {64 / 255:.3f})"
#         self.btn_all.setStyleSheet(f"background-color: {rgba_style}; color: white;")

#         self.btn_refresh = QPushButton(' Refresh')
#         self.btn_refresh.setIcon(QPixmap(os.path.join(icons_dir_path, 'refresh_icon1')))
#         self.btn_refresh.setIconSize(QSize(13, 13))

#         self.btn_selected_clear = QPushButton(' Clear Selected')
#         self.btn_selected_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'selected_clear_icon1')))
#         self.btn_selected_clear.setIconSize(QSize(13, 13)) 

#         self.btn_all_clear = QPushButton(' Clear All')
#         self.btn_all_clear.setIcon(QPixmap(os.path.join(icons_dir_path, 'clear_icon')))
#         self.btn_all_clear.setIconSize(QSize(13, 13))    

#         self.hlay_1.addWidget(self.search_line_edit)
#         self.hlay_1.addWidget(self.btn_export)
#         self.hlay_1.addWidget(self.btn_import)
#         self.hlay_1.addWidget(self.btn_load)
#         self.hlay_1.addWidget(self.btn_add)
#         self.hlay_1.addWidget(self.btn_all)
#         self.hlay_1.addWidget(self.btn_refresh)
#         self.hlay_1.addWidget(self.btn_selected_clear)
#         self.hlay_1.addWidget(self.btn_all_clear)
       
#         self.mainVlay.addLayout(self.hlay_1)

#     # def configure_multi_ops(self):
#     #     self.multi_operation_HLay = QHBoxLayout()

#     #     self.btn_export = QPushButton('Export')
#     #     self.btn_import = QPushButton('Import')

#     #     multi_operation_spacer1 = QSpacerItem(2000, 10, QSizePolicy.Maximum)

#     #     self.ck_sel_on_off = QCheckBox('On/Off')
#     #     self.ck_sel_on_off.setChecked(False)
#     #     self.ck_sel_on_off.stateChanged.connect(self.on_off_state_changed)

#     #     self.ck_sel_thumbnail = QCheckBox('Thumbnail')
#     #     self.ck_sel_thumbnail.setChecked(False)

#     #     self.ck_sel_favorite = QCheckBox('Favorite')
#     #     self.ck_sel_favorite.setChecked(False)

#     #     self.ck_sel_hide_input = QCheckBox('Hide Input')
#     #     self.ck_sel_hide_input.setChecked(False)

#     #     multi_operation_spacer2 = QSpacerItem(2000, 10, QSizePolicy.Maximum)

#     #     self.cb_sel_colorspace = QComboBox()
#     #     self.cb_sel_localized = QComboBox()

#     #     self.multi_operation_HLay.addWidget(self.btn_export)
#     #     self.multi_operation_HLay.addWidget(self.btn_import)
#     #     self.multi_operation_HLay.addSpacerItem(multi_operation_spacer1)
#     #     self.multi_operation_HLay.addWidget(self.ck_sel_on_off)
#     #     self.multi_operation_HLay.addWidget(self.ck_sel_thumbnail)
#     #     self.multi_operation_HLay.addWidget(self.ck_sel_favorite)
#     #     self.multi_operation_HLay.addWidget(self.ck_sel_hide_input)
#     #     self.multi_operation_HLay.addSpacerItem(multi_operation_spacer2)
#     #     self.multi_operation_HLay.addWidget(self.cb_sel_colorspace)
#     #     self.multi_operation_HLay.addWidget(self.cb_sel_localized)
        
#     #     self.mainVlay.addLayout(self.multi_operation_HLay)

#     def add_font_widget(self):
#         self.fontHLay = QHBoxLayout()
#         self.label_nodes_added = QLabel('Nodes Added : ')    
#         self.label_nodes_count = QLabel('')

#         font_spacer = QSpacerItem(2000, 10, QSizePolicy.Maximum)
#         self.font_combo = QComboBox()        
#         fonts_data = nuke.getFonts()
#         all_fonts = []
#         for font_nm in fonts_data:
#            all_fonts.append(font_nm[0])
#         self.font_combo.addItems(all_fonts)
#         self.font_combo.setCurrentText('Verdana')


#         self.btn_bold = QPushButton('Bold')
#         self.btn_bold.setIcon(QPixmap(os.path.join(icons_dir_path, 'bold_icon1.png')))
#         self.btn_bold.setIconSize(QSize(12, 12))
#         self.btn_bold.setMaximumWidth(50)
#         self.btn_bold.setCheckable(True)
#         self.btn_bold.setChecked(False)
        

#         self.btn_italic = QPushButton('Italic')
#         self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
#         self.btn_italic.setIconSize(QSize(12, 12))
#         self.btn_italic.setMaximumWidth(75)
#         self.btn_italic.setCheckable(True)
#         self.btn_italic.setChecked(False)

#         self.font_size = QLineEdit('11')
#         self.font_size.setMaximumWidth(30)

#         self.btn_color = QPushButton('Color')
#         self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
#         self.btn_color.setMaximumWidth(75)

#         self.separator = QFrame()
#         self.separator.setFrameShape(QFrame.VLine)
#         self.separator.setFrameShadow(QFrame.Sunken)

#         self.fontHLay.addWidget(self.label_nodes_added)
#         self.fontHLay.addWidget(self.label_nodes_count)
#         self.fontHLay.addSpacerItem(font_spacer)
#         self.fontHLay.addWidget(self.font_combo)
#         self.fontHLay.addWidget(self.btn_bold)
#         self.fontHLay.addWidget(self.btn_italic)
#         self.fontHLay.addWidget(self.font_size)
#         self.fontHLay.addWidget(self.separator)
#         self.fontHLay.addWidget(self.btn_color)

#         self.mainVlay.addLayout(self.fontHLay)
        
#     def add_table(self):

#         self.table = QTableWidget()
#         self.table.setColumnCount(10)
#         self.headers = ['Node Name', 'On/Off', 'Mix', 'Label', 'Thumbnail', 'ColorSpace', 'Localized', 'Favorite', 'Hide Input', 'Lifetime']
#         self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # set table header with column count
#         self.table.setColumnCount(len(self.headers))
#         self.table.setHorizontalHeaderLabels(self.headers)  

#         self.table.horizontalHeader().setStretchLastSection(True) 
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  


#         self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

#         self.mainVlay.addWidget(self.table, stretch=1)

#         # print('=*='*10)
#         # for i in dir(self.table):
#         #     print(i)
#         # print('=*='*10)

#     def set_nodes_count(self, nodes_len):
#         self.label_nodes_count.setText(str(nodes_len))

#     def set_row_count_to_ui(self, nodes_len):
#         self.table.setRowCount(nodes_len)
#         print('row updated')

#     def get_selected_node(self):
#         check_nodes_ = nuke.selectedNodes()
#         if len(check_nodes_) > 0:
#             self.sel_nodes = nuke.selectedNodes()

#     def get_nodes_info(self, nodes):     

#         self.nodes_data = {}   

#         for index, node in enumerate(nodes):

#             node_name = node.name()
#             if node_name not in self.nodes_data:
#                 self.nodes_data[node_name] = {}

#             for knob in node.allKnobs():

#                 self.nodes_data[node_name]['node_name'] = node_name
            
#                 if knob.name() == 'disable':
#                     self.nodes_data[node_name]['disable'] = node['disable'].value()
#                 if knob.name() == 'mix':
#                     self.nodes_data[node_name]['mix'] = node['mix'].value()

#                 if knob.name() == 'label':
#                     self.nodes_data[node_name]['label'] = node['label'].value()

#                 if knob.name() == 'postage_stamp':
#                     self.nodes_data[node_name]['postage_stamp'] = node['postage_stamp'].value()

#                 if knob.name() == 'colorspace':
#                     self.nodes_data[node_name]['colorspace'] = node['colorspace'].value()
#                     self.colorspace_conbo = QComboBox()

#                 if knob.name() == 'localizationPolicy':
#                     self.nodes_data[node_name]['localizationPolicy'] = node['localizationPolicy'].value()

#                 if knob.name() == 'bookmark':
#                     self.nodes_data[node_name]['bookmark'] = node['bookmark'].value()

#                 if knob.name() == 'hide_input':
#                     self.nodes_data[node_name]['hide_input'] = node['hide_input'].value()

#                 if knob.name() == 'lifetimeStart':
#                     self.nodes_data[node_name]['lifetimeStart'] = node['lifetimeStart'].value()   


#                 if knob.name() == 'lifetimeEnd':
#                     self.nodes_data[node_name]['lifetimeEnd'] = node['lifetimeEnd'].value()
                  
#     def set_ui_with_knobs(self, add_row=None):
#         """
#         {'Read2': {'bookmark': False,
#                    'colorspace': 'default',
#                    'disable': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'localizationPolicy': 'fromAutoLocalizePath',
#                    'node_name': 'Read2',
#                    'postage_stamp': True},
#          'Roto1': {'bookmark': False,
#                    'disable': False,
#                    'hide_input': False,
#                    'label': '',
#                    'lifetimeStart': 0.0,
#                    'node_name': 'Roto1',
#                    'postage_stamp': False}
#         """


#         all_node_names = self.nodes_data.keys()

#         sorted_all_node_names = sorted(all_node_names)
#         for row_index, node_nm in enumerate(sorted_all_node_names):

#             if add_row:
#                row_index = add_row

#             node_nm_widget = QTableWidgetItem(node_nm)
#             self.table.setItem(row_index, 0, node_nm_widget)

#             if 'disable' in self.nodes_data[node_nm]:           
#                 bln = self.nodes_data[node_nm]['disable']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 1)
#                 else:  
#                     self.set_chekckbox(False, row_index, 1)                    

#             if 'mix' in self.nodes_data[node_nm]:
#                 mix_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['mix']))
#                 self.table.setItem(row_index, 2, mix_widget)


#             if 'label' in self.nodes_data[node_nm]:
#                 label_widget = QTableWidgetItem(str(self.nodes_data[node_nm]['label']))
#                 self.table.setItem(row_index, 3, label_widget)

#             if 'postage_stamp' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['postage_stamp']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 4)
#                 else:  
#                     self.set_chekckbox(False, row_index, 4)  

#             if 'colorspace' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'colorspace', row_index, 5)

#             if 'localizationPolicy' in self.nodes_data[node_nm]:
#                 self.set_combo_companies(node_nm, 'localizationPolicy', row_index, 6)

#             if 'bookmark' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['bookmark']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 7)
#                 else:  
#                     self.set_chekckbox(False, row_index, 7)                  

#             if 'hide_input' in self.nodes_data[node_nm]:
#                 bln = self.nodes_data[node_nm]['hide_input']
#                 if bln:
#                     self.set_chekckbox(True, row_index, 8)
#                 else:  
#                     self.set_chekckbox(False, row_index, 8)  

#             if 'lifetimeStart' in self.nodes_data[node_nm]:                
#                 life_start = int(self.nodes_data[node_nm]['lifetimeStart'])
#                 life_end = int(self.nodes_data[node_nm]['lifetimeEnd'])
#                 lifetime_widget = QTableWidgetItem(f'{life_start}.{life_end}')

#                 if life_start != 0 or life_end != 0:
#                     lifetime_widget.setBackground(QColor(110, 106, 94))
#                 self.table.setItem(row_index, 9, lifetime_widget)
  
#             self.table.setRowHeight(row_index, (row_index+2) * 16)

#     def update_checkbox_status(self,nod_nm, row, column, checkbox, state, nodes_nm):
#         if state == Qt.Checked:
#             checkbox.setText('Enabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(True)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(True)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(True)                

#         else:
#             checkbox.setText('Disabled')
#             if column == 1:
#                 nuke.toNode(nod_nm)['disable'].setValue(False)
#             if column == 4:
#                 nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
#             if column == 7:
#                 nuke.toNode(nod_nm)['bookmark'].setValue(False)
#             if column == 8:
#                 nuke.toNode(nod_nm)['hide_input'].setValue(False)                  

#     def get_sel_ui_nods_nm(self):
#         selected_items = self.table.selectedItems()

#         nod_nm_lst = []
#         for item in selected_items:
#             row = item.row()
#             column = item.column()

#             if column == 0:
#                 nod_nm_lst.append(item.text())

#         return nod_nm_lst

#     def set_chekckbox(self, bln, row_index, col):    
#             checkbox_widget = QWidget()
#             checkbox_layout = QHBoxLayout(checkbox_widget)
#             checkbox_layout.setContentsMargins(0,0,0,0)
#             checkbox_layout.setAlignment(Qt.AlignCenter)

#             changed_val_nod_nm = self.table.item(row_index, 0).text()

#             if bln:
#                 checkbox = QCheckBox('Enabled')
#                 checkbox.setChecked(True)
#             else:
#                 checkbox = QCheckBox('Disabled')
#                 checkbox.setChecked(False)

#             nodes_nm = self.get_sel_ui_nods_nm()

#             checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state, nodes_nm))

#             checkbox_layout.addWidget(checkbox)
#             self.table.setCellWidget(row_index, col, checkbox_widget)

#     def update_node_value(self, nod_nm, c_row, c_col, c_val):
#         nuke_node = nuke.toNode(nod_nm)
        
#         if c_col == 0:
#             pass

#         elif c_col == 1:
#             pass

#         elif c_col == 2: # mix
#             if 'mix' in nuke_node.knobs():
#                  nuke_node['mix'].setValue(float(c_val))

#         elif c_col == 3: # label
#             if 'label' in nuke_node.knobs():
#                 nuke_node['label'].setValue(c_val)

#         elif c_col == 9: # lift time

#             if 'lifetimeStart' in nuke_node.knobs():              
#                 life_start = int(c_val.split('.')[0])
#                 life_end = int(c_val.split('.')[-1])
#                 nuke_node['lifetimeStart'].setValue(life_start)
#                 nuke_node['lifetimeEnd'].setValue(life_end)     
                
#                 if life_start != 0 or life_end != 0:
#                     nuke_node['useLifetime'].setValue(True)
#                     lifetime_widget = self.table.item(c_row, c_col)
#                     lifetime_widget.setBackground(QColor(110, 106, 94))  
                    
#                 else:
#                     nuke_node['useLifetime'].setValue(False)

#         elif c_col == 5: #
#             if 'colorspace' in nuke_node.knobs():
#                 nuke_node['colorspace'].setValue(c_val)

#         elif c_col == 6:
#             if 'localizationPolicy' in nuke_node.knobs():
#                 nuke_node['localizationPolicy'].setValue(c_val)

#         else:
#             pass     

#     def on_cell_changed(self, row, column):
#         item = self.table.item(row, column)
#         if item:
#             changed_row = row
#             changed_column =  column
#             changed_value = item.text()
#             changed_val_nod_nm = self.table.item(row, 0).text()
#             self.update_node_value(changed_val_nod_nm, changed_row, changed_column, changed_value)

#     def lock_first_last(self):       
#         for row in range(self.table.rowCount()):
#             read_item = self.table.item(row, 0)
#             read_item.setFlags(read_item.flags() & ~Qt.ItemIsEditable)

#             lifetime_item = self.table.item(row, 9)
#             # lifetime_item.setFlags(lifetime_item.flags() & ~Qt.ItemIsEditable)

#     def colorspace_index_changed(self, combo_box):
#         # print('combo_box ============= ', dir(combo_box))
#         combo_cur_text = combo_box.currentText()
#         changed_row = None
#         changed_column = None

#         for row in range(self.table.rowCount()):
#             for column in range(self.table.columnCount()):
#                 if self.table.cellWidget(row, column) == combo_box:
#                     changed_row = row
#                     changed_column = column

#         changed_val_nod_nm = self.table.item(changed_row, 0).text()
#         self.update_node_value(changed_val_nod_nm, changed_row, changed_column, combo_cur_text)

#     def set_combo_companies(self, node_nm, knob_nm, row_index, col):
#             self.colorspace_combobox = QComboBox()                
#             values = nuke.toNode(node_nm)[knob_nm].values()
#             self.colorspace_combobox.addItems(values)
#             self.table.setCellWidget(row_index, col, self.colorspace_combobox)
            
#             value = nuke.toNode(node_nm)[knob_nm].value()
#             index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
#             self.colorspace_combobox.setCurrentIndex(index)

#             # self.colorspace_combobox.currentIndexChanged.connect(lambda state, r=row_index, c=col: self.colorspace_index_changed(r, c, state))
#             self.colorspace_combobox.currentIndexChanged.connect(lambda text, combo_box=self.colorspace_combobox: self.colorspace_index_changed(combo_box))

#     def btn_load_clicked(self):

#         self.sel_nodes = None
#         self.get_selected_node()

#         if self.sel_nodes:
#             self.btn_all_clear_clicked()

#             nodes_len = len(nuke.selectedNodes())
#             self.set_row_count_to_ui(nodes_len)

#             nodes = nuke.selectedNodes()
#             self.get_nodes_info(nodes)
#             self.set_ui_with_knobs()
#             self.lock_first_last()

#             self.set_nodes_count(nodes_len)
#         else:
#             nuke.message('Please Select Nodes')
#         self.btn_add.setEnabled(True)

#     def btn_add_clicked(self):        
#         nodes = nuke.selectedNodes()
#         add_count = 0
#         for index, node in enumerate(nodes):
#             bln = self.check_node_in_table(node)
#             if bln:
#                 add_row = self.add_new_node(index, node)    
#                 self.get_nodes_info([node])
#                 self.set_ui_with_knobs(add_row)  
#                 add_count += 1
#         self.lock_first_last()   

#         nodes_len = add_count + int(self.label_nodes_count.text())
#         self.set_nodes_count(str(nodes_len))

#     def check_node_in_table(self, node):
#         all_node_names = []
#         for row in range(self.table.rowCount()):
#             fst_column_data = self.table.item(row, 0)
#             all_node_names.append(fst_column_data.text())

#         if node.name() in all_node_names:
#             return False
#         else:
#             return True

#     def add_new_node(self, index, node):
#         current_row_count = self.table.rowCount()
#         self.table.insertRow(current_row_count)
#         return current_row_count
        
#     def btn_all_clicked(self):

#         self.btn_all.setEnabled(False)
#         self.btn_all_clear_clicked()

#         nodes_len = len(nuke.allNodes())
#         self.set_row_count_to_ui(nodes_len)

#         nodes = nuke.allNodes()
#         self.get_nodes_info(nodes)
#         self.set_ui_with_knobs()      
#         self.btn_add.setEnabled(False)
#         self.lock_first_last()
#         self.btn_all.setEnabled(True)

#         self.set_nodes_count(nodes_len)

#     def btn_all_clear_clicked(self):
#         self.table.clearContents()
#         self.table.setRowCount(0)
#         self.table.setColumnCount(10)
#         self.btn_add.setEnabled(False)
#         self.set_nodes_count('')
        
#     def edited_search_line(self, text):
#         self.table.setCurrentItem(None)
#         if not text:
#             return
#         matching_items = self.table.findItems(text, Qt.MatchContains) 
#         if matching_items:
#             for item in matching_items:
#                 item.setSelected(True)

#     def changed_font_size(self, size):
#         if not size:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font_size'].setValue(int(size))
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')
        
#     def btn_color_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             usr_sel_color = nuke.getColor() 

#             if usr_sel_color: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['tile_color'].setValue(usr_sel_color) 

#     def font_changed(self, font_nm):
#         if not font_nm:
#             return

#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())
    
#             if sel_item_nm: 
#                 for node_nm in sel_item_nm:
#                     if nuke.toNode(node_nm):
#                         nuke.toNode(node_nm)['note_font'].setValue(font_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_text_pattern(self, bold=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if bold:
#                     nuke.toNode(node_nm)['note_font'].setValue('bold')
#                 else:
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_bold_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_bold.isChecked():
#                     self.update_text_pattern(bold='bold', sel_item_nm=sel_item_nm)
#                 else:
#                     self.update_text_pattern(bold=None, sel_item_nm=sel_item_nm)
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def update_italic_pattern(self, italic=None, sel_item_nm=None):

#         for node_nm in sel_item_nm:
#             if nuke.toNode(node_nm):     
#                 if italic:
#                     nuke.toNode(node_nm)['note_font'].setValue('italic')
#                     print('pressed for italic')
#                 else:
#                     print('released for italic')
#                     nuke.toNode(node_nm)['note_font'].setValue("")

#     def btn_italic_clicked(self):
#         sel_items = self.table.selectedItems()
#         sel_item_nm = []

#         if sel_items:
#             for item in sel_items:
#                 sel_item_nm.append(item.text())

#             if sel_item_nm: 
#                 if self.btn_italic.isChecked():
#                     self.update_italic_pattern(italic='italic', sel_item_nm=sel_item_nm)            
#                 else:
#                      self.update_italic_pattern(italic=None, sel_item_nm=sel_item_nm)            
#             else:
#                 nuke.message('Please select Node Names in Node Operator UI')

#     def get_life_frame_range(self):
#         frame_range = nuke.getInput('Please Enter frame-range \n example 1009.1050')
#         if not '.' in frame_range:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()

#         start_frame = frame_range.split('.')[0]
#         end_frame = frame_range.split('.')[-1]

#         if not start_frame <= end_frame:
#             nuke.message('Invalid frame-range \n Please try again')
#             self.get_frame_range()
#         else:
#             return True, start_frame, end_frame

#     def on_cellDoubleClicked(self, row, column):
#         if column == 9:
#             bln, start_frame, end_frame = self.get_life_frame_range()
#             if bln:
#                 item = QTableWidgetItem(f'{start_frame}.{end_frame}')
#                 self.table.setItem(row, column, item)
#                 item.setFlags(item.flags() & ~Qt.ItemIsEditable)

#                 changed_val_nod_nm = self.table.item(row, 0).text()
#                 self.update_node_value(changed_val_nod_nm, row, column, [start_frame, end_frame])

#     def btn_refresh_clicked(self):
#         ui_nod_nm_lst = []
#         for row in range(self.table.rowCount()):
#             node_nm = self.table.item(row, 0).text()
#             ui_nod_nm_lst.append(node_nm)

#         if ui_nod_nm_lst:
#             self.btn_all_clear_clicked()

#             nodes_len = len(ui_nod_nm_lst)
#             self.set_row_count_to_ui(nodes_len)

#             nodes = []
#             for nod in ui_nod_nm_lst:
#                 nodes.append(nuke.toNode(nod))

#             self.get_nodes_info(nodes)
#             self.set_ui_with_knobs()
#             self.lock_first_last()

#             self.set_nodes_count(nodes_len)

#         else:
#             nuke.message('Node Operator panel is empty \n Please Load nodes!')
                
#     def btn_selected_clear_clicked(self):
#         # selected_items = self.table.selectedItems()

#         # remove_nod_nm_lst = []
#         # for item in selected_items:
#         #     row = item.row()
#         #     column = item.column()

#         #     if column == 0:
#         #         remove_nod_nm_lst.append(item.text())

#         remove_nod_nm_lst = self.get_sel_ui_nods_nm()

#         if remove_nod_nm_lst:
#             ui_nod_nm_lst = []
#             for row in range(self.table.rowCount()):
#                 node_nm = self.table.item(row, 0).text()
#                 ui_nod_nm_lst.append(node_nm)  

#             nod_nm_lst_for_add = [ele for ele in ui_nod_nm_lst]
#             for a in remove_nod_nm_lst:
#                 if a in ui_nod_nm_lst:
#                     nod_nm_lst_for_add.remove(a)

#             if nod_nm_lst_for_add:
#                 self.btn_all_clear_clicked()   

#                 nodes_len = len(nod_nm_lst_for_add)
#                 self.set_row_count_to_ui(nodes_len)

#                 nodes = []
#                 for nod in nod_nm_lst_for_add:
#                     nodes.append(nuke.toNode(nod))    

#                 self.get_nodes_info(nodes)
#                 self.set_ui_with_knobs()
#                 self.lock_first_last()

#                 self.set_nodes_count(nodes_len)

#             else:
#                 self.btn_all_clear_clicked()

#     # def on_off_state_changed(self, state):
#     #     selected_items = self.table.selectedItems()

#     #     nod_nm_lst = []
#     #     for item in selected_items:
#     #         column = item.column()

#     #         if column == 0:
#     #             nod_nm_lst.append(item.text())

#     #     if state == 2:
#     #         bln = True
#     #     else:
#     #         bln = False

#     #     if nod_nm_lst:
#     #         nodes = []
#     #         for nod in nod_nm_lst:
#     #             nodes.append(nuke.toNode(nod))  

#     #         for nod in nodes:
#     #             if nod['disable']:
#     #                 nod['disable'].setValue(bln)

#     #         # self.btn_refresh_clicked()
#     #     selected_ranges= self.table.selectedRanges()
#     #     for selected_range in selected_ranges:
#     #         for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
#     #             cell_widget = self.table.cellWidget(row, 1)
           
#     #             # if state:
#     #             #     cell_widget.setChecked(cell_widget.isChecked())
#     #             # else:
#     #             #     cell_widget.setChecked(not cell_widget.isChecked())

#     #             # lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state)
#     #             # self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state)

        


# def main():
#     global window
# #    app = QApplication(sys.argv)
#     window = NodeOperator()
#     window.show()
# #    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()

# ############################################################################



  




import sys
import threading
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QTextEdit, QWidget, QLabel
)
from PySide2.QtCore import Qt
# import shotgun_api3

# ShotGrid configuration (replace with your details)
SHOTGRID_URL = "https://yourshotgridurl.shotgunstudio.com"
SHOTGRID_SCRIPT_NAME = "your_script_name"
SHOTGRID_API_KEY = "your_api_key"

# UI Class
class ShotGridUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShotGrid Path Fetcher")
        self.setGeometry(300, 300, 600, 400)
        self.init_ui()
        self.sg = None

    def init_ui(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Sequence input
        self.sequence_label = QLabel("Enter Sequence Name:")
        layout.addWidget(self.sequence_label)

        self.sequence_input = QLineEdit()
        layout.addWidget(self.sequence_input)

        # Fetch button
        self.fetch_button = QPushButton("Fetch Paths")
        self.fetch_button.clicked.connect(self.start_fetch_thread)
        layout.addWidget(self.fetch_button)

        # Log output
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        layout.addWidget(self.log_output)

    def log_message(self, message):
        """Log messages to the output."""
        self.log_output.append(message)

    def fetch_paths(self):
        """Fetch published and work paths for the given sequence."""
        sequence_name = self.sequence_input.text().strip()
        if not sequence_name:
            self.log_message("Sequence name cannot be empty.")
            return

        try:
            self.log_message("Connecting to ShotGrid...")
            if not self.sg:
                self.sg = shotgun_api3.Shotgun(SHOTGRID_URL, SHOTGRID_SCRIPT_NAME, SHOTGRID_API_KEY)
            
            self.log_message(f"Fetching data for sequence: {sequence_name}...")
            
            # Find the sequence
            sequence = self.sg.find_one("Sequence", [["code", "is", sequence_name]], ["id", "code"])
            if not sequence:
                self.log_message(f"Sequence '{sequence_name}' not found.")
                return
            
            # Fetch published paths and work paths
            published_files = self.sg.find(
                "PublishedFile",
                [["entity", "type_is", "Shot"], ["entity.Sequence.id", "is", sequence["id"]]],
                ["path"]
            )

            work_files = self.sg.find(
                "Task",
                [["entity", "type_is", "Shot"], ["entity.Sequence.id", "is", sequence["id"]]],
                ["sg_work_file"]
            )

            # Log the paths
            self.log_message("Published Paths:")
            for file in published_files:
                self.log_message(file["path"]["local_path"])

            self.log_message("Work Paths:")
            for task in work_files:
                work_path = task.get("sg_work_file")
                if work_path:
                    self.log_message(work_path)

        except Exception as e:
            self.log_message(f"Error fetching paths: {e}")

    def start_fetch_thread(self):
        """Start a thread for fetching paths."""
        fetch_thread = threading.Thread(target=self.fetch_paths)
        fetch_thread.start()


# Main Function
def main():
    app = QApplication(sys.argv)
    window = ShotGridUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



#####################################################################

from PySide2.QtWidgets import QWidget, QApplication,QFileDialog, QTableWidget, QHeaderView,QFrame,QAbstractItemView, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
from PySide2.QtGui import QPixmap, QColor, QFont
from PySide2.QtCore import QSize, Qt, QRect
import sys, os
import nuke
import re
import ast
import json
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
        # self.configure_multi_ops()
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
        self.table.cellClicked.connect(self.cell_clicked)
        self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_import.clicked.connect(self.btn_import_clicked)
        
        

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

    # def configure_multi_ops(self):
    #     self.multi_operation_HLay = QHBoxLayout()

    #     self.btn_export = QPushButton('Export')
    #     self.btn_import = QPushButton('Import')

    #     multi_operation_spacer1 = QSpacerItem(2000, 10, QSizePolicy.Maximum)

    #     self.ck_sel_on_off = QCheckBox('On/Off')
    #     self.ck_sel_on_off.setChecked(False)
    #     self.ck_sel_on_off.stateChanged.connect(self.on_off_state_changed)

    #     self.ck_sel_thumbnail = QCheckBox('Thumbnail')
    #     self.ck_sel_thumbnail.setChecked(False)

    #     self.ck_sel_favorite = QCheckBox('Favorite')
    #     self.ck_sel_favorite.setChecked(False)

    #     self.ck_sel_hide_input = QCheckBox('Hide Input')
    #     self.ck_sel_hide_input.setChecked(False)

    #     multi_operation_spacer2 = QSpacerItem(2000, 10, QSizePolicy.Maximum)

    #     self.cb_sel_colorspace = QComboBox()
    #     self.cb_sel_localized = QComboBox()

    #     self.multi_operation_HLay.addWidget(self.btn_export)
    #     self.multi_operation_HLay.addWidget(self.btn_import)
    #     self.multi_operation_HLay.addSpacerItem(multi_operation_spacer1)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_on_off)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_thumbnail)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_favorite)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_hide_input)
    #     self.multi_operation_HLay.addSpacerItem(multi_operation_spacer2)
    #     self.multi_operation_HLay.addWidget(self.cb_sel_colorspace)
    #     self.multi_operation_HLay.addWidget(self.cb_sel_localized)
        
    #     self.mainVlay.addLayout(self.multi_operation_HLay)

    def add_font_widget(self):
        self.fontHLay = QHBoxLayout()
        self.label_nodes_added = QLabel('Nodes Added : ')    
        self.label_nodes_count = QLabel('')
        self.label_nodes_selected_name = QLabel('Nodes Selected Name : ') 
        self.label_sel_nods_nm = QLabel()

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
        self.btn_bold.setToolTip('Text font will be bold for single or multiple selections in the Node Operator Tool.')    

        self.btn_italic = QPushButton('Italic')
        self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
        self.btn_italic.setIconSize(QSize(12, 12))
        self.btn_italic.setMaximumWidth(75)
        self.btn_italic.setCheckable(True)
        self.btn_italic.setChecked(False)
        self.btn_italic.setToolTip('Text font will be italic for single or multiple selections in the Node Operator Tool.') 

        self.font_size = QLineEdit('11')
        self.font_size.setMaximumWidth(30)
        self.font_size.setToolTip('Text font size will be set for single or multiple selections in the Node Operator Tool.') 

        self.btn_color = QPushButton('Color')
        self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
        self.btn_color.setMaximumWidth(75)
        self.btn_color.setToolTip('Node color will be set for single or multiple selections in the Node Operator Tool.') 

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

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

        # self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.table.setSelectionBehavior(QAbstractItemView.SelectItems)

        


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

    def set_fit_to_screen(self, node_name):
        node = nuke.toNode(node_name)
        xpos = node.xpos()
        ypos = node.ypos()
        nuke.zoom(1, [xpos + node.screenWidth() / 2, ypos + node.screenHeight() / 2])


    def selectNodes(self, sel_nods_nm):
        
        for nod in nuke.allNodes():
            if nod.name() in sel_nods_nm:
                nuke.toNode(nod.name()).setSelected(True)
            else:
                nuke.toNode(nod.name()).setSelected(False)

    def cell_clicked(self):
        
        items = self.table.selectedItems()
        if items:
            if items[0].column() == 0:
                sel_nods_nm = []
                for index, item in enumerate(items):        
                    # print(index, item.text())
                    # print(item.column(), item.text())
                    if item.column() == 0:
                        sel_nods_nm.append(item.text())

                self.label_sel_nods_nm.setText(f'{sel_nods_nm}')

                self.selectNodes(sel_nods_nm)

                if len(sel_nods_nm) == 1:
                    self.set_fit_to_screen(sel_nods_nm[0])

    def update_checkbox_status(self, nod_nm, row, column, checkbox, state):
        print('checkbox -- ', checkbox)

        # if len(self.label_sel_nods_nm.text()) == 0:

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
            # checkbox = QCheckBox('Disabled')
            if column == 1:
                nuke.toNode(nod_nm)['disable'].setValue(False)
            if column == 4:
                nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
            if column == 7:
                nuke.toNode(nod_nm)['bookmark'].setValue(False)
            if column == 8:
                nuke.toNode(nod_nm)['hide_input'].setValue(False) 
 
        # else:
        if not len(self.label_sel_nods_nm.text()) == 0:
            nodes_nm_str = self.label_sel_nods_nm.text()
            nods_nm_lst = ast.literal_eval(nodes_nm_str)

            # print(nods_nm_lst, type(nods_nm_lst)) # ['Blur1', 'Blur10', 'Blur2', 'Blur5', 'Blur6']
            # print('column -- ', column) # 1,4,7,8

            # <PySide2.QtWidgets.QCheckBox(0x1d786e0d290) at 0x000001D782FC3980>
            # <PySide2.QtWidgets.QCheckBox(0x1d78edaa270) at 0x000001D793F40800>

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












########################################################################################
        # print('nod_nm -- ', nod_nm)
        # print('row -- ', row)
        # print('column -- ', column)
        # print('checkbox -- ', checkbox)
        # print('state -- ', state)
        
        # print(self.label_sel_nods_nm)
        # print(type(self.label_sel_nods_nm))
        # print('label_sel_nods_nm -- ', self.label_sel_nods_nm.text(), len(self.label_sel_nods_nm.text()))
        

        # selected_items = self.table.selectedItems()
        # print('selected_items -- ', selected_items)

        # node_nm_row_dict = {}
        # for item in selected_items:
        #     row = item.row()
        #     column = item.column()
        #     if column == 0:
        #         node_nm_row_dict[item.text()] = row, column
        # pprint(node_nm_row_dict)
        

        # # nodes_nm = self.get_sel_ui_nods_nm()

        # selected_items = self.table.selectedItems()
        # print('selected_items -- ', selected_items)
        # # nod_nm_lst = []
        # node_nm_row_dict = {}
        # for item in selected_items:
        #     row = item.row()
        #     column = item.column()

        #     if column == 0:
        #         # nod_nm_lst.append(item.text())
        #         node_nm_row_dict[item.text()] = row
        # pprint(node_nm_row_dict)

        # if node_nm_row_dict:
        #     for nod_nm in node_nm_row_dict.keys():   
        #         _row = node_nm_row_dict[nod_nm]
        #         print('_row -- ', _row)
        #         print('column -- ', column)
        #         table_widget = self.table.item(_row, column) 
        #         # print('type -- ', table_widget.Type)
        #         # print('checkState -- ', table_widget.checkState())
        #         # print('data -- ', table_widget.data())
        #         # print('text -- ', table_widget.text())

        #         if state == Qt.Checked:
        #             # checkbox.setText('Enabled')
        #             # checkbox.setChecked(True)
        #             # table_widget.setText('Enabled')
        #             # table_widget.setChecked(True)
        #             if column == 1:
        #                 nuke.toNode(nod_nm)['disable'].setValue(True)
        #             if column == 4:
        #                 nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
        #             if column == 7:
        #                 nuke.toNode(nod_nm)['bookmark'].setValue(True)
        #             if column == 8:
        #                 nuke.toNode(nod_nm)['hide_input'].setValue(True)                

        #         else:
        #             # checkbox.setText('Disabled')
        #             # checkbox = QCheckBox('Disabled')
        #             # table_widget.setText('Disabled')
        #             # table_widget.setChecked(False)

        #             if column == 1:
        #                 nuke.toNode(nod_nm)['disable'].setValue(False)
        #             if column == 4:
        #                 nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
        #             if column == 7:
        #                 nuke.toNode(nod_nm)['bookmark'].setValue(False)
        #             if column == 8:
        #                 nuke.toNode(nod_nm)['hide_input'].setValue(False)    
        # else:
        #     if state == Qt.Checked:
        #         checkbox.setText('Enabled')
        #         checkbox.setChecked(True)
        #         if column == 1:
        #             nuke.toNode(nod_nm)['disable'].setValue(True)
        #         if column == 4:
        #             nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
        #         if column == 7:
        #             nuke.toNode(nod_nm)['bookmark'].setValue(True)
        #         if column == 8:
        #             nuke.toNode(nod_nm)['hide_input'].setValue(True)                

        #     else:
        #         checkbox.setText('Disabled')
        #         checkbox = QCheckBox('Disabled')
        #         if column == 1:
        #             nuke.toNode(nod_nm)['disable'].setValue(False)
        #         if column == 4:
        #             nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
        #         if column == 7:
        #             nuke.toNode(nod_nm)['bookmark'].setValue(False)
        #         if column == 8:
        #             nuke.toNode(nod_nm)['hide_input'].setValue(False) 

 


    def get_sel_ui_nods_nm(self):
        selected_items = self.table.selectedItems()

        nod_nm_lst = []
        for item in selected_items:
            row = item.row()
            column = item.column()

            if column == 0:
                nod_nm_lst.append(item.text())

        return nod_nm_lst

    def set_chekckbox(self, bln, row_index, col):    
            # checkbox_widget = QWidget()
            # checkbox_layout = QHBoxLayout(checkbox_widget)
            # checkbox_layout.setContentsMargins(0,0,0,0)
            # checkbox_layout.setAlignment(Qt.AlignCenter)

            changed_val_nod_nm = self.table.item(row_index, 0).text()

            if bln:
                checkbox = QCheckBox('Enabled')
                checkbox.setChecked(True)
            else:
                checkbox = QCheckBox('Disabled')
                checkbox.setChecked(False)

            # checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state, nodes_nm))
            checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))

            # checkbox_layout.addWidget(checkbox)
            # self.table.setCellWidget(row_index, col, checkbox_widget)
            self.table.setCellWidget(row_index, col, checkbox)

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

    def colorspace_index_changed(self, combo_box, col):
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
                    # print('dir combobox_item -- ', dir(combobox_item))
                    # 'setCurrentIndex',
                    #     'setCurrentText',



    def adjust_combobox_width(self, row, column):
        """Adjust ComboBox width to fit the column size."""
        widget = self.table.cellWidget(row, column)
        if isinstance(widget, QComboBox):
            column_width = self.table.columnWidth(column)
            widget.setFixedWidth(column_width)

    def adjust_combobox_widths(self):
            """Adjust all ComboBoxes in the table."""
            for row in range(self.table.rowCount()):
                for column in range(self.table.columnCount()):
                    self.adjust_combobox_width(row, column)

    def set_combo_companies(self, node_nm, knob_nm, row_index, col):
            self.colorspace_combobox = QComboBox()
                 
            values = nuke.toNode(node_nm)[knob_nm].values()
            self.colorspace_combobox.addItems(values)
            self.table.setCellWidget(row_index, col, self.colorspace_combobox)

            self.adjust_combobox_width(row_index, col)
            # col_width = self.table.columnWidth(col)  
            # comb_widget = self.table.cellWidget(row_index, col) 
            # comb_widget.setFixedWidth(col_width)
            
            value = nuke.toNode(node_nm)[knob_nm].value()
            index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
            self.colorspace_combobox.setCurrentIndex(index)

            # self.colorspace_combobox.currentIndexChanged.connect(lambda state, r=row_index, c=col: self.colorspace_index_changed(r, c, state))
            self.colorspace_combobox.currentIndexChanged.connect(lambda text, c=col, combo_box=self.colorspace_combobox: self.colorspace_index_changed(combo_box, c))

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
        self.btn_export.setEnabled(True)
        

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
        self.btn_export.setEnabled(True)

    def btn_all_clear_clicked(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setColumnCount(10)
        self.btn_add.setEnabled(False)
        self.set_nodes_count('')
        self.btn_export.setEnabled(False)
        
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

            self.label_sel_nods_nm.setText('')

        else:
            nuke.message('Node Operator panel is empty \n Please Load nodes!')
                
    def btn_selected_clear_clicked(self):
        # selected_items = self.table.selectedItems()

        # remove_nod_nm_lst = []
        # for item in selected_items:
        #     row = item.row()
        #     column = item.column()

        #     if column == 0:
        #         remove_nod_nm_lst.append(item.text())

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

    # def on_off_state_changed(self, state):
    #     selected_items = self.table.selectedItems()

    #     nod_nm_lst = []
    #     for item in selected_items:
    #         column = item.column()

    #         if column == 0:
    #             nod_nm_lst.append(item.text())

    #     if state == 2:
    #         bln = True
    #     else:
    #         bln = False

    #     if nod_nm_lst:
    #         nodes = []
    #         for nod in nod_nm_lst:
    #             nodes.append(nuke.toNode(nod))  

    #         for nod in nodes:
    #             if nod['disable']:
    #                 nod['disable'].setValue(bln)

    #         # self.btn_refresh_clicked()
    #     selected_ranges= self.table.selectedRanges()
    #     for selected_range in selected_ranges:
    #         for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
    #             cell_widget = self.table.cellWidget(row, 1)
           
    #             # if state:
    #             #     cell_widget.setChecked(cell_widget.isChecked())
    #             # else:
    #             #     cell_widget.setChecked(not cell_widget.isChecked())

    #             # lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state)
    #             # self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state)

        

    def btn_export_clicked(self):
        # self.path_to_export = QFileDialog.getOpenFileName()
        # self.path_to_export = QFileDialog.getSaveFileName()
        # print('self.path_to_export -- ', self.path_to_export)

        all_ui_nod_nm_lst = []
        for row in range(self.table.rowCount()):
            node_nm = self.table.item(row, 0).text()
            all_ui_nod_nm_lst.append(node_nm)

        if all_ui_nod_nm_lst:
            file_dialog = QFileDialog()
            save_file_path, _ = file_dialog.getSaveFileName(self, "Export content", "", "JSON (*.json)")  # Extract the file path

            if save_file_path:  # Ensure the user didn't cancel the dialog
                print('save_file_path -- ', save_file_path)
                try:
                    with open(save_file_path, 'w') as json_file:
                        json.dump(all_ui_nod_nm_lst, json_file, indent=4)
                    nuke.message(f"Node information saved to : {save_file_path}")
                except Exception as e:
                    nuke.message(f"Failed to save file: {e}")
            else:
                nuke.message("Save operation was canceled.")

    def btn_import_clicked(self):
        file_dialog = QFileDialog()
        path_to_import, _  = file_dialog.getOpenFileName(self, "Import content", "", "JSON (*.json)")

        data = None
        if path_to_import:
            try:
                with open(path_to_import, 'r') as f:
                    data = json.load(f)
                    print('data -- ', data)
            except Exception as e:
                    nuke.message(f"Error reading JSON file: {e}")

        print('data -- ', data)
        if data:

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




def main():
    global window
#    app = QApplication(sys.argv)
    window = NodeOperator()
    window.show()
#    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

############################################################################



  






from PySide2.QtWidgets import QWidget, QApplication,QFileDialog, QTableWidget, QHeaderView,QFrame,QAbstractItemView, QHBoxLayout, QVBoxLayout, QSizePolicy,QTableWidgetItem, QSpacerItem, QLabel, QLineEdit, QComboBox, QCheckBox, QPushButton
from PySide2.QtGui import QPixmap, QColor, QFont
from PySide2.QtCore import QSize, Qt, QRect
import sys, os
import nuke
import re
import ast
import json
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
        # self.configure_multi_ops()
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
        self.table.cellClicked.connect(self.cell_clicked)
        self.btn_refresh.clicked.connect(self.btn_refresh_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_import.clicked.connect(self.btn_import_clicked)
        
        

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

    # def configure_multi_ops(self):
    #     self.multi_operation_HLay = QHBoxLayout()

    #     self.btn_export = QPushButton('Export')
    #     self.btn_import = QPushButton('Import')

    #     multi_operation_spacer1 = QSpacerItem(2000, 10, QSizePolicy.Maximum)

    #     self.ck_sel_on_off = QCheckBox('On/Off')
    #     self.ck_sel_on_off.setChecked(False)
    #     self.ck_sel_on_off.stateChanged.connect(self.on_off_state_changed)

    #     self.ck_sel_thumbnail = QCheckBox('Thumbnail')
    #     self.ck_sel_thumbnail.setChecked(False)

    #     self.ck_sel_favorite = QCheckBox('Favorite')
    #     self.ck_sel_favorite.setChecked(False)

    #     self.ck_sel_hide_input = QCheckBox('Hide Input')
    #     self.ck_sel_hide_input.setChecked(False)

    #     multi_operation_spacer2 = QSpacerItem(2000, 10, QSizePolicy.Maximum)

    #     self.cb_sel_colorspace = QComboBox()
    #     self.cb_sel_localized = QComboBox()

    #     self.multi_operation_HLay.addWidget(self.btn_export)
    #     self.multi_operation_HLay.addWidget(self.btn_import)
    #     self.multi_operation_HLay.addSpacerItem(multi_operation_spacer1)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_on_off)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_thumbnail)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_favorite)
    #     self.multi_operation_HLay.addWidget(self.ck_sel_hide_input)
    #     self.multi_operation_HLay.addSpacerItem(multi_operation_spacer2)
    #     self.multi_operation_HLay.addWidget(self.cb_sel_colorspace)
    #     self.multi_operation_HLay.addWidget(self.cb_sel_localized)
        
    #     self.mainVlay.addLayout(self.multi_operation_HLay)

    def add_font_widget(self):
        self.fontHLay = QHBoxLayout()
        self.label_nodes_added = QLabel('Nodes Added : ')    
        self.label_nodes_count = QLabel('')
        self.label_nodes_selected_name = QLabel('Nodes Selected Name : ') 
        self.label_sel_nods_nm = QLabel()

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
        self.btn_bold.setToolTip('Text font will be bold for single or multiple selections in the Node Operator Tool.')    

        self.btn_italic = QPushButton('Italic')
        self.btn_italic.setIcon(QPixmap(os.path.join(icons_dir_path, 'italic_icon1.png')))
        self.btn_italic.setIconSize(QSize(12, 12))
        self.btn_italic.setMaximumWidth(75)
        self.btn_italic.setCheckable(True)
        self.btn_italic.setChecked(False)
        self.btn_italic.setToolTip('Text font will be italic for single or multiple selections in the Node Operator Tool.') 

        self.font_size = QLineEdit('11')
        self.font_size.setMaximumWidth(30)
        self.font_size.setToolTip('Text font size will be set for single or multiple selections in the Node Operator Tool.') 

        self.btn_color = QPushButton('Color')
        self.btn_color.setIcon(QPixmap(os.path.join(icons_dir_path, 'tile_color_icon.png')))
        self.btn_color.setMaximumWidth(75)
        self.btn_color.setToolTip('Node color will be set for single or multiple selections in the Node Operator Tool.') 

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.VLine)
        self.separator.setFrameShadow(QFrame.Sunken)

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

        # self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.table.setSelectionBehavior(QAbstractItemView.SelectItems)

        


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

    def set_fit_to_screen(self, node_name):
        node = nuke.toNode(node_name)
        xpos = node.xpos()
        ypos = node.ypos()
        nuke.zoom(1, [xpos + node.screenWidth() / 2, ypos + node.screenHeight() / 2])


    def selectNodes(self, sel_nods_nm):
        
        for nod in nuke.allNodes():
            if nod.name() in sel_nods_nm:
                nuke.toNode(nod.name()).setSelected(True)
            else:
                nuke.toNode(nod.name()).setSelected(False)

    def cell_clicked(self):
        
        items = self.table.selectedItems()
        if items:
            if items[0].column() == 0:
                sel_nods_nm = []
                for index, item in enumerate(items):        
                    # print(index, item.text())
                    # print(item.column(), item.text())
                    if item.column() == 0:
                        sel_nods_nm.append(item.text())

                self.label_sel_nods_nm.setText(f'{sel_nods_nm}')

                self.selectNodes(sel_nods_nm)

                if len(sel_nods_nm) == 1:
                    self.set_fit_to_screen(sel_nods_nm[0])

    def update_checkbox_status(self, nod_nm, row, column, checkbox, state):
        print('checkbox -- ', checkbox)

        # if len(self.label_sel_nods_nm.text()) == 0:

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
            # checkbox = QCheckBox('Disabled')
            if column == 1:
                nuke.toNode(nod_nm)['disable'].setValue(False)
            if column == 4:
                nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
            if column == 7:
                nuke.toNode(nod_nm)['bookmark'].setValue(False)
            if column == 8:
                nuke.toNode(nod_nm)['hide_input'].setValue(False) 
 
        # else:
        if not len(self.label_sel_nods_nm.text()) == 0:
            nodes_nm_str = self.label_sel_nods_nm.text()
            nods_nm_lst = ast.literal_eval(nodes_nm_str)

            # print(nods_nm_lst, type(nods_nm_lst)) # ['Blur1', 'Blur10', 'Blur2', 'Blur5', 'Blur6']
            # print('column -- ', column) # 1,4,7,8

            # <PySide2.QtWidgets.QCheckBox(0x1d786e0d290) at 0x000001D782FC3980>
            # <PySide2.QtWidgets.QCheckBox(0x1d78edaa270) at 0x000001D793F40800>

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












########################################################################################
        # print('nod_nm -- ', nod_nm)
        # print('row -- ', row)
        # print('column -- ', column)
        # print('checkbox -- ', checkbox)
        # print('state -- ', state)
        
        # print(self.label_sel_nods_nm)
        # print(type(self.label_sel_nods_nm))
        # print('label_sel_nods_nm -- ', self.label_sel_nods_nm.text(), len(self.label_sel_nods_nm.text()))
        

        # selected_items = self.table.selectedItems()
        # print('selected_items -- ', selected_items)

        # node_nm_row_dict = {}
        # for item in selected_items:
        #     row = item.row()
        #     column = item.column()
        #     if column == 0:
        #         node_nm_row_dict[item.text()] = row, column
        # pprint(node_nm_row_dict)
        

        # # nodes_nm = self.get_sel_ui_nods_nm()

        # selected_items = self.table.selectedItems()
        # print('selected_items -- ', selected_items)
        # # nod_nm_lst = []
        # node_nm_row_dict = {}
        # for item in selected_items:
        #     row = item.row()
        #     column = item.column()

        #     if column == 0:
        #         # nod_nm_lst.append(item.text())
        #         node_nm_row_dict[item.text()] = row
        # pprint(node_nm_row_dict)

        # if node_nm_row_dict:
        #     for nod_nm in node_nm_row_dict.keys():   
        #         _row = node_nm_row_dict[nod_nm]
        #         print('_row -- ', _row)
        #         print('column -- ', column)
        #         table_widget = self.table.item(_row, column) 
        #         # print('type -- ', table_widget.Type)
        #         # print('checkState -- ', table_widget.checkState())
        #         # print('data -- ', table_widget.data())
        #         # print('text -- ', table_widget.text())

        #         if state == Qt.Checked:
        #             # checkbox.setText('Enabled')
        #             # checkbox.setChecked(True)
        #             # table_widget.setText('Enabled')
        #             # table_widget.setChecked(True)
        #             if column == 1:
        #                 nuke.toNode(nod_nm)['disable'].setValue(True)
        #             if column == 4:
        #                 nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
        #             if column == 7:
        #                 nuke.toNode(nod_nm)['bookmark'].setValue(True)
        #             if column == 8:
        #                 nuke.toNode(nod_nm)['hide_input'].setValue(True)                

        #         else:
        #             # checkbox.setText('Disabled')
        #             # checkbox = QCheckBox('Disabled')
        #             # table_widget.setText('Disabled')
        #             # table_widget.setChecked(False)

        #             if column == 1:
        #                 nuke.toNode(nod_nm)['disable'].setValue(False)
        #             if column == 4:
        #                 nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
        #             if column == 7:
        #                 nuke.toNode(nod_nm)['bookmark'].setValue(False)
        #             if column == 8:
        #                 nuke.toNode(nod_nm)['hide_input'].setValue(False)    
        # else:
        #     if state == Qt.Checked:
        #         checkbox.setText('Enabled')
        #         checkbox.setChecked(True)
        #         if column == 1:
        #             nuke.toNode(nod_nm)['disable'].setValue(True)
        #         if column == 4:
        #             nuke.toNode(nod_nm)['postage_stamp'].setValue(True)
        #         if column == 7:
        #             nuke.toNode(nod_nm)['bookmark'].setValue(True)
        #         if column == 8:
        #             nuke.toNode(nod_nm)['hide_input'].setValue(True)                

        #     else:
        #         checkbox.setText('Disabled')
        #         checkbox = QCheckBox('Disabled')
        #         if column == 1:
        #             nuke.toNode(nod_nm)['disable'].setValue(False)
        #         if column == 4:
        #             nuke.toNode(nod_nm)['postage_stamp'].setValue(False)
        #         if column == 7:
        #             nuke.toNode(nod_nm)['bookmark'].setValue(False)
        #         if column == 8:
        #             nuke.toNode(nod_nm)['hide_input'].setValue(False) 

 


    def get_sel_ui_nods_nm(self):
        selected_items = self.table.selectedItems()

        nod_nm_lst = []
        for item in selected_items:
            row = item.row()
            column = item.column()

            if column == 0:
                nod_nm_lst.append(item.text())

        return nod_nm_lst

    def set_chekckbox(self, bln, row_index, col):    
            # checkbox_widget = QWidget()
            # checkbox_layout = QHBoxLayout(checkbox_widget)
            # checkbox_layout.setContentsMargins(0,0,0,0)
            # checkbox_layout.setAlignment(Qt.AlignCenter)

            changed_val_nod_nm = self.table.item(row_index, 0).text()

            if bln:
                checkbox = QCheckBox('Enabled')
                checkbox.setChecked(True)
            else:
                checkbox = QCheckBox('Disabled')
                checkbox.setChecked(False)

            # checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state, nodes_nm))
            checkbox.stateChanged.connect(lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state))

            # checkbox_layout.addWidget(checkbox)
            # self.table.setCellWidget(row_index, col, checkbox_widget)
            self.table.setCellWidget(row_index, col, checkbox)

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

    def colorspace_index_changed(self, combo_box, col):
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
                    # print('dir combobox_item -- ', dir(combobox_item))
                    # 'setCurrentIndex',
                    #     'setCurrentText',



    def adjust_combobox_width(self, row, column):
        """Adjust ComboBox width to fit the column size."""
        widget = self.table.cellWidget(row, column)
        if isinstance(widget, QComboBox):
            column_width = self.table.columnWidth(column)
            widget.setFixedWidth(column_width)

    def adjust_combobox_widths(self):
            """Adjust all ComboBoxes in the table."""
            for row in range(self.table.rowCount()):
                for column in range(self.table.columnCount()):
                    self.adjust_combobox_width(row, column)

    def set_combo_companies(self, node_nm, knob_nm, row_index, col):
            self.colorspace_combobox = QComboBox()
                 
            values = nuke.toNode(node_nm)[knob_nm].values()
            self.colorspace_combobox.addItems(values)
            self.table.setCellWidget(row_index, col, self.colorspace_combobox)

            self.adjust_combobox_width(row_index, col)
            # col_width = self.table.columnWidth(col)  
            # comb_widget = self.table.cellWidget(row_index, col) 
            # comb_widget.setFixedWidth(col_width)
            
            value = nuke.toNode(node_nm)[knob_nm].value()
            index = self.colorspace_combobox.findText(str(value), Qt.MatchFixedString)
            self.colorspace_combobox.setCurrentIndex(index)

            # self.colorspace_combobox.currentIndexChanged.connect(lambda state, r=row_index, c=col: self.colorspace_index_changed(r, c, state))
            self.colorspace_combobox.currentIndexChanged.connect(lambda text, c=col, combo_box=self.colorspace_combobox: self.colorspace_index_changed(combo_box, c))

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
        self.btn_export.setEnabled(True)
        

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
        self.btn_export.setEnabled(True)

    def btn_all_clear_clicked(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.table.setColumnCount(10)
        self.btn_add.setEnabled(False)
        self.set_nodes_count('')
        self.btn_export.setEnabled(False)
        
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

            self.label_sel_nods_nm.setText('')

        else:
            nuke.message('Node Operator panel is empty \n Please Load nodes!')
                
    def btn_selected_clear_clicked(self):
        # selected_items = self.table.selectedItems()

        # remove_nod_nm_lst = []
        # for item in selected_items:
        #     row = item.row()
        #     column = item.column()

        #     if column == 0:
        #         remove_nod_nm_lst.append(item.text())

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

    # def on_off_state_changed(self, state):
    #     selected_items = self.table.selectedItems()

    #     nod_nm_lst = []
    #     for item in selected_items:
    #         column = item.column()

    #         if column == 0:
    #             nod_nm_lst.append(item.text())

    #     if state == 2:
    #         bln = True
    #     else:
    #         bln = False

    #     if nod_nm_lst:
    #         nodes = []
    #         for nod in nod_nm_lst:
    #             nodes.append(nuke.toNode(nod))  

    #         for nod in nodes:
    #             if nod['disable']:
    #                 nod['disable'].setValue(bln)

    #         # self.btn_refresh_clicked()
    #     selected_ranges= self.table.selectedRanges()
    #     for selected_range in selected_ranges:
    #         for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
    #             cell_widget = self.table.cellWidget(row, 1)
           
    #             # if state:
    #             #     cell_widget.setChecked(cell_widget.isChecked())
    #             # else:
    #             #     cell_widget.setChecked(not cell_widget.isChecked())

    #             # lambda state, r=row_index, c=col, cb=checkbox: self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state)
    #             # self.update_checkbox_status(changed_val_nod_nm, r, c, cb, state)

        

    def btn_export_clicked(self):
        # self.path_to_export = QFileDialog.getOpenFileName()
        # self.path_to_export = QFileDialog.getSaveFileName()
        # print('self.path_to_export -- ', self.path_to_export)

        all_ui_nod_nm_lst = []
        for row in range(self.table.rowCount()):
            node_nm = self.table.item(row, 0).text()
            all_ui_nod_nm_lst.append(node_nm)

        if all_ui_nod_nm_lst:
            file_dialog = QFileDialog()
            save_file_path, _ = file_dialog.getSaveFileName(self, "Export content", "", "JSON (*.json)")  # Extract the file path

            if save_file_path:  # Ensure the user didn't cancel the dialog
                print('save_file_path -- ', save_file_path)
                try:
                    with open(save_file_path, 'w') as json_file:
                        json.dump(all_ui_nod_nm_lst, json_file, indent=4)
                    nuke.message(f"Node information saved to : {save_file_path}")
                except Exception as e:
                    nuke.message(f"Failed to save file: {e}")
            else:
                nuke.message("Save operation was canceled.")

    def btn_import_clicked(self):
        file_dialog = QFileDialog()
        path_to_import, _  = file_dialog.getOpenFileName(self, "Import content", "", "JSON (*.json)")

        data = None
        if path_to_import:
            try:
                with open(path_to_import, 'r') as f:
                    data = json.load(f)
                    print('data -- ', data)
            except Exception as e:
                    nuke.message(f"Error reading JSON file: {e}")

        print('data -- ', data)
        if data:

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




def main():
    global window
#    app = QApplication(sys.argv)
    window = NodeOperator()
    window.show()
#    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

############################################################################



  













































































