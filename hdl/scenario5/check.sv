module check #(parameter D_WIDTH = 6)
(
input  [(D_WIDTH-1):0]  rtl_data,
input                   rtl_valid,
input  [(D_WIDTH-1):0]  model_data
);

//This is a BLACKBOX MODULE
//All input ports are not used inside the module because they will be accessed externally from python
//using hierarchical references and used in "post_process_logic_state" call of "check_gadget".

endmodule
