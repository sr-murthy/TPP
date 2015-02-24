'''
    Parser for the TPP triple raw data contained in static HTML tables containing subgroup TPP data and JSON files containing GAP small groups information.
'''
import collections, io, json

class TPPTripleDataParser:

    small_groups_JSON_schema = {
      'GAP_ID': { 'JSON_type': 'array', 'python_type': tuple, 'length': 2 },
      'order': { 'JSON_type': 'number', 'python_type': int },
      'GAP_desc': { 'JSON_type': 'string', 'python_type': str },
      'GAP_pickled_ID': { 'JSON_type': 'string', 'python_type': str },
      'index_LAN_subgroup': { 'JSON_type': 'number', 'python_type': int },
      'index_LCN_subgroup': { 'JSON_type': 'number', 'python_type': int },
      'index_LEAN_subgroup': { 'JSON_type': 'number', 'python_type': int },
      'is_abelian': { 'JSON_type': 'boolean', 'python_type': bool },
      'comm_length': { 'JSON_type': 'number', 'python_type': int },
      'is_cyclic': { 'JSON_type': 'boolean', 'python_type': bool },
      'is_elem_abelian': { 'JSON_type': 'boolean', 'python_type': bool },
      'is_simple': { 'JSON_type': 'boolean', 'python_type': bool },
      'comp_length': { 'JSON_type': 'number', 'python_type': int },
      'is_nilpotent': { 'JSON_type': 'boolean', 'python_type': bool },
      'nilpotency_class': { 'JSON_type': 'number', 'python_type': int },
      'is_solvable': { 'JSON_type': 'boolean', 'python_type': bool },
      'derived_length': { 'JSON_type': 'number', 'python_type': int },
      'is_pgroup': { 'JSON_type': 'boolean', 'python_type': bool },
      'generators': { 'JSON_type': 'string', 'python_type': str },
      'char_degrees': { 'JSON_type': 'string', 'python_type': str },
      'D3': { 'JSON_type': 'number', 'python_type': int },
      'MBS_STPP_param_type': { 'JSON_type': 'array', 'python_type': tuple, 'length': 3 },
      'Beta0': { 'JSON_type': 'number', 'python_type': int }
    }

    TPP_excluded_small_groups = [ (128,[2320]),(192,range( 1541, 1543)),(288,[1040]),
                              (288,[1044]),(320,range( 1276, 1641 )),(324,[169]),
                              (324,[175]),(384,range( 1336,20170)),(432,),(448,),
                              (480,range( 824,1214 )),(486,range( 242,262 )),
                              (512,),(544,),(576,range( 520,8682 )),(640,),
                              (648,range( 334,758 )),(672,range( 684,1281 )),
                              (686,[14]),(704,range( 487,1388 )),(720,range( 473,841 )),
                              (729,range( 122,505 )),(736,[194]),(756,range( 172,190 )),
                              (768,),(784,range( 132,173)),(800,range( 218,1212 )),
                              (810,range( 95, 114 )),(832,range( 298,1631 )),
                              (880,),(900,),(912,),(928,),(960,),(972,),
                              (992,),(1000,)]

    GAP_small_groups_numeric_info_order_1_to_1000 = collections.OrderedDict( [(1, 1), (2, 1), (3, 1), (4, 2), (5, 1), (6, 2), (7, 1), (8, 5), (9, 2), (10, 2), (11, 1), (12, 5), (13, 1), (14, 2), (15, 1), (16, 14), (17, 1), (18, 5), (19, 1), (20, 5), (21, 2), (22, 2), (23, 1), (24, 15), (25, 2), (26, 2), (27, 5), (28, 4), (29, 1), (30, 4), (31, 1), (32, 51), (33, 1), (34, 2), (35, 1), (36, 14), (37, 1), (38, 2), (39, 2), (40, 14), (41, 1), (42, 6), (43, 1), (44, 4), (45, 2), (46, 2), (47, 1), (48, 52), (49, 2), (50, 5), (51, 1), (52, 5), (53, 1), (54, 15), (55, 2), (56, 13), (57, 2), (58, 2), (59, 1), (60, 13), (61, 1), (62, 2), (63, 4), (64, 267), (65, 1), (66, 4), (67, 1), (68, 5), (69, 1), (70, 4), (71, 1), (72, 50), (73, 1), (74, 2), (75, 3), (76, 4), (77, 1), (78, 6), (79, 1), (80, 52), (81, 15), (82, 2), (83, 1), (84, 15), (85, 1), (86, 2), (87, 1), (88, 12), (89, 1), (90, 10), (91, 1), (92, 4), (93, 2), (94, 2), (95, 1), (96, 231), (97, 1), (98, 5), (99, 2), (100, 16), (101, 1), (102, 4), (103, 1), (104, 14), (105, 2), (106, 2), (107, 1), (108, 45), (109, 1), (110, 6), (111, 2), (112, 43), (113, 1), (114, 6), (115, 1), (116, 5), (117, 4), (118, 2), (119, 1), (120, 47), (121, 2), (122, 2), (123, 1), (124, 4), (125, 5), (126, 16), (127, 1), (128, 2328), (129, 2), (130, 4), (131, 1), (132, 10), (133, 1), (134, 2), (135, 5), (136, 15), (137, 1), (138, 4), (139, 1), (140, 11), (141, 1), (142, 2), (143, 1), (144, 197), (145, 1), (146, 2), (147, 6), (148, 5), (149, 1), (150, 13), (151, 1), (152, 12), (153, 2), (154, 4), (155, 2), (156, 18), (157, 1), (158, 2), (159, 1), (160, 238), (161, 1), (162, 55), (163, 1), (164, 5), (165, 2), (166, 2), (167, 1), (168, 57), (169, 2), (170, 4), (171, 5), (172, 4), (173, 1), (174, 4), (175, 2), (176, 42), (177, 1), (178, 2), (179, 1), (180, 37), (181, 1), (182, 4), (183, 2), (184, 12), (185, 1), (186, 6), (187, 1), (188, 4), (189, 13), (190, 4), (191, 1), (192, 1543), (193, 1), (194, 2), (195, 2), (196, 12), (197, 1), (198, 10), (199, 1), (200, 52), (201, 2), (202, 2), (203, 2), (204, 12), (205, 2), (206, 2), (207, 2), (208, 51), (209, 1), (210, 12), (211, 1), (212, 5), (213, 1), (214, 2), (215, 1), (216, 177), (217, 1), (218, 2), (219, 2), (220, 15), (221, 1), (222, 6), (223, 1), (224, 197), (225, 6), (226, 2), (227, 1), (228, 15), (229, 1), (230, 4), (231, 2), (232, 14), (233, 1), (234, 16), (235, 1), (236, 4), (237, 2), (238, 4), (239, 1), (240, 208), (241, 1), (242, 5), (243, 67), (244, 5), (245, 2), (246, 4), (247, 1), (248, 12), (249, 1), (250, 15), (251, 1), (252, 46), (253, 2), (254, 2), (255, 1), (256, 56092), (257, 1), (258, 6), (259, 1), (260, 15), (261, 2), (262, 2), (263, 1), (264, 39), (265, 1), (266, 4), (267, 1), (268, 4), (269, 1), (270, 30), (271, 1), (272, 54), (273, 5), (274, 2), (275, 4), (276, 10), (277, 1), (278, 2), (279, 4), (280, 40), (281, 1), (282, 4), (283, 1), (284, 4), (285, 2), (286, 4), (287, 1), (288, 1045), (289, 2), (290, 4), (291, 2), (292, 5), (293, 1), (294, 23), (295, 1), (296, 14), (297, 5), (298, 2), (299, 1), (300, 49), (301, 2), (302, 2), (303, 1), (304, 42), (305, 2), (306, 10), (307, 1), (308, 9), (309, 2), (310, 6), (311, 1), (312, 61), (313, 1), (314, 2), (315, 4), (316, 4), (317, 1), (318, 4), (319, 1), (320, 1640), (321, 1), (322, 4), (323, 1), (324, 176), (325, 2), (326, 2), (327, 2), (328, 15), (329, 1), (330, 12), (331, 1), (332, 4), (333, 5), (334, 2), (335, 1), (336, 228), (337, 1), (338, 5), (339, 1), (340, 15), (341, 1), (342, 18), (343, 5), (344, 12), (345, 1), (346, 2), (347, 1), (348, 12), (349, 1), (350, 10), (351, 14), (352, 195), (353, 1), (354, 4), (355, 2), (356, 5), (357, 2), (358, 2), (359, 1), (360, 162), (361, 2), (362, 2), (363, 3), (364, 11), (365, 1), (366, 6), (367, 1), (368, 42), (369, 2), (370, 4), (371, 1), (372, 15), (373, 1), (374, 4), (375, 7), (376, 12), (377, 1), (378, 60), (379, 1), (380, 11), (381, 2), (382, 2), (383, 1), (384, 20169), (385, 2), (386, 2), (387, 4), (388, 5), (389, 1), (390, 12), (391, 1), (392, 44), (393, 1), (394, 2), (395, 1), (396, 30), (397, 1), (398, 2), (399, 5), (400, 221), (401, 1), (402, 6), (403, 1), (404, 5), (405, 16), (406, 6), (407, 1), (408, 46), (409, 1), (410, 6), (411, 1), (412, 4), (413, 1), (414, 10), (415, 1), (416, 235), (417, 2), (418, 4), (419, 1), (420, 41), (421, 1), (422, 2), (423, 2), (424, 14), (425, 2), (426, 4), (427, 1), (428, 4), (429, 2), (430, 4), (431, 1), (432, 775), (433, 1), (434, 4), (435, 1), (436, 5), (437, 1), (438, 6), (439, 1), (440, 51), (441, 13), (442, 4), (443, 1), (444, 18), (445, 1), (446, 2), (447, 1), (448, 1396), (449, 1), (450, 34), (451, 1), (452, 5), (453, 2), (454, 2), (455, 1), (456, 54), (457, 1), (458, 2), (459, 5), (460, 11), (461, 1), (462, 12), (463, 1), (464, 51), (465, 4), (466, 2), (467, 1), (468, 55), (469, 1), (470, 4), (471, 2), (472, 12), (473, 1), (474, 6), (475, 2), (476, 11), (477, 2), (478, 2), (479, 1), (480, 1213), (481, 1), (482, 2), (483, 2), (484, 12), (485, 1), (486, 261), (487, 1), (488, 14), (489, 2), (490, 10), (491, 1), (492, 12), (493, 1), (494, 4), (495, 4), (496, 42), (497, 2), (498, 4), (499, 1), (500, 56), (501, 1), (502, 2), (503, 1), (504, 202), (505, 2), (506, 6), (507, 6), (508, 4), (509, 1), (510, 8), (511, 1), (512, 10494213), (513, 15), (514, 2), (515, 1), (516, 15), (517, 1), (518, 4), (519, 1), (520, 49), (521, 1), (522, 10), (523, 1), (524, 4), (525, 6), (526, 2), (527, 1), (528, 170), (529, 2), (530, 4), (531, 2), (532, 9), (533, 1), (534, 4), (535, 1), (536, 12), (537, 1), (538, 2), (539, 2), (540, 119), (541, 1), (542, 2), (543, 2), (544, 246), (545, 1), (546, 24), (547, 1), (548, 5), (549, 4), (550, 16), (551, 1), (552, 39), (553, 1), (554, 2), (555, 2), (556, 4), (557, 1), (558, 16), (559, 1), (560, 180), (561, 1), (562, 2), (563, 1), (564, 10), (565, 1), (566, 2), (567, 49), (568, 12), (569, 1), (570, 12), (571, 1), (572, 11), (573, 1), (574, 4), (575, 2), (576, 8681), (577, 1), (578, 5), (579, 2), (580, 15), (581, 1), (582, 6), (583, 1), (584, 15), (585, 4), (586, 2), (587, 1), (588, 66), (589, 1), (590, 4), (591, 1), (592, 51), (593, 1), (594, 30), (595, 1), (596, 5), (597, 2), (598, 4), (599, 1), (600, 205), (601, 1), (602, 6), (603, 4), (604, 4), (605, 7), (606, 4), (607, 1), (608, 195), (609, 3), (610, 6), (611, 1), (612, 36), (613, 1), (614, 2), (615, 2), (616, 35), (617, 1), (618, 6), (619, 1), (620, 15), (621, 5), (622, 2), (623, 1), (624, 260), (625, 15), (626, 2), (627, 2), (628, 5), (629, 1), (630, 32), (631, 1), (632, 12), (633, 2), (634, 2), (635, 1), (636, 12), (637, 2), (638, 4), (639, 2), (640, 21541), (641, 1), (642, 4), (643, 1), (644, 9), (645, 2), (646, 4), (647, 1), (648, 757), (649, 1), (650, 10), (651, 5), (652, 4), (653, 1), (654, 6), (655, 2), (656, 53), (657, 5), (658, 4), (659, 1), (660, 40), (661, 1), (662, 2), (663, 2), (664, 12), (665, 1), (666, 18), (667, 1), (668, 4), (669, 2), (670, 4), (671, 1), (672, 1280), (673, 1), (674, 2), (675, 17), (676, 16), (677, 1), (678, 4), (679, 1), (680, 53), (681, 1), (682, 4), (683, 1), (684, 51), (685, 1), (686, 15), (687, 2), (688, 42), (689, 2), (690, 8), (691, 1), (692, 5), (693, 4), (694, 2), (695, 1), (696, 44), (697, 1), (698, 2), (699, 1), (700, 36), (701, 1), (702, 62), (703, 1), (704, 1387), (705, 1), (706, 2), (707, 1), (708, 10), (709, 1), (710, 6), (711, 4), (712, 15), (713, 1), (714, 12), (715, 2), (716, 4), (717, 1), (718, 2), (719, 1), (720, 840), (721, 1), (722, 5), (723, 2), (724, 5), (725, 2), (726, 13), (727, 1), (728, 40), (729, 504), (730, 4), (731, 1), (732, 18), (733, 1), (734, 2), (735, 6), (736, 195), (737, 2), (738, 10), (739, 1), (740, 15), (741, 5), (742, 4), (743, 1), (744, 54), (745, 1), (746, 2), (747, 2), (748, 11), (749, 1), (750, 39), (751, 1), (752, 42), (753, 1), (754, 4), (755, 2), (756, 189), (757, 1), (758, 2), (759, 2), (760, 39), (761, 1), (762, 6), (763, 1), (764, 4), (765, 2), (766, 2), (767, 1), (768, 1090235), (769, 1), (770, 12), (771, 1), (772, 5), (773, 1), (774, 16), (775, 4), (776, 15), (777, 5), (778, 2), (779, 1), (780, 53), (781, 1), (782, 4), (783, 5), (784, 172), (785, 1), (786, 4), (787, 1), (788, 5), (789, 1), (790, 4), (791, 2), (792, 137), (793, 1), (794, 2), (795, 1), (796, 4), (797, 1), (798, 24), (799, 1), (800, 1211), (801, 2), (802, 2), (803, 1), (804, 15), (805, 1), (806, 4), (807, 1), (808, 14), (809, 1), (810, 113), (811, 1), (812, 16), (813, 2), (814, 4), (815, 1), (816, 205), (817, 1), (818, 2), (819, 11), (820, 20), (821, 1), (822, 4), (823, 1), (824, 12), (825, 5), (826, 4), (827, 1), (828, 30), (829, 1), (830, 4), (831, 2), (832, 1630), (833, 2), (834, 6), (835, 1), (836, 9), (837, 13), (838, 2), (839, 1), (840, 186), (841, 2), (842, 2), (843, 1), (844, 4), (845, 2), (846, 10), (847, 2), (848, 51), (849, 2), (850, 10), (851, 1), (852, 10), (853, 1), (854, 4), (855, 5), (856, 12), (857, 1), (858, 12), (859, 1), (860, 11), (861, 2), (862, 2), (863, 1), (864, 4725), (865, 1), (866, 2), (867, 3), (868, 9), (869, 1), (870, 8), (871, 1), (872, 14), (873, 4), (874, 4), (875, 5), (876, 18), (877, 1), (878, 2), (879, 1), (880, 221), (881, 1), (882, 68), (883, 1), (884, 15), (885, 1), (886, 2), (887, 1), (888, 61), (889, 2), (890, 4), (891, 15), (892, 4), (893, 1), (894, 4), (895, 1), (896, 19349), (897, 2), (898, 2), (899, 1), (900, 150), (901, 1), (902, 4), (903, 7), (904, 15), (905, 2), (906, 6), (907, 1), (908, 4), (909, 2), (910, 8), (911, 1), (912, 222), (913, 1), (914, 2), (915, 4), (916, 5), (917, 1), (918, 30), (919, 1), (920, 39), (921, 2), (922, 2), (923, 1), (924, 34), (925, 2), (926, 2), (927, 4), (928, 235), (929, 1), (930, 18), (931, 2), (932, 5), (933, 1), (934, 2), (935, 2), (936, 222), (937, 1), (938, 4), (939, 2), (940, 11), (941, 1), (942, 6), (943, 1), (944, 42), (945, 13), (946, 4), (947, 1), (948, 15), (949, 1), (950, 10), (951, 1), (952, 42), (953, 1), (954, 10), (955, 2), (956, 4), (957, 1), (958, 2), (959, 1), (960, 11394), (961, 2), (962, 4), (963, 2), (964, 5), (965, 1), (966, 12), (967, 1), (968, 42), (969, 2), (970, 4), (971, 1), (972, 900), (973, 1), (974, 2), (975, 6), (976, 51), (977, 1), (978, 6), (979, 2), (980, 34), (981, 5), (982, 2), (983, 1), (984, 46), (985, 1), (986, 4), (987, 2), (988, 11), (989, 1), (990, 30), (991, 1), (992, 196), (993, 2), (994, 6), (995, 1), (996, 10), (997, 1), (998, 2), (999, 15), (1000, 199)] )


    def __is_excluded_TPP_small_group( self, ID ):

        order = ID[0]
        index = ID[1]
        excluded_orders = [ex_groups[0] for ex_groups in self.TPP_excluded_small_groups]
        for od in excluded_orders:
            if order == od:
                ex_groups = self.TPP_excluded_small_groups[excluded_orders.index( od )]
                if len( ex_groups ) == 1: return True
                else:
                    if index in ex_groups[1]: return True
                    else: return False

        return False


    def __is_valid_GAP_small_group( self, ID ):

        order = ID[0]
        index = ID[1]
        return order in self.GAP_small_groups_numeric_info_order_1_to_1000.keys() and \
               index in \
               range ( 1, self.GAP_small_groups_numeric_info_order_1_to_1000[order] + 1 )


    def is_valid_TPP_small_group( self, ID ):

        order = ID[0]
        index = ID[1]
        return not self.__is_excluded_TPP_small_group( ID ) and \
                   self.__is_valid_GAP_small_group( ID )


    def __get_HTML_table_column_indices( self, row, count ):

        i = j = 0

        while count > 0:
            i = row.find( '<td>', i + 1 )
            if i != -1: count -= 1
            else: return ()

        return (i + 4, row.find( '</td>', i ))


    def __get_HTML_table_column_value( self, row, col_name ):

        col_val = ''
        col_indices = ()

        if col_name in [ 'GAP_ID', 'order' ]:
            col_indices += self.__get_HTML_table_column_indices( row, 1 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].translate( None, '[]* ' )
                col_val = tuple( int( s ) for s in col_val.split( ',' ) )
            else: return 'ERROR'
            if col_name == 'order': col_val = col_val[0]
        elif col_name == 'char_degrees':
            col_indices += self.__get_HTML_table_column_indices( row, 2 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].replace( ' ', '' )
            else: return 'ERROR'
        elif col_name == 'D3':
            col_indices += self.__get_HTML_table_column_indices( row, 3 )
            if col_indices != ():
                col_val = int( row[col_indices[0]:col_indices[1]].replace( ' ', '' ) )
        elif col_name in [ 'MBS_STPP_param_type', 'Beta0' ]:
            col_indices += self.__get_HTML_table_column_indices( row, 9 )
            if col_indices != ():
                col_val = row[col_indices[0]:col_indices[1]].replace( ' ', '' )
                col_val = [int( s ) for s in col_val.split( ',' )]
                col_val.reverse()
                col_val = tuple( col_val )
                if col_name == 'Beta0':
                    col_val = col_val[0]*col_val[1]*col_val[2]
        else: return 'ERROR'

        return col_val


    def __get_HTML_table_row( self, HTML_data_file ):

        row_line = ''

        while True:
            line = HTML_data_file.readline().lower()
            if not line == '':
                if '<tr>' in line:
                    row_line += line.replace( ' ', '' )
                    while True:
                        line = HTML_data_file.readline().lower()
                        if not line == '':
                            row_line += line.strip().replace( ' ', '' )
                            if '</tr>' in line:
                                return row_line
                            else: continue
                        else: break
            else: return 'EOF'

        return row_line


    def get_small_groups_static_HTML_data( self, file_path ):

        HTML_data_file = open( file_path, 'r', 0 )
        SmallGroup = collections.namedtuple(
                  'SmallGroup', TPPTripleDataParser.small_groups_JSON_schema.keys()
                                      )
        row = ''
        i = 0
        print '\n'
        row = self.__get_HTML_table_row( HTML_data_file)

        while not row == 'EOF':
            ID = self.__get_HTML_table_column_value( row, 'GAP_ID' )
            ptype = self.__get_HTML_table_column_value( row, 'MBS_STPP_param_type' )
            group_rec = SmallGroup( GAP_ID=ID, order=ID[0], GAP_desc='',
            GAP_pickled_ID='', is_abelian=None, comm_length=None, is_cyclic=None,
            is_elem_abelian=None, is_simple=None, comp_length=None,
            is_nilpotent=None, nilpotency_class=None, is_solvable=None,
            derived_length=None, is_pgroup=None, generators=None,
            char_degrees=self.__get_HTML_table_column_value( row, 'char_degrees' ),
            D3=self.__get_HTML_table_column_value( row, 'D3' ),
            MBS_STPP_param_type=ptype, Beta0=ptype[0]*ptype[1]*ptype[2] )
            self.small_groups.update( {ID:group_rec} )
            i += 1
            row = self.__get_HTML_table_row( HTML_data_file )

        HTML_data_file.close()
        print 'Ordered dictionary of {} named tuples of small groups created.  File {} closed.'.format( len( self.small_groups ), HTML_data_file.name )


    def write_small_groups_JSON_file( self, file_dir, file_name, indent_num ):

        with io.open( file_dir + file_name, 'w', encoding='utf-8' ) as file:
            file.write( unicode( '[\n' ) )
            for count, small_group in enumerate( self.small_groups.values() ):
                if count:  file.write( unicode( ',\n' ) )
                JSON_obj = json.dumps( small_group._asdict(), \
                                       indent=indent_num, \
                                       ensure_ascii=False )
                file.write( unicode( JSON_obj ) )
            file.write( unicode( '\n]' ) )

        print '{} small group JSON objects successfully written to the file {}.'.\
              format( len( self.small_groups ), file.name )


    def read_small_groups_JSON_file( self, file_path, source ):

        sm_groups = collections.OrderedDict()
        decoder = json.JSONDecoder()

        with io.open( file_path, 'r', encoding='utf-8' ) as file:
            for line in file:
                if '{' in line and '}' in line:
                    sm_group = decoder.raw_decode( line )[0]
                    ID = tuple( sm_group['GAP_ID'] )
                    sm_group['GAP_ID'] = ID
                    if source in [ 'static HTML', 'JSON' ]:
                        sm_group['MBS_STPP_param_type'] = \
                          tuple( sm_group['MBS_STPP_param_type'] )
                        sm_group['index_LAN_subgroup'] = None
                        sm_group['index_LCN_subgroup'] = None
                        sm_group['index_LEAN_subgroup'] = None
                    elif source == 'GAP':
                        sm_group['order'] = ID[0]
                        sm_group['D3'] = None
                        sm_group['MBS_STPP_param_type'] = None
                        sm_group['Beta0'] = None
                    sm_group = collections.namedtuple( 'SmallGroup', \
                               TPPTripleDataParser.small_groups_JSON_schema.keys() )\
                               ( **sm_group )
                    sm_groups.update( {ID:sm_group} )

        print 'Ordered dictionary of {} named tuples of small groups loaded from JSON file {}.'.format( len( sm_groups ), file.name )
        return sm_groups


    def update_small_groups( self, groups_updated_info ):

        count = 0

        for ID in self.small_groups.keys():
            if ID in groups_updated_info.keys():
                small_group = self.small_groups[ID]._asdict()
                update_group = groups_updated_info[ID]._asdict()
                for key in update_group.keys():
                    if not key in [ 'GAP_ID', 'Beta0', 'MBS_STPP_param_type' ]:
                        small_group[key] = update_group[key]
                small_group = collections.namedtuple( 'SmallGroup', \
                           TPPTripleDataParser.small_groups_JSON_schema.keys() )\
                           ( **small_group )
                self.small_groups[ID] = small_group
                count += 1

        print 'Updated {} small groups in parser.'.format( count )


    def get_small_groups( self, asdict ):

        if asdict: return self.small_groups._asdict()
        else: return self.small_groups


    def __init__( self ):

        print 'Creating a new TPPTripleDataParser instance ...'
        self.small_groups = collections.OrderedDict()
