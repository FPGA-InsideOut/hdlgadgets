import cocotb
from lib.common.program_class import program
from lib.scenario3_class import scenario3

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario3()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
