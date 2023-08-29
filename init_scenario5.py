import cocotb
from lib.common.program_class import program
from lib.scenario5_class import scenario5

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario5()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
