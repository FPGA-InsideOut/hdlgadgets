import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_fifobase(gadgettop):

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

