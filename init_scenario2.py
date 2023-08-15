import cocotb
from lib.common.program_class import program
from lib.scenario2_class import scenario2

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario2()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
