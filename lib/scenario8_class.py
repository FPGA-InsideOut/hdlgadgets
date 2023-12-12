import curses
from lib.common.scenariotop_class import scenariotop
from lib.gadgets.gadget_fifo_class import gadget_fifo
from lib.gadgets.gadget_fifotr_class import gadget_fifotr
from lib.gadgets.gadget_custlogic_xl_class import gadget_custlogic_xl
from lib.gadgets.gadget_modelqueuea_class import gadget_modelqueuea
from lib.gadgets.gadget_modelqueueb_class import gadget_modelqueueb
from lib.gadgets.gadget_check_class import gadget_check
from lib.gadgets.gadget_control_fork_class import gadget_control_fork
from lib.gadgets.gadget_fplate_sc8_class import gadget_fplate_sc8

class scenario8(scenariotop):

        def __init__(self):
                super().__init__()
                self._fifo1 = gadget_fifo()
                self._fifotr1 = gadget_fifotr()
                self._fifo2 = gadget_fifo()
                self._fifotr2 = gadget_fifotr()
                self._fifo3 = gadget_fifo()
                self._fifotr3 = gadget_fifotr()
                self._custlogic = gadget_custlogic_xl()
                self._modelqueue_a = gadget_modelqueuea()
                self._modelqueue_b = gadget_modelqueueb()
                self._check_a = gadget_check()
                self._check_b = gadget_check()
                self._control = gadget_control_fork()
                self._fplate = gadget_fplate_sc8()

        def __del__(self):
                del self._fifo1
                del self._fifotr1
                del self._fifo2
                del self._fifotr2
                del self._fifo3
                del self._fifotr3
                del self._custlogic
                del self._modelqueue_a
                del self._modelqueue_b
                del self._check_a
                del self._check_b
                del self._control
                del self._fplate
                super().__del__()

        def setup_2d_model (self, ctx):
                #IN 3D VERSION THIS METHOD WILL BE USED TO PROVIDE 3D MODEL MESH, IN 2D THERE IS ONLY SUBWINDOW LAYOUTS
                self._ctx = ctx

                self._fifo1.setup_2d_model(self._ctx.subwin(2, 5))
                self._fifotr1.setup_2d_model(self._ctx.subwin(2, 5))
                self._fifo2.setup_2d_model(self._ctx.subwin(2, 61))
                self._fifotr2.setup_2d_model(self._ctx.subwin(2, 61))
                self._fifo3.setup_2d_model(self._ctx.subwin(17, 61))
                self._fifotr3.setup_2d_model(self._ctx.subwin(17, 61))
                self._custlogic.setup_2d_model(self._ctx.subwin(5, 51))
                self._modelqueue_a.setup_2d_model(self._ctx.subwin(32, 16))
                self._modelqueue_b.setup_2d_model(self._ctx.subwin(32, 54))
                self._check_a.setup_2d_model(self._ctx.subwin(32, 92))
                self._check_b.setup_2d_model(self._ctx.subwin(36, 92))
                self._control.setup_2d_model(self._ctx.subwin(19, 1))
                self._fplate.setup_2d_model(self._ctx.subwin(0, 0))

        def process_input_stimulus (self, hdl, key):
                self._fifo1.process_input_stimulus (hdl, key)
                self._fifotr1.process_input_stimulus (hdl, key)
                self._fifo2.process_input_stimulus (hdl, key)
                self._fifotr2.process_input_stimulus (hdl, key)
                self._fifo3.process_input_stimulus (hdl, key)
                self._fifotr3.process_input_stimulus (hdl, key)
                self._custlogic.process_input_stimulus (hdl, key)
                self._modelqueue_a.process_input_stimulus (hdl, key)
                self._modelqueue_b.process_input_stimulus (hdl, key)
                self._check_a.process_input_stimulus (hdl, key)
                self._check_b.process_input_stimulus (hdl, key)
                self._control.process_input_stimulus (hdl, key)
                self._fplate.process_input_stimulus (hdl, key)

        def get_logic_state_data_from_simulator (self, hdl):
                self._fifo1.get_logic_state_data_from_simulator (hdl.RTL1.FIFO1)
                self._fifotr1.get_logic_state_data_from_simulator (hdl.RTL1.FIFO1)
                self._fifo2.get_logic_state_data_from_simulator (hdl.RTL1.FIFO2)
                self._fifotr2.get_logic_state_data_from_simulator (hdl.RTL1.FIFO2)
                self._fifo3.get_logic_state_data_from_simulator (hdl.RTL1.FIFO3)
                self._fifotr3.get_logic_state_data_from_simulator (hdl.RTL1.FIFO3)
                self._custlogic.get_logic_state_data_from_simulator (hdl.RTL1.CLGC1)
                self._modelqueue_a.get_logic_state_data_from_simulator (hdl.MDL1)
                self._modelqueue_b.get_logic_state_data_from_simulator (hdl.MDL1)
                self._check_a.get_logic_state_data_from_simulator (hdl.CHK1)
                self._check_b.get_logic_state_data_from_simulator (hdl.CHK2)
                self._control.get_logic_state_data_from_simulator (hdl)
                self._fplate.get_logic_state_data_from_simulator (hdl)

        def post_process_logic_state (self, phase):
                self._fifo1.post_process_logic_state (phase)
                self._fifotr1.post_process_logic_state (phase)
                self._fifo2.post_process_logic_state (phase)
                self._fifotr2.post_process_logic_state (phase)
                self._fifo3.post_process_logic_state (phase)
                self._fifotr3.post_process_logic_state (phase)
                self._custlogic.post_process_logic_state (phase)
                self._modelqueue_a.post_process_logic_state (phase)
                self._modelqueue_b.post_process_logic_state (phase)
                self._check_a.post_process_logic_state (phase)
                self._check_b.post_process_logic_state (phase)
                self._control.post_process_logic_state (phase)
                self._fplate.post_process_logic_state (phase)

        def write_to_log (self, logfile):
                self._fifo1.write_to_log ("FIFO1", logfile)
                self._fifotr1.write_to_log ("FIFOTR1", logfile)
                self._fifo2.write_to_log ("FIFO2", logfile)
                self._fifotr2.write_to_log ("FIFOTR2", logfile)
                self._fifo3.write_to_log ("FIFO2", logfile)
                self._fifotr3.write_to_log ("FIFOTR2", logfile)
                self._custlogic.write_to_log ("CUSTLOGIC", logfile)
                self._modelqueue_a.write_to_log ('MDLQ1', logfile)
                self._modelqueue_b.write_to_log ('MDLQ2', logfile)
                self._check_a.write_to_log ('CHK1', logfile)
                self._check_b.write_to_log ('CHK2', logifle)
                self._control.write_to_log ("CONTROL", logfile)
                self._fplate.write_to_log ("FPLATE", logfile)

        def drive_2d_model (self):
                self._fifo1.drive_2d_model ()
                self._fifotr1.drive_2d_model ()
                self._fifo2.drive_2d_model ()
                self._fifotr2.drive_2d_model ()
                self._fifo3.drive_2d_model ()
                self._fifotr3.drive_2d_model ()
                self._custlogic.drive_2d_model ()
                self._modelqueue_a.drive_2d_model ()
                self._modelqueue_b.drive_2d_model ()
                self._check_a.drive_2d_model ()
                self._check_b.drive_2d_model ()
                self._control.drive_2d_model ()
                self._fplate.drive_2d_model ()
