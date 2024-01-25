import cocotb
from lib.common.program_class import program
from lib.scenario14_class import scenario14

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario14()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
