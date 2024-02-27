import curses
from lib.common.scenariotop_class import scenariotop
from lib.gadgets.gadget_fiforollback_class import gadget_fiforollback
from lib.gadgets.gadget_fiforollbacktr_class import gadget_fiforollbacktr
from lib.gadgets.gadget_modelqueuea_class import gadget_modelqueuea
from lib.gadgets.gadget_modelqueueb_class import gadget_modelqueueb
from lib.gadgets.gadget_check_class import gadget_check
from lib.gadgets.gadget_control_class import gadget_control
from lib.gadgets.gadget_fplate_sc18_class import gadget_fplate_sc18

class scenario18(scenariotop):

        def __init__(self):
                super().__init__()
                self._fifo = gadget_fiforollback()
                self._fifotr = gadget_fiforollbacktr()
                self._modelqueue_a = gadget_modelqueuea()
                self._modelqueue_b = gadget_modelqueueb()
                self._check = gadget_check()
                self._control = gadget_control()
                self._fplate = gadget_fplate_sc18()

        def __del__(self):
                del self._fifo
                del self._fifotr
                del self._modelqueue_a
                del self._modelqueue_b
                del self._check
                del self._control
                del self._fplate
                super().__del__()

        def setup_2d_model (self, ctx):
                #IN 3D VERSION THIS METHOD WILL BE USED TO PROVIDE 3D MODEL MESH, IN 2D THERE IS ONLY SUBWINDOW LAYOUTS
                self._ctx = ctx

                self._fifo.setup_2d_model(self._ctx.subwin(2, 5))
                self._fifotr.setup_2d_model(self._ctx.subwin(2, 5))
                self._modelqueue_a.setup_2d_model(self._ctx.subwin(2, 54))
                self._modelqueue_b.setup_2d_model(self._ctx.subwin(10, 54))
                self._check.setup_2d_model(self._ctx.subwin(20, 64))
                self._control.setup_2d_model(self._ctx.subwin(26, 5))
                self._fplate.setup_2d_model(self._ctx.subwin(0, 0))

        def process_input_stimulus (self, hdl, key):
                self._fifo.process_input_stimulus (hdl, key)
                self._fifotr.process_input_stimulus (hdl, key)
                self._modelqueue_a.process_input_stimulus (hdl, key)
                self._modelqueue_b.process_input_stimulus (hdl, key)
                self._check.process_input_stimulus (hdl, key)
                self._control.process_input_stimulus (hdl, key)
                self._fplate.process_input_stimulus (hdl, key)

        def get_logic_state_data_from_simulator (self, hdl):
                self._fifo.get_logic_state_data_from_simulator (hdl.RTL1.FIFORLB1)
                self._fifotr.get_logic_state_data_from_simulator (hdl.RTL1.FIFORLB1)
                self._modelqueue_a.get_logic_state_data_from_simulator (hdl.MDL1)
                self._modelqueue_b.get_logic_state_data_from_simulator (hdl.MDL1)
                self._check.get_logic_state_data_from_simulator (hdl.CHK1)
                self._control.get_logic_state_data_from_simulator (hdl)
                self._fplate.get_logic_state_data_from_simulator (hdl)

        def post_process_logic_state (self, phase):
                self._fifo.post_process_logic_state (phase)
                self._fifotr.post_process_logic_state (phase)
                self._modelqueue_a.post_process_logic_state (phase)
                self._modelqueue_b.post_process_logic_state (phase)
                self._check.post_process_logic_state (phase)
                self._control.post_process_logic_state (phase)
                self._fplate.post_process_logic_state (phase)

        def write_to_log (self, logfile):
                self._fifo.write_to_log ("FIFORLB", logfile)
                self._fifotr.write_to_log ("FIFORLBTR", logfile)
                self._modelqueue_a.write_to_log ('MDLQ1', logfile)
                self._modelqueue_b.write_to_log ('MDLQ2', logfile)
                self._check.write_to_log ("CHK", logfile)
                self._control.write_to_log ("CONTROL", logfile)
                self._fplate.write_to_log ("FPLATE", logfile)

        def drive_2d_model (self):
                self._fifo.drive_2d_model ()
                self._fifotr.drive_2d_model ()
                self._modelqueue_a.drive_2d_model ()
                self._modelqueue_b.drive_2d_model ()
                self._check.drive_2d_model ()
                self._control.drive_2d_model ()
                self._fplate.drive_2d_model ()
