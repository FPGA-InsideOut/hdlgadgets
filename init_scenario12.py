import cocotb
from lib.common.program_class import program
from lib.scenario12_class import scenario12

@cocotb.test()
async def my_first_test(hdl):
    scenario = scenario12()
    prog = program(hdl, scenario)
    #prog.logtofile("logfile.txt")
    await prog.run()
    del prog
    del scenario
