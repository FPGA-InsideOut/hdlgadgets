import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_custlogic(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'debug':[None,None,None,None,None,None,None,None,None,None]}
                self.logicstate_post = {'debug':[None,None,None,None,None,None,None,None,None,None]}

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

                helper.put_hdl_vector_to_dict(self.logicstate_post['debug'], hdlpath.debug.value.binstr)

        def post_process_logic_state (self, phase):
                pass


        def write_to_log (self, strprefix, logfile):
                logfile.write(strprefix + ", logicstate_pre:" + str(self.logicstate_pre) + "\n")
                logfile.write(strprefix + ", logicstate_post:" + str(self.logicstate_post) + "\n")

        def drive_2d_model (self):
                ####BASE####
                ##########################0#####1#####2#####3#####4#####5#####6#####7#####8#####9#####
                self._wctx.addstr(0,0, u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(1,0, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(2,0, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(3,0, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(4,0, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(5,0, u'\u2502\u0020\u0064\u0065\u0062\u0075\u0067\u003A\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(6,0, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(7,0, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(8,0, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(9,0, u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[0]####
                if (self.logicstate_post['debug'][0] == '1'):
                    self._wctx.addstr(6,1, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][0] == '0'):
                    self._wctx.addstr(6,1, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,1, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[1]####
                if (self.logicstate_post['debug'][1] == '1'):
                    self._wctx.addstr(6,2, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][1] == '0'):
                    self._wctx.addstr(6,2, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,2, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[2]####
                if (self.logicstate_post['debug'][2] == '1'):
                    self._wctx.addstr(6,3, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][2] == '0'):
                    self._wctx.addstr(6,3, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,3, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[3]####
                if (self.logicstate_post['debug'][3] == '1'):
                    self._wctx.addstr(6,4, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][3] == '0'):
                    self._wctx.addstr(6,4, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,4, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[4]####
                if (self.logicstate_post['debug'][4] == '1'):
                    self._wctx.addstr(6,5, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][4] == '0'):
                    self._wctx.addstr(6,5, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,5, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[5]####
                if (self.logicstate_post['debug'][5] == '1'):
                    self._wctx.addstr(6,6, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][5] == '0'):
                    self._wctx.addstr(6,6, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,6, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[6]####
                if (self.logicstate_post['debug'][6] == '1'):
                    self._wctx.addstr(6,7, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][6] == '0'):
                    self._wctx.addstr(6,7, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,7, u'\u25CC'.encode('utf-8'), curses.color_pair(1))
                ####DEBUG[7]####
                if (self.logicstate_post['debug'][7] == '1'):
                    self._wctx.addstr(6,8, u'\u25C9'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['debug'][7] == '0'):
                    self._wctx.addstr(6,8, u'\u25CB'.encode('utf-8'), curses.color_pair(1))
                else:
                    self._wctx.addstr(6,8, u'\u25CC'.encode('utf-8'), curses.color_pair(1))

                self._wctx.refresh()
