module credbasedfc_44 #(parameter D_WIDTH = 6, CREDIT_WIDTH = 3)
(
input                          clk,
input                          rst,
input  [(D_WIDTH-1):0]         up_data,
input                          up_valid,
output                         up_ready,
output [(D_WIDTH-1):0]         down_data,
output                         down_valid,
input                          down_credit,
input  [(CREDIT_WIDTH-1):0]    credit_initval
);

//localparam INITVAL = 3'b100;

reg                            valid0, valid1, valid2, valid3;
reg [(D_WIDTH-1):0]            data0, data1, data2, data3;
reg                            credit0, credit1, credit2, credit3;
reg [(CREDIT_WIDTH-1):0]       creditcounter;

wire [(CREDIT_WIDTH-1):0] addend, creditcounter_d;
wire creditplus, creditminus;
wire valid_pipeline;

//Data
always @(posedge clk)
  begin
      data0 <= up_data;
      data1 <= data0;
      data2 <= data1;
      data3 <= data2;
  end

//Valid
always @(posedge clk)
if (rst) begin
      valid0 <= 1'b0;
      valid1 <= 1'b0;
      valid2 <= 1'b0;
      valid3 <= 1'b0;
 end else begin
      valid0 <= valid_pipeline;
      valid1 <= valid0;
      valid2 <= valid1;
      valid3 <= valid2;
 end

//Credit delay
always @(posedge clk)
if (rst) begin
      credit0 <= 1'b0;
      credit1 <= 1'b0;
      credit2 <= 1'b0;
      credit3 <= 1'b0;
 end else begin
      credit0 <= down_credit;
      credit1 <= credit0;
      credit2 <= credit1;
      credit3 <= credit2;
 end


//Credit counter using two's complement addition
  always @(posedge clk)
    if (rst)
      creditcounter <= credit_initval;
    else
      creditcounter <= creditcounter_d;

  //Two complements arithmetics
  //creditplus    creditminus    addend
  //         1              1      0
  //         1              0      1
  //         0              1      11..1 - this is "minus-one"
  //         0              0      0
  //assign addend = creditplus ? (creditminus ? 0 : 1) : (creditminus ? 111 : 0)


  assign down_valid = valid3;
  assign down_data = data3;
  assign valid_pipeline = up_valid & up_ready;
  assign up_ready = (| creditcounter);
  assign creditplus = credit3;
  assign creditminus = up_valid & up_ready;
  assign addend = creditplus ? (creditminus ? 0 : 1) : (creditminus ? {(CREDIT_WIDTH){1'b1}} : 0);
  assign creditcounter_d = creditcounter + addend;


endmodule
