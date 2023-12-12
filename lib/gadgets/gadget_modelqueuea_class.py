from lib.gadgets.gadget_modelqueuebase_class import gadget_modelqueuebase
from lib.common.helper_class import helper

class gadget_modelqueuea(gadget_modelqueuebase):

        def __init__(self):
                super().__init__()

        def __del__(self):
                super().__del__()

        def get_logic_state_data_from_simulator (self, hdlpath):
                #Copy post logic state into pre logic state
                helper.dictcopy(self.logicstate_post, self.logicstate_pre)

                helper.put_hdl_vector_to_dict(self.logicstate_post['queue0'], hdlpath.queue0_a.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['queue1'], hdlpath.queue1_a.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['queue2'], hdlpath.queue2_a.value.binstr)
                self.logicstate_post['qsize'][0] = hdlpath.qsize_a.value.integer
