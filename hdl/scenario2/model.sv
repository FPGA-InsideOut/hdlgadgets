//---MODEL---//

module model #(parameter D_WIDTH = 6)
(
input                         clk,
input                         rst,
input        [(D_WIDTH-1):0]  up_data,
input                         push,
output logic [(D_WIDTH-1):0]  down_data,
input                         pop
);

// Modeling
int unsigned qsize;
logic [D_WIDTH - 1:0] queue [$];
logic [D_WIDTH - 1:0] queue0, queue1, queue2;

////START OF QUEUE MODEL////
  always @ (posedge clk)
  begin
    if (rst)
    begin
      queue = {};
    end
    else
    ////DO MODELLING HERE////
    begin
      if (push)
      begin
        queue.push_back (up_data);
      end
      if (pop)
      begin
        if (queue.size () != 0)
        begin
          queue.delete (0);          // queue.delete(0) is used as "queue.pop_front()" method doesn't work in Icarus
        end
      end
    end

    qsize = queue.size ();
    //Cocotb cannot access queue[$] via hierarchical reference but can access queue0, queue1, queue2 with coonstant indexes
    queue0 = queue [0];
    queue1 = queue [1];
    queue2 = queue [2];
    down_data = queue [0];

  end
////END OF QUEUE MODEL////

endmodule
