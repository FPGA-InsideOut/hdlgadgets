import curses
from lib.common.scenariotop_class import scenariotop
from lib.gadgets.gadget_shiftreg_class import gadget_shiftreg
from lib.gadgets.gadget_shiftregtr_class import gadget_shiftregtr
from lib.gadgets.gadget_fifo_class import gadget_fifo
from lib.gadgets.gadget_fifotr_class import gadget_fifotr
from lib.gadgets.gadget_control_class import gadget_control
from lib.gadgets.gadget_fplate_sc15_class import gadget_fplate_sc15

class scenario15(scenariotop):

        def __init__(self):
                super().__init__()
                self._sftreg1 = gadget_shiftreg()
                self._sftregtr1 = gadget_shiftregtr()
                self._fifo1 = gadget_fifo()
                self._fifotr1 = gadget_fifotr()
                self._control = gadget_control()
                self._fplate = gadget_fplate_sc15()

        def __del__(self):
                del self._sftreg1
                del self._sftregtr1
                del self._fifo1
                del self._fifotr1
                del self._control
                del self._fplate
                super().__del__()

        def setup_2d_model (self, ctx):
                #IN 3D VERSION THIS METHOD WILL BE USED TO PROVIDE 3D MODEL MESH, IN 2D THERE IS ONLY SUBWINDOW LAYOUTS
                self._ctx = ctx

                self._sftreg1.setup_2d_model(self._ctx.subwin(3, 5))
                self._sftregtr1.setup_2d_model(self._ctx.subwin(3, 5))
                self._fifo1.setup_2d_model(self._ctx.subwin(3, 51))
                self._fifotr1.setup_2d_model(self._ctx.subwin(3, 51))
                self._control.setup_2d_model(self._ctx.subwin(20, 5))
                self._fplate.setup_2d_model(self._ctx.subwin(0, 0))

        def process_input_stimulus (self, hdl, key):
                self._sftreg1.process_input_stimulus (hdl, key)
                self._sftregtr1.process_input_stimulus (hdl, key)
                self._fifo1.process_input_stimulus (hdl, key)
                self._fifotr1.process_input_stimulus (hdl, key)
                self._control.process_input_stimulus (hdl, key)
                self._fplate.process_input_stimulus (hdl, key)

        def get_logic_state_data_from_simulator (self, hdl):
                self._sftreg1.get_logic_state_data_from_simulator (hdl.RTL1.SFTREG1)
                self._sftregtr1.get_logic_state_data_from_simulator (hdl.RTL1.SFTREG1)
                self._fifo1.get_logic_state_data_from_simulator (hdl.RTL1.FIFO1)
                self._fifotr1.get_logic_state_data_from_simulator (hdl.RTL1.FIFO1)
                self._control.get_logic_state_data_from_simulator (hdl)
                self._fplate.get_logic_state_data_from_simulator (hdl)

        def post_process_logic_state (self, phase):
                self._sftreg1.post_process_logic_state (phase)
                self._sftregtr1.post_process_logic_state (phase)
                self._fifo1.post_process_logic_state (phase)
                self._fifotr1.post_process_logic_state (phase)
                self._control.post_process_logic_state (phase)
                self._fplate.post_process_logic_state (phase)

        def write_to_log (self, logfile):
                self._sftreg1.write_to_log ("SFTREG1", logfile)
                self._sftregtr1.write_to_log ("SFTREGTR1", logfile)
                self._fifo1.write_to_log ("FIFO1", logfile)
                self._fifotr1.write_to_log ("FIFOTR1", logfile)
                self._control.write_to_log ("CONTROL", logfile)
                self._fplate.write_to_log ("FPLATE", logfile)

        def drive_2d_model (self):
                self._sftreg1.drive_2d_model ()
                self._sftregtr1.drive_2d_model ()
                self._fifo1.drive_2d_model ()
                self._fifotr1.drive_2d_model ()
                self._control.drive_2d_model ()
                self._fplate.drive_2d_model ()
