import curses
from lib.common.scenariotop_class import scenariotop
from lib.gadgets.gadget_credbasedfc44_class import gadget_credbasedfc44
from lib.gadgets.gadget_credbasedfc4Xtr_class import gadget_credbasedfc4Xtr
from lib.gadgets.gadget_credbasedfcX4tr_class import gadget_credbasedfcX4tr
from lib.gadgets.gadget_fifocreditreturn_class import gadget_fifocreditreturn
from lib.gadgets.gadget_fifotr_class import gadget_fifotr
from lib.gadgets.gadget_modelqueue_class import gadget_modelqueue
from lib.gadgets.gadget_check_class import gadget_check
from lib.gadgets.gadget_control_class import gadget_control
from lib.gadgets.gadget_fplate_sc16_class import gadget_fplate_sc16

class scenario16(scenariotop):

        def __init__(self):
                super().__init__()
                self._cbfc1 = gadget_credbasedfc44()
                self._cbfctr1 = gadget_credbasedfc4Xtr()
                self._cbfctr2 = gadget_credbasedfcX4tr()
                self._fifocr1 = gadget_fifocreditreturn()
                self._fifotr1 = gadget_fifotr()
                self._modelqueue = gadget_modelqueue()
                self._check = gadget_check()
                self._control = gadget_control()
                self._fplate = gadget_fplate_sc16()

        def __del__(self):
                del self._cbfc1
                del self._cbfctr1
                del self._cbfctr2
                del self._fifocr1
                del self._fifotr1
                del self._modelqueue
                del self._check
                del self._control
                del self._fplate
                super().__del__()

        def setup_2d_model (self, ctx):
                #IN 3D VERSION THIS METHOD WILL BE USED TO PROVIDE 3D MODEL MESH, IN 2D THERE IS ONLY SUBWINDOW LAYOUTS
                self._ctx = ctx

                self._cbfc1.setup_2d_model(self._ctx.subwin(2, 5))
                self._cbfctr1.setup_2d_model(self._ctx.subwin(2, 5))
                self._cbfctr2.setup_2d_model(self._ctx.subwin(2, 8))
                self._fifocr1.setup_2d_model(self._ctx.subwin(3, 51))
                self._fifotr1.setup_2d_model(self._ctx.subwin(3, 51))
                self._modelqueue.setup_2d_model(self._ctx.subwin(22, 54))
                self._check.setup_2d_model(self._ctx.subwin(22, 93))
                self._control.setup_2d_model(self._ctx.subwin(22, 5))
                self._fplate.setup_2d_model(self._ctx.subwin(0, 0))

        def process_input_stimulus (self, hdl, key):
                self._cbfc1.process_input_stimulus (hdl, key)
                self._cbfctr1.process_input_stimulus (hdl, key)
                self._cbfctr2.process_input_stimulus (hdl, key)
                self._fifocr1.process_input_stimulus (hdl, key)
                self._fifotr1.process_input_stimulus (hdl, key)
                self._modelqueue.process_input_stimulus (hdl, key)
                self._check.process_input_stimulus (hdl, key)
                self._control.process_input_stimulus (hdl, key)
                self._fplate.process_input_stimulus (hdl, key)

        def get_logic_state_data_from_simulator (self, hdl):
                self._cbfc1.get_logic_state_data_from_simulator (hdl.RTL1.CBFC1)
                self._cbfctr1.get_logic_state_data_from_simulator (hdl.RTL1.CBFC1)
                self._cbfctr2.get_logic_state_data_from_simulator (hdl.RTL1.CBFC1)
                self._fifocr1.get_logic_state_data_from_simulator (hdl.RTL1.FIFOCR1)
                self._fifotr1.get_logic_state_data_from_simulator (hdl.RTL1.FIFOCR1)
                self._modelqueue.get_logic_state_data_from_simulator (hdl.MDL1)
                self._check.get_logic_state_data_from_simulator (hdl.CHK1)
                self._control.get_logic_state_data_from_simulator (hdl)
                self._fplate.get_logic_state_data_from_simulator (hdl)

        def post_process_logic_state (self, phase):
                self._cbfc1.post_process_logic_state (phase)
                self._cbfctr1.post_process_logic_state (phase)
                self._cbfctr2.post_process_logic_state (phase)
                self._fifocr1.post_process_logic_state (phase)
                self._fifotr1.post_process_logic_state (phase)
                self._modelqueue.post_process_logic_state (phase)
                self._check.post_process_logic_state (phase)
                self._control.post_process_logic_state (phase)
                self._fplate.post_process_logic_state (phase)

        def write_to_log (self, logfile):
                self._cbfc1.write_to_log ("CBFC1", logfile)
                self._cbfctr1.write_to_log ("CBFCTR1", logfile)
                self._cbfctr2.write_to_log ("CBFCTR2", logfile)
                self._fifocr1.write_to_log ("FIFOCR1", logfile)
                self._fifotr1.write_to_log ("FIFOTR1", logfile)
                self._modelqueue.write_to_log ("MDLQ1", logfile)
                self._check.write_to_log ("CHK1", logfile)
                self._control.write_to_log ("CONTROL", logfile)
                self._fplate.write_to_log ("FPLATE", logfile)

        def drive_2d_model (self):
                self._cbfc1.drive_2d_model ()
                self._cbfctr1.drive_2d_model ()
                self._cbfctr2.drive_2d_model ()
                self._fifocr1.drive_2d_model ()
                self._fifotr1.drive_2d_model ()
                self._modelqueue.drive_2d_model ()
                self._check.drive_2d_model ()
                self._control.drive_2d_model ()
                self._fplate.drive_2d_model ()
