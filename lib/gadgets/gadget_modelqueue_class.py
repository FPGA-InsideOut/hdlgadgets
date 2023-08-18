import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_modelqueue(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'queue0': [None,None,None,None,None,None], 'queue1': [None,None,None,None,None,None], 'queue2': [None,None,None,None,None,None], 'qsize':[None]}
                self.logicstate_post = {'queue0': [None,None,None,None,None,None], 'queue1': [None,None,None,None,None,None], 'queue2': [None,None,None,None,None,None], 'qsize':[None]}

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

                helper.put_hdl_vector_to_dict(self.logicstate_post['queue0'], hdlpath.queue0.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['queue1'], hdlpath.queue1.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['queue2'], hdlpath.queue2.value.binstr)
                self.logicstate_post['qsize'][0] = hdlpath.qsize.value.integer

        def post_process_logic_state (self, phase):
                #Nothing to do here in 2D version
                pass

        def write_to_log (self, strprefix, logfile):
                logfile.write(strprefix + ", logicstate_pre:" + str(self.logicstate_pre) + "\n")
                logfile.write(strprefix + ", logicstate_post:" + str(self.logicstate_post) + "\n")

        def drive_2d_model (self):
                ####BASE####
                ###########################0#####1#####2#####3#####4#####5#####6#####7#####8#####9#####10####11####12####13####14####15####16####17####180###19####20####21####22####23####24####25####26####27####28####29####30####31####32####33####34####35#####
                self._wctx.addstr(0,0,  u'\u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(1,0,  u'\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(2,0,  u'\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(3,0,  u'\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(4,0,  u'\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0071\u0075\u0065\u0075\u0065\u005F\u0073\u0069\u007A\u0065\u003A\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503'.encode('utf-8'), curses.color_pair(1))
                self._wctx.addstr(5,0,  u'\u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251B'.encode('utf-8'), curses.color_pair(1))
                ####QUEUE_0####
                if (self.logicstate_post['qsize'][0] > 0):
                    self._wctx.addstr(1,23, u'\u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(2,23, u'\u2503\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2503'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(3,23, u'\u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u251B'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(2,25, helper.show_dict_charlist_as_string(self.logicstate_post['queue0']), curses.color_pair(1))
                else:
                    self._wctx.addstr(2,25, helper.show_dict_charlist_as_string(self.logicstate_post['queue0']), curses.color_pair(1))
                ####QUEUE_1####
                if (self.logicstate_post['qsize'][0] > 1):
                    self._wctx.addstr(1,13, u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(2,13, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(3,13, u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(2,15, helper.show_dict_charlist_as_string(self.logicstate_post['queue1']), curses.color_pair(1))
                else:
                    pass
                ####QUEUE_2####
                if (self.logicstate_post['qsize'][0] > 2):
                    self._wctx.addstr(1,3, u'\u250C\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2510'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(2,3, u'\u2502\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u2502'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(3,3, u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(2,5, helper.show_dict_charlist_as_string(self.logicstate_post['queue2']), curses.color_pair(1))
                else:
                    pass
                ####MORE_SHADOW####
                if (self.logicstate_post['qsize'][0] > 4):
                    self._wctx.addstr(2,2, u'\u2590'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(3,2, u'\u2590'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(4,2, u'\u259D\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580\u2580'.encode('utf-8'), curses.color_pair(1))
                elif (self.logicstate_post['qsize'][0] == 4):
                    self._wctx.addstr(2,2, u'\u250C'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(3,2, u'\u2502'.encode('utf-8'), curses.color_pair(1))
                    self._wctx.addstr(4,2, u'\u2514\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2518'.encode('utf-8'), curses.color_pair(1))
                else:
                    pass
                ####PRINT QUEUE_SIZE####
                self._wctx.addstr(4,28, str(self.logicstate_post['qsize'][0]), curses.color_pair(1))

                self._wctx.refresh()

