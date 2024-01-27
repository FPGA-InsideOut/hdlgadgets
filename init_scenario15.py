import cocotb
from lib.common.program_class import program
from lib.scenario15_class import scenario15

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario15()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
