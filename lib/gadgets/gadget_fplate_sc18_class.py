import curses
from lib.common.gadgettop_class import gadgettop

class gadget_fplate_sc18(gadgettop):

        def __init__(self):
                super().__init__()

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
                pass

        def post_process_logic_state (self, phase):
                pass

        def write_to_log (self, strprefix, logfile):
                pass

        def drive_2d_model (self):
                self._wctx.addstr(1,23, u'\u0046\u0049\u0046\u004F\u005F\u0052\u004C\u0042\u004B'.encode('utf-8'), curses.color_pair(3))
                self._wctx.addstr(1,64, u'\u0020\u004D\u004F\u0044\u0045\u004C\u005F\u0051\u0055\u0045\u0055\u0045\u005F\u0041\u0020'.encode('utf-8'), curses.color_pair(3))
                self._wctx.addstr(9,64, u'\u0020\u004D\u004F\u0044\u0045\u004C\u005F\u0051\u0055\u0045\u0055\u0045\u005F\u0042\u0020'.encode('utf-8'), curses.color_pair(3))
                self._wctx.addstr(19,65, u'\u0052\u0054\u004C\u005F\u004D\u004F\u0044\u0045\u004C\u005F\u0045\u0052\u0052'.encode('utf-8'), curses.color_pair(3))
                self._wctx.addstr(25,22, u'\u0020\u0020\u0043\u004F\u004E\u0054\u0052\u004F\u004C\u0020\u0020'.encode('utf-8'), curses.color_pair(3))

                self._wctx.refresh()
