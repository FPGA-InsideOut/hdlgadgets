#!/usr/bin/env bash

clear

echo "Select Scenario:"
echo "  1) One_FIFO"
echo "  2) One_FIFO with Model"
echo "  3) Two_FIFOs"
echo "  4) Two_FIFOs with Custom_Logic"
echo "  5) Two_FIFOs with Custom_Logic with Model"
echo "  6) Two_FIFOs with Model"
echo "  7) Fork One_FIFO to Two_FIFOs with Custom_Logic"
echo "  8) Fork One_FIFO to Two_FIFOs with Custom_Logic with Model"
echo "  9) Join Two_FIFOs to One_FIFO with Custom_Logic"
echo "  10) Join Two_FIFOs to One_FIFO with Custom_Logic with Model"

read n

termcolumns=$(tput cols)
termlines=$(tput lines)

#Check miminum size of terminal window
if [ "$n" = "1" ]; then
    if [ $termcolumns -lt 52 ] || [ $termlines -lt 29 ]; then { echo "Expand terminal window to minimum: 52x29, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "2" ]; then
    if [ $termcolumns -lt 97 ] || [ $termlines -lt 30 ]; then { echo "Expand terminal window to minimum: 97x30, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "3" ]; then
    if [ $termcolumns -lt 98 ] || [ $termlines -lt 30 ]; then { echo "Expand terminal window to minimum: 98x30, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "4" ]; then
    if [ $termcolumns -lt 108 ] || [ $termlines -lt 30 ]; then { echo "Expand terminal window to minimum: 108x30, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "5" ]; then
    if [ $termcolumns -lt 109 ] || [ $termlines -lt 30 ]; then { echo "Expand terminal window to minimum: 109x30, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "6" ]; then
    if [ $termcolumns -lt 109 ] || [ $termlines -lt 30 ]; then { echo "Expand terminal window to minimum: 109x30, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "7" ]; then
    if [ $termcolumns -lt 108 ] || [ $termlines -lt 31 ]; then { echo "Expand terminal window to minimum: 108x31, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "8" ]; then
    if [ $termcolumns -lt 108 ] || [ $termlines -lt 39 ]; then { echo "Expand terminal window to minimum: 108x39, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "9" ]; then
    if [ $termcolumns -lt 108 ] || [ $termlines -lt 30 ]; then { echo "Expand terminal window to minimum: 108x30, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi
if [ "$n" = "10" ]; then
    if [ $termcolumns -lt 109 ] || [ $termlines -lt 29 ]; then { echo "Expand terminal window to minimum: 109x29, your window is too small: ${termcolumns}x${termlines}" ; exit 1; } fi
fi

#Start Cocotb
case $n in
  1) make -B -f Makefile_sc1;;
  2) make -B -f Makefile_sc2;;
  3) make -B -f Makefile_sc3;;
  4) make -B -f Makefile_sc4;;
  5) make -B -f Makefile_sc5;;
  6) make -B -f Makefile_sc6;;
  7) make -B -f Makefile_sc7;;
  8) make -B -f Makefile_sc8;;
  9) make -B -f Makefile_sc9;;
  10) make -B -f Makefile_sc10;;
  *) echo "invalid option";;
esac