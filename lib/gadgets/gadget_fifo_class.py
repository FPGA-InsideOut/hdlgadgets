import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_fifo(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'rst':[None], 'up_data':[None,None,None,None,None,None], 'up_valid':[None], 'up_ready':[None], 'full':[None], 'push':[None], 'down_data':[None,None,None,None,None,None], 'down_valid':[None], 'empty':[None], 'down_ready':[None], 'pop':[None], 'wr_ptr':[None,None,None], 'rd_ptr':[None,None,None], 'fifo_line0':[None,None,None,None,None,None], 'fifo_line1':[None,None,None,None,None,None], 'fifo_line2':[None,None,None,None,None,None], 'fifo_line3':[None,None,None,None,None,None]}
                self.logicstate_post = {'rst':[None], 'up_data':[None,None,None,None,None,None], 'up_valid':[None], 'up_ready':[None], 'full':[None], 'push':[None], 'down_data':[None,None,None,None,None,None], 'down_valid':[None], 'empty':[None], 'down_ready':[None], 'pop':[None], 'wr_ptr':[None,None,None], 'rd_ptr':[None,None,None], 'fifo_line0':[None,None,None,None,None,None], 'fifo_line1':[None,None,None,None,None,None], 'fifo_line2':[None,None,None,None,None,None], 'fifo_line3':[None,None,None,None,None,None]}

        def __del__(self):
                super().__del__()

        def setup_2d_model (self, wctx):
                self._wctx = wctx
                self._wctx.erase()
                self._wctx.bkgd(' ', curses.color_pair(1))
                self._wctx.refresh()

        def process_input_stimulus (self, hdlpath, key):
                pass

        def get_logic_state_data_from_simulator (self, hdlpath):
                #Copy post logic state into pre logic state
                helper.dictcopy(self.logicstate_post, self.logicstate_pre)

                helper.put_hdl_vector_to_dict(self.logicstate_post['rst'], hdlpath.rst.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_data'], hdlpath.up_data.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_valid'], hdlpath.up_valid.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_ready'], hdlpath.up_ready.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['full'], hdlpath.full.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['push'], hdlpath.push.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_data'], hdlpath.down_data.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_valid'], hdlpath.down_valid.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['empty'], hdlpath.empty.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_ready'], hdlpath.down_ready.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['pop'], hdlpath.pop.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['wr_ptr'], hdlpath.fullwidth_wr_ptr.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['rd_ptr'], hdlpath.fullwidth_rd_ptr.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['fifo_line0'], hdlpath.ram[0].value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['fifo_line1'], hdlpath.ram[1].value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['fifo_line2'], hdlpath.ram[2].value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['fifo_line3'], hdlpath.ram[3].value.binstr)


        def post_process_logic_state (self, phase):
                pass


        def write_to_log (self, strprefix, logfile):
                logfile.write(strprefix + ", logicstate_pre:" + str(self.logicstate_pre) + "\n")
                logfile.write(strprefix + ", logicstate_post:" + str(self.logicstate_post) + "\n")

        def drive_2d_model (self):
                ####BASE####
                ###########################0#####1#####2#####3#####4#####5#####6#####7####8#####9#####10#####11####12####13####14####15####16####17####18####19####20####21####22####23####24####25####26####27####28####29####30####31####32####33####34####35####36####37####38####39####40####41####42####43####44####45###
                self._wctx.addstr(0,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(1,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(2,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(3,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(4,0,  u'\u2501\u2501\u2501\u2501\u0020\u0020\u0020\u0020\u0020\u0020\u2501\u2501\u2501\u257E\u0020\u0020\u2503\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2503\u0020\u0020\u0020\u257C\u2501\u2501\u0020\u0020\u0020\u0020\u0020\u0020\u2501\u2501\u2501\u2771'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(5,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(6,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(7,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(8,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2521\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2529\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(9,0,  u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(10,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(11,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(12,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                ####UP_VALID####
                if (self.logicstate_post['up_valid'][0] == '1'):
                    self._wctx.addstr(10,0, u'\u2500\u2500\u2500\u2500\u0076\u0061\u006C\u0069\u0064\u2500\u2500\u2500\u2500\u2500\u2500\u276F'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_valid'][0] == '0'):
                    self._wctx.addstr(10,0, u'\uFF65\uFF65\uFF65\uFF65\u0021\u0076\u0061\u006C\u0069\u0064\uFF65\uFF65\uFF65\uFF65\uFF65\u276D'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(10,0, u'\u00D7\u00D7\u00D7\u00D7\u003F\u0076\u0061\u006C\u0069\u0064\u00D7\u00D7\u00D7\u00D7\u00D7\u276D'.encode('utf-8'), curses.color_pair(1))
                ####UP_READY####
                if (self.logicstate_post['up_ready'][0] == '1'):
                    self._wctx.addstr(11,0, u'\u276E\u2500\u2500\u2500\u0072\u0065\u0061\u0064\u0079\u2500\u2500\u2500\u2500\u2500\u2500\u2500'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['up_ready'][0] == '0'):
                    self._wctx.addstr(11,0, u'\u276C\uFF65\uFF65\uFF65\u0021\u0072\u0065\u0061\u0064\u0079\uFF65\uFF65\uFF65\uFF65\uFF65\uFF65'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(11,0, u'\u276C\u00D7\u00D7\u00D7\u003F\u0072\u0065\u0061\u0064\u0079\u00D7\u00D7\u00D7\u00D7\u00D7\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####UP_DATA####
                self._wctx.addstr(4,4, helper.show_dict_charlist_as_string(self.logicstate_post['up_data']), curses.color_pair(1))
                ####FULL####
                if (self.logicstate_post['full'][0] == '1'):
                    self._wctx.addstr(11,17, u'\u0066\u0075\u006C\u006C'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['full'][0] == '0'):
                    self._wctx.addstr(11,17, u'\u0021\u0066\u0075\u006C\u006C'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(11,17, u'\u003F\u0066\u0075\u006C\u006C'.encode('utf-8'), curses.color_pair(1))
                ####PUSH####
                if (self.logicstate_post['push'][0] == '1'):
                    self._wctx.addstr(10,17, u'\u0070\u0075\u0073\u0068'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['push'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(10,17, u'\u003F\u0070\u0075\u0073\u0068'.encode('utf-8'), curses.color_pair(1))
                ####MSB_WR_PTR####
                if (self.logicstate_post['wr_ptr'][0] == '1'):
                    self._wctx.addstr(9,17, u'\u0031'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['wr_ptr'][0] == '0'):
                    self._wctx.addstr(9,17, u'\u0030'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,17, u'\u0078'.encode('utf-8'), curses.color_pair(1))
                ####WR_PTR####
                if (self.logicstate_post['wr_ptr'][1] == '0' and self.logicstate_post['wr_ptr'][2] == '0'):
                    self._wctx.addstr(9,18, u'\u0030\u0030'.encode('utf-8'), curses.color_pair(1))          #wr_counter
                    self._wctx.addstr(4,13, u'\u256F'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(3,13, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(2,13, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(1,13, u'\u256D\u2500\u2771'.encode('utf-8'), curses.color_pair(1))    #input_arrow
                elif (self.logicstate_post['wr_ptr'][1] == '0' and self.logicstate_post['wr_ptr'][2] == '1'):
                    self._wctx.addstr(9,18, u'\u0030\u0031'.encode('utf-8'), curses.color_pair(1))          #wr_counter
                    self._wctx.addstr(4,13, u'\u256F'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(3,13, u'\u256D\u2500\u2771'.encode('utf-8'), curses.color_pair(1))    #input_arrow
                elif (self.logicstate_post['wr_ptr'][1] == '1' and self.logicstate_post['wr_ptr'][2] == '0'):
                    self._wctx.addstr(9,18, u'\u0031\u0030'.encode('utf-8'), curses.color_pair(1))          #wr_counter
                    self._wctx.addstr(4,13, u'\u256E'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(5,13, u'\u2570\u2500\u2771'.encode('utf-8'), curses.color_pair(1))    #input_arrow
                elif (self.logicstate_post['wr_ptr'][1] == '1' and self.logicstate_post['wr_ptr'][2] == '1'):
                    self._wctx.addstr(9,18, u'\u0031\u0031'.encode('utf-8'), curses.color_pair(1))          #wr_counter
                    self._wctx.addstr(4,13, u'\u256E'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(5,13, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(6,13, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                    self._wctx.addstr(7,13, u'\u2570\u2500\u2771'.encode('utf-8'), curses.color_pair(1))    #input_arrow
                else:
                    self._wctx.addstr(9,18, u'\u0078\u0078'.encode('utf-8'), curses.color_pair(1))          #wr_counter
                    self._wctx.addstr(4,13, u'\u003F'.encode('utf-8'), curses.color_pair(1))                #input_arrow
                ####FIFO_LINE0####
                self._wctx.addstr(1,19, helper.show_dict_charlist_as_string(self.logicstate_post['fifo_line0']), curses.color_pair(1))
                ####FIFO_LINE1####
                self._wctx.addstr(3,19, helper.show_dict_charlist_as_string(self.logicstate_post['fifo_line1']), curses.color_pair(1))
                ####FIFO_LINE2####
                self._wctx.addstr(5,19, helper.show_dict_charlist_as_string(self.logicstate_post['fifo_line2']), curses.color_pair(1))
                ####FIFO_LINE3####
                self._wctx.addstr(7,19, helper.show_dict_charlist_as_string(self.logicstate_post['fifo_line3']), curses.color_pair(1))
                ####DOWN_VALID####
                if (self.logicstate_post['down_valid'][0] == '1'):
                    self._wctx.addstr(10,30, u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u0076\u0061\u006C\u0069\u0064\u2500\u2500\u2500\u276F'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['down_valid'][0] == '0'):
                    self._wctx.addstr(10,30, u'\uFF65\uFF65\uFF65\uFF65\uFF65\uFF65\u0021\u0076\u0061\u006C\u0069\u0064\uFF65\uFF65\uFF65\u276D'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(10,30, u'\u00D7\u00D7\u00D7\u00D7\u00D7\u00D7\u003F\u0076\u0061\u006C\u0069\u0064\u00D7\u00D7\u00D7\u276D'.encode('utf-8'), curses.color_pair(1))
                ####DOWN_READY####
                if (self.logicstate_post['down_ready'][0] == '1'):
                    self._wctx.addstr(11,30, u'\u276E\u2500\u2500\u2500\u2500\u2500\u2500\u0072\u0065\u0061\u0064\u0079\u2500\u2500\u2500\u2500'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['down_ready'][0] == '0'):
                    self._wctx.addstr(11,30, u'\u276C\uFF65\uFF65\uFF65\uFF65\uFF65\u0021\u0072\u0065\u0061\u0064\u0079\uFF65\uFF65\uFF65\uFF65'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(11,30, u'\u276C\u00D7\u00D7\u00D7\u00D7\u00D7\u003F\u0072\u0065\u0061\u0064\u0079\u00D7\u00D7\u00D7\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####POP####
                if (self.logicstate_post['pop'][0] == '1'):
                    self._wctx.addstr(11,26, u'\u0070\u006F\u0070'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['pop'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(11,25, u'\u003F\u0070\u006F\u0070'.encode('utf-8'), curses.color_pair(1))
                ####DOWN_DATA####
                self._wctx.addstr(4,36, helper.show_dict_charlist_as_string(self.logicstate_post['down_data']), curses.color_pair(1))
                ####EMPTY####
                if (self.logicstate_post['empty'][0] == '1'):
                    self._wctx.addstr(10,24, u'\u0065\u006D\u0070\u0074\u0079'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['empty'][0] == '0'):
                    self._wctx.addstr(10,23, u'\u0021\u0065\u006D\u0070\u0074\u0079'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(10,23, u'\u003F\u0065\u006D\u0070\u0074\u0079'.encode('utf-8'), curses.color_pair(1))
                ####MSB_RD_PTR####
                if (self.logicstate_post['rd_ptr'][0] == '1'):
                    self._wctx.addstr(9,26, u'\u0031'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['rd_ptr'][0] == '0'):
                    self._wctx.addstr(9,26, u'\u0030'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,26, u'\u0078'.encode('utf-8'), curses.color_pair(1))
                ####RD_PTR####
                if (self.logicstate_post['rd_ptr'][1] == '0' and self.logicstate_post['rd_ptr'][2] == '0'):
                    self._wctx.addstr(9,27, u'\u0030\u0030'.encode('utf-8'), curses.color_pair(1))          #rd_counter
                    self._wctx.addstr(1,30, u'\u2500\u2500\u256E'.encode('utf-8'), curses.color_pair(1))    #output_arrow
                    self._wctx.addstr(2,32, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                    self._wctx.addstr(3,32, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                    self._wctx.addstr(4,32, u'\u2570'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                elif (self.logicstate_post['rd_ptr'][1] == '0' and self.logicstate_post['rd_ptr'][2] == '1'):
                    self._wctx.addstr(9,27, u'\u0030\u0031'.encode('utf-8'), curses.color_pair(1))          #rd_counter
                    self._wctx.addstr(3,30, u'\u2500\u2500\u256E'.encode('utf-8'), curses.color_pair(1))    #output_arrow
                    self._wctx.addstr(4,32, u'\u2570'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                elif (self.logicstate_post['rd_ptr'][1] == '1' and self.logicstate_post['rd_ptr'][2] == '0'):
                    self._wctx.addstr(9,27, u'\u0031\u0030'.encode('utf-8'), curses.color_pair(1))          #rd_counter
                    self._wctx.addstr(5,30, u'\u2500\u2500\u256F'.encode('utf-8'), curses.color_pair(1))    #output_arrow
                    self._wctx.addstr(4,32, u'\u256D'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                elif (self.logicstate_post['rd_ptr'][1] == '1' and self.logicstate_post['rd_ptr'][2] == '1'):
                    self._wctx.addstr(9,27, u'\u0031\u0031'.encode('utf-8'), curses.color_pair(1))          #rd_counter
                    self._wctx.addstr(7,30, u'\u2500\u2500\u256F'.encode('utf-8'), curses.color_pair(1))    #output_arrow
                    self._wctx.addstr(6,32, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                    self._wctx.addstr(5,32, u'\u2502'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                    self._wctx.addstr(4,32, u'\u256D'.encode('utf-8'), curses.color_pair(1))                #output_arrow
                else:
                    self._wctx.addstr(9,27, u'\u0078\u0078'.encode('utf-8'), curses.color_pair(1))          #rd_counter
                    self._wctx.addstr(4,32, u'\u003F'.encode('utf-8'), curses.color_pair(1))                #output_arrow

                self._wctx.refresh()
