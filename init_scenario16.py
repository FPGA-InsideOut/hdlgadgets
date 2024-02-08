import cocotb
from lib.common.program_class import program
from lib.scenario16_class import scenario16

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario16()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
