import cocotb
from lib.common.program_class import program
from lib.scenario18_class import scenario18

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario18()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
