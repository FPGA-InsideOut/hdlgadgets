module custom_param #(parameter CREDIT_WIDTH = 3)
(
output [(CREDIT_WIDTH-1):0]  credit_initval
);


//BEGIN CHANGE CUSTOM PARAMETERS HERE
assign credit_initval = 3'b100;

//END CHANGE CUSTOM PARAMETERS HERE

endmodule
