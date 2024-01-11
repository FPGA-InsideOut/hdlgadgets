import cocotb
from lib.common.program_class import program
from lib.scenario11_class import scenario11

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario11()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
