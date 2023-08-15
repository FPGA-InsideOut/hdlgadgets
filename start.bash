#!/usr/bin/env bash
echo "Select Scenario:"
echo "  1) One_FIFO"
echo "  2) One_FIFO with Model"
echo "  3) Two_FIFOs"
echo "  4) Two_FIFOs with Custom_Logic"


read n
case $n in
  1) make -B -f Makefile_sc1;;
  2) make -B -f Makefile_sc2;;
  3) make -B -f Makefile_sc3;;
  4) make -B -f Makefile_sc4;;
  *) echo "invalid option";;
esac