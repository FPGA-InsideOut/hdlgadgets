module custom_logic_fork #(parameter D_WIDTH = 6)
(
input                   clk,
input                   rst,
input  [(D_WIDTH-1):0]  up_data,
input                   up_valid,
output                  up_ready,
output [(D_WIDTH-1):0]  down_data_a,
output                  down_valid_a,
input                   down_ready_a,
output [(D_WIDTH-1):0]  down_data_b,
output                  down_valid_b,
input                   down_ready_b
);

//Connect signals to the debug vector for visualisation
wire [7:0] debug;


//REASSIGN DEBUG SIGNALS AS NEEDED
assign debug[7] = 1'bx;
assign debug[6] = 1'bx;
assign debug[5] = 1'bx;
assign debug[4] = 1'bx;
assign debug[3] = 1'bx;
assign debug[2] = 1'bx;
assign debug[1] = 1'bx;
assign debug[0] = 1'bx;


//BEGIN CUSTOM LOGIC BLOCK

assign down_data_a = up_data;
assign down_data_b = up_data;
assign down_valid_a = up_valid & down_ready_a & down_ready_b;
assign down_valid_b = up_valid & down_ready_a & down_ready_b;
assign up_ready = down_ready_a & down_ready_b;

//END CUSTOM LOGIC BLOCK

endmodule
