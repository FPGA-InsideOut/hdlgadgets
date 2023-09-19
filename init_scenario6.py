import cocotb
from lib.common.program_class import program
from lib.scenario6_class import scenario6

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario6()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
