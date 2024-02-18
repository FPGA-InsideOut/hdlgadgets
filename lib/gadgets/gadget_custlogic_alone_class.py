import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_custlogic_alone(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'rst':[None], 'up_data':[None,None,None,None,None,None], 'up_valid':[None], 'up_ready':[None], 'down_data':[None,None,None,None,None,None], 'down_valid':[None], 'down_ready':[None], 'debug':[None,None,None,None,None,None,None,None,None,None]}
                self.logicstate_post = {'rst':[None], 'up_data':[None,None,None,None,None,None], 'up_valid':[None], 'up_ready':[None], 'down_data':[None,None,None,None,None,None], 'down_valid':[None], 'down_ready':[None], 'debug':[None,None,None,None,None,None,None,None,None,None]}

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
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_data'], hdlpath.down_data.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_valid'], hdlpath.down_valid.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_ready'], hdlpath.down_ready.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['debug'], hdlpath.debug.value.binstr)

        def post_process_logic_state (self, phase):
                pass


        def write_to_log (self, strprefix, logfile):
                logfile.write(strprefix + ", logicstate_pre:" + str(self.logicstate_pre) + "\n")
                logfile.write(strprefix + ", logicstate_post:" + str(self.logicstate_post) + "\n")

        def drive_2d_model (self):
                ####BASE####
                ##########################0#####1#####2#####3#####4#####5#####6#####7#####8#####9#####10####11####12####13####14####15####16####17####18####19####20####21####22####23####24####25####26####27####28####29####30####31####32####33####34####35####36####37####38####39####40####41###
                self._wctx.addstr(0,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(1,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(2,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(3,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(4,0, u'\u2501\u2501\u2501\u2501\u0020\u0020\u0020\u0020\u0020\u0020\u2501\u2501\u2501\u2501\u2501\u2771\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u2501\u2501\u2501\u2501\u2501\u2501\u0020\u0020\u0020\u0020\u0020\u0020\u2501\u2501\u2501\u2771'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(5,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(6,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(7,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(8,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0064\u0065\u0062\u0075\u0067\u003A\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(9,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(10,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(11,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(12,0, u'\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020'.encode('utf-8'), curses.color_pair(1))

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
                ####DOWN_VALID####
                if (self.logicstate_post['down_valid'][0] == '1'):
                    self._wctx.addstr(10,26, u'\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u0076\u0061\u006C\u0069\u0064\u2500\u2500\u2500\u276F'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['down_valid'][0] == '0'):
                    self._wctx.addstr(10,26, u'\uFF65\uFF65\uFF65\uFF65\uFF65\uFF65\u0021\u0076\u0061\u006C\u0069\u0064\uFF65\uFF65\uFF65\u276D'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(10,26, u'\u00D7\u00D7\u00D7\u00D7\u00D7\u00D7\u003F\u0076\u0061\u006C\u0069\u0064\u00D7\u00D7\u00D7\u276D'.encode('utf-8'), curses.color_pair(1))
                ####DOWN_READY####
                if (self.logicstate_post['down_ready'][0] == '1'):
                    self._wctx.addstr(11,26, u'\u276E\u2500\u2500\u2500\u2500\u2500\u2500\u0072\u0065\u0061\u0064\u0079\u2500\u2500\u2500\u2500'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['down_ready'][0] == '0'):
                    self._wctx.addstr(11,26, u'\u276C\uFF65\uFF65\uFF65\uFF65\uFF65\u0021\u0072\u0065\u0061\u0064\u0079\uFF65\uFF65\uFF65\uFF65'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(11,26, u'\u276C\u00D7\u00D7\u00D7\u00D7\u00D7\u003F\u0072\u0065\u0061\u0064\u0079\u00D7\u00D7\u00D7\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####DOWN_DATA####
                self._wctx.addstr(4,32, helper.show_dict_charlist_as_string(self.logicstate_post['down_data']), curses.color_pair(1))
                ####DEBUG[0]####
                if (self.logicstate_post['debug'][0] == '1'):
                    self._wctx.addstr(9,17, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][0] == '0'):
                    self._wctx.addstr(9,17, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,17, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[1]####
                if (self.logicstate_post['debug'][1] == '1'):
                    self._wctx.addstr(9,18, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][1] == '0'):
                    self._wctx.addstr(9,18, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,18, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[2]####
                if (self.logicstate_post['debug'][2] == '1'):
                    self._wctx.addstr(9,19, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][2] == '0'):
                    self._wctx.addstr(9,19, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,19, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[3]####
                if (self.logicstate_post['debug'][3] == '1'):
                    self._wctx.addstr(9,20, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][3] == '0'):
                    self._wctx.addstr(9,20, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,20, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[4]####
                if (self.logicstate_post['debug'][4] == '1'):
                    self._wctx.addstr(9,21, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][4] == '0'):
                    self._wctx.addstr(9,21, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,21, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[5]####
                if (self.logicstate_post['debug'][5] == '1'):
                    self._wctx.addstr(9,22, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][5] == '0'):
                    self._wctx.addstr(9,22, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,22, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[6]####
                if (self.logicstate_post['debug'][6] == '1'):
                    self._wctx.addstr(9,23, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][6] == '0'):
                    self._wctx.addstr(9,23, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,23, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[7]####
                if (self.logicstate_post['debug'][7] == '1'):
                    self._wctx.addstr(9,24, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][7] == '0'):
                    self._wctx.addstr(9,24, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(9,24, u'\u25CC'.encode('utf-8'), curses.color_pair(1))

                self._wctx.refresh()
