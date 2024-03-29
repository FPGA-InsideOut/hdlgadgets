import curses
from lib.common.gadgettop_class import gadgettop
from cocotb.types import Bit, Logic, LogicArray
from lib.common.helper_class import helper

class gadget_control_join(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'up_valid_a':[None], 'up_data_a':[None,None,None,None,None,None], 'up_valid_b':[None], 'up_data_b':[None,None,None,None,None,None], 'down_ready':[None], 'rst':[None]}
                self.logicstate_post = {'up_valid_a':[None], 'up_data_a':[None,None,None,None,None,None], 'up_valid_b':[None], 'up_data_b':[None,None,None,None,None,None],'down_ready':[None], 'rst':[None]}

                #Control state
                self.controlstate_pre = {'up_valid_a':[None], 'up_data_a':[None,None,None,None,None,None], 'up_valid_b':[None], 'up_data_b':[None,None,None,None,None,None], 'down_ready':[None], 'rst':[None]}
                self.controlstate_post = {'up_valid_a':['0'], 'up_data_a':['0','0','0','0','0','0'], 'up_valid_b':['0'], 'up_data_b':['0','0','0','0','0','0'], 'down_ready':['0'], 'rst':['0']}

        def __del__(self):
                super().__del__()

        def setup_2d_model (self, wctx):
                self._wctx = wctx
                self._wctx.erase()
                self._wctx.bkgd(' ', curses.color_pair(1))
                self._wctx.refresh()

        def process_input_stimulus (self, hdlpath, key):

                helper.dictcopy(self.controlstate_post, self.controlstate_pre)

                if (key == 122):                                                                                         #z-sym pressed
                     self.controlstate_post['up_data_a'][0] = '0' if (self.controlstate_pre['up_data_a'][0] == '1') else '1'
                if (key == 120):                                                                                         #x-sym pressed
                     self.controlstate_post['up_data_a'][1] = '0' if (self.controlstate_pre['up_data_a'][1] == '1') else '1'
                if (key == 99):                                                                                          #c-sym pressed
                     self.controlstate_post['up_data_a'][2] = '0' if (self.controlstate_pre['up_data_a'][2] == '1') else '1'
                if (key == 118):                                                                                         #v-sym pressed
                     self.controlstate_post['up_data_a'][3] = '0' if (self.controlstate_pre['up_data_a'][3] == '1') else '1'
                if (key == 98):                                                                                          #b-sym pressed
                     self.controlstate_post['up_data_a'][4] = '0' if (self.controlstate_pre['up_data_a'][4] == '1') else '1'
                if (key == 110):                                                                                         #n-sym pressed
                     self.controlstate_post['up_data_a'][5] = '0' if (self.controlstate_pre['up_data_a'][5] == '1') else '1'
                if (key == 97):                                                                                          #a-sym pressed
                     self.controlstate_post['up_valid_a'][0] = '0' if (self.controlstate_pre['up_valid_a'][0] == '1') else '1'

                if (key == 90):                                                                                          #Z-sym pressed
                     self.controlstate_post['up_data_b'][0] = '0' if (self.controlstate_pre['up_data_b'][0] == '1') else '1'
                if (key == 88):                                                                                          #X-sym pressed
                     self.controlstate_post['up_data_b'][1] = '0' if (self.controlstate_pre['up_data_b'][1] == '1') else '1'
                if (key == 67):                                                                                          #C-sym pressed
                     self.controlstate_post['up_data_b'][2] = '0' if (self.controlstate_pre['up_data_b'][2] == '1') else '1'
                if (key == 86):                                                                                          #V-sym pressed
                     self.controlstate_post['up_data_b'][3] = '0' if (self.controlstate_pre['up_data_b'][3] == '1') else '1'
                if (key == 66):                                                                                          #B-sym pressed
                     self.controlstate_post['up_data_b'][4] = '0' if (self.controlstate_pre['up_data_b'][4] == '1') else '1'
                if (key == 78):                                                                                          #N-sym pressed
                     self.controlstate_post['up_data_b'][5] = '0' if (self.controlstate_pre['up_data_b'][5] == '1') else '1'
                if (key == 65):                                                                                          #A-sym pressed
                     self.controlstate_post['up_valid_b'][0] = '0' if (self.controlstate_pre['up_valid_b'][0] == '1') else '1'

                if (key == 83 or key == 115):                                                                            #S/s-key pressed
                     self.controlstate_post['down_ready'][0] = '0' if (self.controlstate_pre['down_ready'][0] == '1') else '1'
                if (key == 82 or key == 114):                                                                            #R/r-key pressed
                     self.controlstate_post['rst'][0] = '0' if (self.controlstate_pre['rst'][0] == '1') else '1'

                hdlpath.up_valid_a.value = Bit(helper.show_dict_charlist_as_string(self.controlstate_post['up_valid_a']))
                hdlpath.up_valid_b.value = Bit(helper.show_dict_charlist_as_string(self.controlstate_post['up_valid_b']))
                hdlpath.up_data_a.value = LogicArray(helper.show_dict_charlist_as_string(self.controlstate_post['up_data_a']))
                hdlpath.up_data_b.value = LogicArray(helper.show_dict_charlist_as_string(self.controlstate_post['up_data_b']))
                hdlpath.down_ready.value = Bit(helper.show_dict_charlist_as_string(self.controlstate_post['down_ready']))
                hdlpath.rst.value = Bit(helper.show_dict_charlist_as_string(self.controlstate_post['rst']))

        def get_logic_state_data_from_simulator (self, hdlpath):
                #We need this method here as following drawing is based on logicstate so we need to take it from simulator
                #Copy post logic state into pre logic state
                helper.dictcopy(self.logicstate_post, self.logicstate_pre)

                helper.put_hdl_vector_to_dict(self.logicstate_post['rst'], hdlpath.rst.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_data_a'], hdlpath.up_data_a.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_valid_a'], hdlpath.up_valid_a.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_data_b'], hdlpath.up_data_b.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_valid_b'], hdlpath.up_valid_b.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_ready'], hdlpath.down_ready.value.binstr)


        def post_process_logic_state (self, phase):
               pass

        def write_to_log (self, strprefix, logfile):
                logfile.write(strprefix + ", logicstate_pre:" + str(self.logicstate_pre) + "\n")
                logfile.write(strprefix + ", logicstate_post:" + str(self.logicstate_post) + "\n")

        def drive_2d_model (self):
                ####BASE####
                ###########################0#####1#####2#####3#####4#####5#####6#####7####8#####9#####10#####11####12####13####14####15####16####17####18####19####20####21####22####23####24####25####26####27####28####29####30####31####32####33####34####35####36####37####38####39####40####41####42####43####44####45###
                self._wctx.addstr(0,0,  u'\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(1,0,  u'\u2551\u0020\u0072\u0065\u0073\u0065\u0074\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u0052\u002D\u006B\u0065\u0079\u0022\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(2,0,  u'\u2551\u0020\u0075\u0070\u005F\u0076\u0061\u006C\u0069\u0064\u005F\u0061\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u0061\u002D\u0073\u0079\u006D\u0022\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(3,0,  u'\u2551\u0020\u0075\u0070\u005F\u0064\u0061\u0074\u0061\u005F\u0061\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u007A\u002C\u0078\u002C\u0063\u002C\u0076\u002C\u0062\u002C\u006E\u002D\u0073\u0079\u006D\u0073\u0022\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(4,0,  u'\u2551\u0020\u0075\u0070\u005F\u0076\u0061\u006C\u0069\u0064\u005F\u0062\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u0041\u002D\u0073\u0079\u006D\u0022\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(5,0,  u'\u2551\u0020\u0075\u0070\u005F\u0064\u0061\u0074\u0061\u005F\u0062\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u005A\u002C\u0058\u002C\u0043\u002C\u0056\u002C\u0042\u002C\u004E\u002D\u0073\u0079\u006D\u0073\u0022\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(6,0,  u'\u2551\u0020\u0064\u006F\u0077\u006E\u005F\u0072\u0065\u0061\u0064\u0079\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u0053\u002D\u006B\u0065\u0079\u0022\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(7,0,  u'\u2551\u0020\u0043\u006C\u006F\u0063\u006B\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u0045\u004E\u0054\u0045\u0052\u002D\u006B\u0065\u0079\u0022\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(8,0,  u'\u2551\u0020\u0051\u0075\u0069\u0074\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u002D\u0020\u0022\u0045\u0053\u0043\u002D\u006B\u0065\u0079\u0022\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2551'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(9,0,  u'\u255A\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255D'.encode('utf-8'), curses.color_pair(1))
                ####RST####
                if (self.logicstate_post['rst'][0] == '1'):
                    self._wctx.addstr(1,15, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['rst'][0] == '0'):
                    self._wctx.addstr(1,15, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(1,15, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_VALID_A####
                if (self.logicstate_post['up_valid_a'][0] == '1'):
                    self._wctx.addstr(2,15, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_valid_a'][0] == '0'):
                    self._wctx.addstr(2,15, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(2,15, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_A[0]####
                if (self.logicstate_post['up_data_a'][0] == '1'):
                    self._wctx.addstr(3,15, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_a'][0] == '0'):
                    self._wctx.addstr(3,15, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(3,15, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_A[1]####
                if (self.logicstate_post['up_data_a'][1] == '1'):
                    self._wctx.addstr(3,16, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_a'][1] == '0'):
                    self._wctx.addstr(3,16, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(3,16, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_A[2]####
                if (self.logicstate_post['up_data_a'][2] == '1'):
                    self._wctx.addstr(3,17, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_a'][2] == '0'):
                    self._wctx.addstr(3,17, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(3,17, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_A[3]####
                if (self.logicstate_post['up_data_a'][3] == '1'):
                    self._wctx.addstr(3,18, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_a'][3] == '0'):
                    self._wctx.addstr(3,18, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(3,18, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_A[4]####
                if (self.logicstate_post['up_data_a'][4] == '1'):
                    self._wctx.addstr(3,19, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_a'][4] == '0'):
                    self._wctx.addstr(3,19, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(3,19, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_A[5]####
                if (self.logicstate_post['up_data_a'][5] == '1'):
                    self._wctx.addstr(3,20, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_a'][5] == '0'):
                    self._wctx.addstr(3,20, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(3,20, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_VALID_B####
                if (self.logicstate_post['up_valid_b'][0] == '1'):
                    self._wctx.addstr(4,15, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_valid_b'][0] == '0'):
                    self._wctx.addstr(4,15, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(4,15, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_B[0]####
                if (self.logicstate_post['up_data_b'][0] == '1'):
                    self._wctx.addstr(5,15, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_b'][0] == '0'):
                    self._wctx.addstr(5,15, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(5,15, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_B[1]####
                if (self.logicstate_post['up_data_b'][1] == '1'):
                    self._wctx.addstr(5,16, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_b'][1] == '0'):
                    self._wctx.addstr(5,16, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(5,16, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_B[2]####
                if (self.logicstate_post['up_data_b'][2] == '1'):
                    self._wctx.addstr(5,17, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_b'][2] == '0'):
                    self._wctx.addstr(5,17, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(5,17, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_B[3]####
                if (self.logicstate_post['up_data_b'][3] == '1'):
                    self._wctx.addstr(5,18, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_b'][3] == '0'):
                    self._wctx.addstr(5,18, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(5,18, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_B[4]####
                if (self.logicstate_post['up_data_b'][4] == '1'):
                    self._wctx.addstr(5,19, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_b'][4] == '0'):
                    self._wctx.addstr(5,19, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(5,19, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA_B[5]####
                if (self.logicstate_post['up_data_b'][5] == '1'):
                    self._wctx.addstr(5,20, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_data_b'][5] == '0'):
                    self._wctx.addstr(5,20, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(5,20, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####DOWN_READY####
                if (self.logicstate_post['down_ready'][0] == '1'):
                    self._wctx.addstr(6,15, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['down_ready'][0] == '0'):
                    self._wctx.addstr(6,15, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,15, u'\u00D7'.encode('utf-8'), curses.color_pair(1))

                self._wctx.refresh()

