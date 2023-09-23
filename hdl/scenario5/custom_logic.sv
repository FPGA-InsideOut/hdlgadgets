module custom_logic #(parameter D_WIDTH = 6)
(
input                   clk,
input                   rst,
input  [(D_WIDTH-1):0]  up_data,
input                   up_valid,
output                  up_ready,
output [(D_WIDTH-1):0]  down_data,
output                  down_valid,
input                   down_ready
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

assign down_data = up_data;
assign down_valid = up_valid;
assign up_ready = down_ready;

//END CUSTOM LOGIC BLOCK

endmodule
