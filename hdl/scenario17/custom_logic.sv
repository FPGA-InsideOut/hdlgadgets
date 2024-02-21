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
assign debug[7] = push & up_tlast & up_tuser;
assign debug[6] = push & up_tlast;
assign debug[5] = push;
assign debug[4] = 1'bx;
assign debug[3] = 1'bx;
assign debug[2] = 1'bx;
assign debug[1] = 1'bx;
assign debug[0] = 1'bx;


//BEGIN CUSTOM LOGIC BLOCK
//THIS IS IMPLEMENTATION OF ROLLBACK FIFO PWR_OF_2
localparam A_WIDTH = 3;

wire up_tuser;
wire up_tlast;

reg [(A_WIDTH):0] fullwidth_wr_ptr, fullwidth_commited_wr_ptr, fullwidth_rd_ptr;
reg [(D_WIDTH-1):0] ram[2**A_WIDTH-1:0];

wire [(A_WIDTH-1):0] wr_ptr, rd_ptr;
wire [(A_WIDTH):0] fullwidth_wr_ptr_d, fullwidth_wr_ptr_incr;

wire push;
wire pop;
wire write_commit;
wire muxselect;

assign up_tuser = up_data[(D_WIDTH-1)];
assign up_tlast = up_data[(D_WIDTH-2)];

assign fullwidth_wr_ptr_incr = fullwidth_wr_ptr + 1'b1;
assign muxselect = up_tlast & up_tuser;

//2-input combinatorial MUX to produce "fullwidth_wr_ptr_d"
assign fullwidth_wr_ptr_d = muxselect ? (fullwidth_commited_wr_ptr) : (fullwidth_wr_ptr_incr);

assign write_commit = push & up_tlast & ~up_tuser;

always @ (posedge clk)
   begin
      if (push)
       ram[wr_ptr] <= up_data;
   end

//WR_CURRENT_COUNTER
always @(posedge clk)
if (rst) begin
 fullwidth_wr_ptr <= {(A_WIDTH+1){1'b0}};
 end else if (push) begin
 fullwidth_wr_ptr <= fullwidth_wr_ptr_d;
 end

//WR_COMMITED_COUNTER
always @(posedge clk)
if (rst) begin
 fullwidth_commited_wr_ptr <= {(A_WIDTH+1){1'b0}};
 end else if (write_commit) begin
 fullwidth_commited_wr_ptr <= fullwidth_wr_ptr_d;
 end

//RD_COUNTER
always @(posedge clk)
if (rst) begin
 fullwidth_rd_ptr <= {(A_WIDTH+1){1'b0}};
 end else if (pop) begin
 fullwidth_rd_ptr <= fullwidth_rd_ptr + 1;
 end

//Generate push and pop signals
assign push = up_valid & up_ready;
assign pop = down_valid & down_ready;

//output LSBits out of ext_wr_ptr
assign wr_ptr = fullwidth_wr_ptr[(A_WIDTH-1):0];
//output LSBits out of ext_rd_ptr
assign rd_ptr = fullwidth_rd_ptr[(A_WIDTH-1):0];

//"empty"
//It is "1" when MSBits and other bits of "full_rd_ptr" and "full_wr_ptr" are equal
  assign empty = ((fullwidth_commited_wr_ptr[(A_WIDTH)] == fullwidth_rd_ptr[(A_WIDTH)]) &&
                         (fullwidth_commited_wr_ptr[(A_WIDTH-1):0] == fullwidth_rd_ptr[(A_WIDTH-1):0])) ? 1'b1 : 1'b0;
//"valid" aka "not_empty"
  assign down_valid = ~empty;

//"full"
//It is "1" when MSBits of "full_rd_ptr" and "full_wr_ptr" are not equal but other bits equal
  assign full = ((fullwidth_wr_ptr[(A_WIDTH)] != fullwidth_rd_ptr[(A_WIDTH)]) &&
                         (fullwidth_wr_ptr[(A_WIDTH-1):0] == fullwidth_rd_ptr[(A_WIDTH-1):0])) ? 1'b1 : 1'b0;

//"ready" aka "not_full"
  assign up_ready = ~full;

assign down_data = ram[rd_ptr];


//END CUSTOM LOGIC BLOCK

endmodule
