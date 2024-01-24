import curses
from lib.common.scenariotop_class import scenariotop
from lib.gadgets.gadget_shiftreg_class import gadget_shiftreg
from lib.gadgets.gadget_shiftregtr_class import gadget_shiftregtr
from lib.gadgets.gadget_control_class import gadget_control
from lib.gadgets.gadget_fplate_sc12_class import gadget_fplate_sc12

class scenario12(scenariotop):

        def __init__(self):
                super().__init__()
                self._sftreg = gadget_shiftreg()
                self._sftregtr = gadget_shiftregtr()
                self._control = gadget_control()
                self._fplate = gadget_fplate_sc12()

        def __del__(self):
                del self._sftreg
                del self._sftregtr
                del self._control
                del self._fplate
                super().__del__()

        def setup_2d_model (self, ctx):
                #IN 3D VERSION THIS METHOD WILL BE USED TO PROVIDE 3D MODEL MESH, IN 2D THERE IS ONLY SUBWINDOW LAYOUTS
                self._ctx = ctx

                self._sftreg.setup_2d_model(self._ctx.subwin(3, 5))
                self._sftregtr.setup_2d_model(self._ctx.subwin(3, 5))
                self._control.setup_2d_model(self._ctx.subwin(20, 5))
                self._fplate.setup_2d_model(self._ctx.subwin(0, 0))

        def process_input_stimulus (self, hdl, key):
                self._sftreg.process_input_stimulus (hdl, key)
                self._sftregtr.process_input_stimulus (hdl, key)
                self._control.process_input_stimulus (hdl, key)
                self._fplate.process_input_stimulus (hdl, key)

        def get_logic_state_data_from_simulator (self, hdl):
                self._sftreg.get_logic_state_data_from_simulator (hdl.RTL1.SFTREG1)
                self._sftregtr.get_logic_state_data_from_simulator (hdl.RTL1.SFTREG1)
                self._control.get_logic_state_data_from_simulator (hdl)
                self._fplate.get_logic_state_data_from_simulator (hdl)

        def post_process_logic_state (self, phase):
                self._sftreg.post_process_logic_state (phase)
                self._sftregtr.post_process_logic_state (phase)
                self._control.post_process_logic_state (phase)
                self._fplate.post_process_logic_state (phase)

        def write_to_log (self, logfile):
                self._sftreg.write_to_log ("SFTREG1", logfile)
                self._sftregtr.write_to_log ("SFTREGTR1", logfile)
                self._control.write_to_log ("CONTROL", logfile)
                self._fplate.write_to_log ("FPLATE", logfile)

        def drive_2d_model (self):
                self._sftreg.drive_2d_model ()
                self._sftregtr.drive_2d_model ()
                self._control.drive_2d_model ()
                self._fplate.drive_2d_model ()
