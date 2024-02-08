import locale
import curses
import cocotb
from cocotb.triggers import RisingEdge, ReadOnly, Timer

class program ():

    def __init__(self, hdl, scenario):
        self.hdl = hdl
        self._scenario = scenario

        self.logenable = False
        self.logfile = None

        locale.setlocale(locale.LC_ALL, '')

        #Start initialisation of 2D drawing environment (using curses in this case)
        self.ctx = curses.initscr()
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        self.ctx.keypad(True)
        if curses.has_colors():
            curses.start_color()
            curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
            curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_RED)
        #Finish initialisation of 2D drawging environment
        self._scenario.setup_2d_model(self.ctx)

    def __del__(self):
        #Start removal of 2D drawing environment
        curses.nocbreak()
        self.ctx.keypad(0)
        curses.echo()
        curses.curs_set(1)
        curses.endwin()
        #End removal of 2D drawing environment
        del self.ctx
        #Close logfile
        if (self.logenable):
            self.logfile.write("STOP Logging\n")
            self.logfile.close()

    def processpressedkey(self):
        keypressed = self.ctx.getch()
        if (keypressed == 27):                                                              #ESC or ALT key was pressed
            self.ctx.nodelay(True)
            n = self.ctx.getch()
            if (n == -1):                                                                   #ESC was pressed
                returnphase = 3
            self.ctx.nodelay(False)
        elif (keypressed == curses.KEY_ENTER or keypressed == 10 or keypressed == 13):      #ENTER was pressed
            returnphase = 1
        else:                                                                               #Other KEY pressed
            returnphase = 0
        return keypressed,returnphase

    def logtofile(self, filename):
        self.logenable = True
        self.logfile = open(filename, 'w')
        self.logfile.write("START Logging\n")

    async def run(self):

        await ReadOnly()

        pressedkey = None
        phase = 0
        run_loop = 1
        while (run_loop == 1):
            if (phase == 0 or phase == 1):
                if (phase == 0):                                                      #phase0 - STIMULUS PHASE
                    await Timer(1, units='step')
                    self._scenario.process_input_stimulus(self.hdl, pressedkey)
                else:                                                                 #phase1 - POSEDGE PHASE
                    await RisingEdge(self.hdl.clk)
                await ReadOnly()
                self._scenario.get_logic_state_data_from_simulator(self.hdl)          #get data from simulator
                self._scenario.post_process_logic_state(phase)                        #calculate new_transaction_state based on new_logic_state (POSEDGE_PHASE)
                self._scenario.drive_2d_model()
                if (self.logenable):
                    self._scenario.write_to_log(self.logfile)                           #print pre, post states to logfile
                pressedkey,phase = self.processpressedkey()
            else:
                run_loop = 0
