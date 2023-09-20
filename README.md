# hdlgadgets

**a human-in-the-loop training tool for rtl-developers, microarchitects and verification engineers allowing experiments with flow control and verification techniques**
</br></br>
In other words, "hdlgadgets" is a python written frontend that provides enhanced visualisation and interactive interface for an HDL simulator. </br></br>
"hdlgadgets" contains a library of "gadgets" packed in training scenarios. A "gadget" may come in different forms but can generally be classified either as: a fixed block that the user can only observe during simulation; a blackbox container in where they can put a custom HDL code; or an auxiliary block.
- Examples of "fixed gadgets": FIFO, Pipeline register, Credit counter, Skidbuffer.
- Examples of content of a "black box gadget": custom rtl code for glue-logic, custom hdl code for transaction-level-model.
- Examples of "auxilliary gadgets": control dashboard, visual checker.

A "gadget" is a module that can be reused in multiple training scenarios.
Here you can see an example of a training scenario comprised of three "gadgets": two FIFOs connected back-to-back and a control dashboard helping the user interact with the design:

![hdlgdtsdmo](https://github.com/FPGA-InsideOut/hdlgadgets/assets/53142676/d82d9e4d-302c-4000-af17-8373fbe8ff2d)


## How it works

"hdlgadgets" requires HDL simulator running on the background (it was tested with Icarus Verilog opensource simulator which has support for SystemVerilog). To communicate with the simulator "hdlgadgets" needs cocotb library:

![howitworks](https://github.com/FPGA-InsideOut/hdlgadgets/assets/53142676/7d4cb68a-fb0e-4ca3-9855-99e7112fbe58)

"hdlgadgets" uses hierarchical references to communicate with the simulated design. This allows to keep HDL code clean so that code can be used as the reference material for the design as is.

## Compatibility

"hdlgadgets" has been tested with the following software:
* python v3.11
* cocotb v1.8.0
* icarus_verilog v11.0

## Installation on Linux (Debian)

Update "apt":
```console
foo@debian:~$ sudo apt update
```
Install "git":
```console
foo@debian:~$ sudo apt install git
```
Install "IcarusVerilog":
```console
foo@debian:~$ sudo apt install iverilog
```
Install "python3":
```console
foo@debian:~$ sudo apt install python3
```
Install "python3-pip" - python package installer:
```console
foo@debian:~$ sudo apt install python3-pip
```
Install "CocoTB":
```console
foo@debian:~$ pip3 install cocotb
```
Get "hdlgadgets":
```console
foo@debian:~$ cd ~
foo@debian:~$ git clone https://github.com/FPGA-InsideOut/hdlgadgets.git
```
Run "start.bash" script to run the program.
```console
foo@debian:~$ cd ./hdlgadgets
foo@debian:~/hdlgadgets$ ./start.bash
```

## Installation on Windows10

* Enable Windows Subsystem for Linux (WSL)
* Download Debian from Microsoft Store
* Windows10 doesnt have default terminal that has full unicode support. Please install WindowsTerminal from Microsoft Store.

Run Debian in WSL from WindowsTerminal.

Update "apt":
```console
foo@debian:~$ sudo apt update
```
Install "git":
```console
foo@debian:~$ sudo apt install git
```
Install "IcarusVerilog":
```console
foo@debian:~$ sudo apt install iverilog
```
Install "python3":
```console
foo@debian:~$ sudo apt install python3
```
Install "python3-pip" - python package installer:
```console
foo@debian:~$ sudo apt install python3-pip
```
*On some Debian versions "cocotb" refuse to install outside python virtual environment - if that is the case then a virtual environment shall be created*

Install "python3-venv" - module for managing virtual environments:
```console
foo@debian:~$ sudo apt install python3-venv
```
Create python3 virtual environment in user home directory:
```console
foo@debian:~$ cd ~
foo@debian:~$ python3 -m venv myvirtenv
```
Activate virtual environment and install CocoTB inside it:
```console
foo@debian:~$ cd ~
foo@debian:~$ source ./myvirtenv/bin/activate
(myvirtenv) foo@debian:~$ pip3 install cocotb
```
Leave virtual environment (if you want to):
```console
(myvirtenv) foo@debian:~$ deactivate
```
Get "hdlgadgets":
```console
foo@debian:~$ cd ~
foo@debian:~$ git clone https://github.com/FPGA-InsideOut/hdlgadgets.git
```
Activate virtual environment (if not active) and run "start.bash" script to run the program:
```console
foo@debian:~$ cd ~
foo@debian:~$ source ./myvirtenv/bin/activate
(myvirtenv) foo@debian:~$ cd ./hdlgadgets
(myvirtenv) foo@debian:~/hdlgadgets$ ./start.bash
```

## Possible issues and troubleshooting

1. "hdlgadgets" uses "curses" library which may crash the program if it tries to draw outside terminal window. Although "start.bash" script checks the size of the terminal window before proceeding, it is important not to resize terminal window while "hdlgadgets" is running.

2. In case of an undexpected program crash it might not be possible to see an exact reason displayed on the screen because "curses" intercepts "stdout".

To help troubleshoot the problem it is recommended to close current terminal window. And in new terminal window start problematic scenario redirecting "stout" to a file on disk:

Start "hdlgadgets" scenario directly using "make" command:
```console
foo@debian:~$ make -B -f ./Makefile_sc1 >> ./outfile
```
Then you can analyse "outfile" for a possible error that caused program crash.

3. For Linux, standard Linux terminal can be used as it has full unicode support. On Windows10 please use WindowsTerminal and run WSL with Linux.
