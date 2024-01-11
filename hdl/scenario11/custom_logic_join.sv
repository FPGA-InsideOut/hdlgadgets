module custom_logic_join #(parameter D_WIDTH = 6)
(
input                   clk,
input                   rst,
input  [(D_WIDTH-1):0]  up_data_a,
input                   up_valid_a,
output                  up_ready_a,
input  [(D_WIDTH-1):0]  up_data_b,
input                   up_valid_b,
output                  up_ready_b,
output [(D_WIDTH-1):0]  down_data,
output                  down_valid,
input                   down_ready
);

//Connect signals to the debug vector for visualisation
wire [7:0] debug;


//REASSIGN DEBUG SIGNALS AS NEEDED
assign debug[7] = state;
assign debug[6] = next;
assign debug[5] = 1'bx;
assign debug[4] = 1'bx;
assign debug[3] = 1'bx;
assign debug[2] = 1'bx;
assign debug[1] = 1'bx;
assign debug[0] = 1'bx;


//BEGIN CUSTOM LOGIC BLOCK
//THIS IS IMPLEMENTATION OF ROUND-ROBIN PACKET ARBITER (NON-BLOCKING)
reg prev_grant;
reg new_grant;
wire sel;
wire latch_grant;
wire tlast;

//Register that stores current grant value
always @(posedge clk)
  if (rst) begin
    prev_grant <= 1'b0;
    end else if (latch_grant) begin
    prev_grant <= sel;
    end

assign sel = (latch_grant) ? new_grant : prev_grant;


wire req;
assign req = up_valid_a | up_valid_b;
assign tlast = down_data[(D_WIDTH-1)];    //tlast is the most significant bit in data vector. Packet multiplexing is based on tlast


//////BEGIN FSM
  parameter WAIT_FOR_REQ = 1'b0,
            WAIT_FOR_LAST = 1'b1;

  reg state, next;

  always @(posedge clk)
    if (rst) state <= WAIT_FOR_REQ;
    else state <= next;

  always @(state or req or tlast or down_ready or down_valid) begin
    next = 'bx;
    case (state)
      WAIT_FOR_REQ    : if (req & ~tlast & down_ready) next = WAIT_FOR_LAST;
               else next = WAIT_FOR_REQ;
      WAIT_FOR_LAST   : if (down_valid & tlast & down_ready) next = WAIT_FOR_REQ;
               else next = WAIT_FOR_LAST;
    endcase
  end

  assign latch_grant = ((state == WAIT_FOR_REQ) & (req) & (down_ready));
///END FSM


//2-req Arbiter (combinatorial)
always @ (prev_grant or up_valid_a or up_valid_b) begin
case (prev_grant) // synopsys full_case parallel_case
1'b0 :            //up_valid_a
if (up_valid_b) new_grant = 1'b1;
else new_grant = 1'b0;
1'b1 :            //up_valid_b
if (up_valid_a) new_grant = 1'b0;
else new_grant = 1'b1;
endcase // case(req)
end


//Mux for assigning down_valid and down_data
assign down_data = (sel) ? up_data_b : up_data_a;
assign down_valid = (sel) ? up_valid_b : up_valid_a;
//Demux for up_ready_a and up_ready_b
assign up_ready_a = (~sel & down_ready);
assign up_ready_b = (sel & down_ready);

//END CUSTOM LOGIC BLOCK

endmodule
