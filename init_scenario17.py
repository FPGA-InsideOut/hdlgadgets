import cocotb
from lib.common.program_class import program
from lib.scenario17_class import scenario17

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario17()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
