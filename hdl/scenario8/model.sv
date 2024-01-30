//---MODEL---//

module model #(parameter D_WIDTH = 6)
(
input                         clk,
input                         rst,
input        [(D_WIDTH-1):0]  up_data,
input                         push,
output logic [(D_WIDTH-1):0]  down_data_a,
output logic [(D_WIDTH-1):0]  down_data_b,
input                         pop_a,
input                         pop_b
);

// Modeling
int unsigned qsize_a, qsize_b;
logic [(D_WIDTH-1):0] queue_a [$], queue_b [$];
logic [(D_WIDTH-1):0] queue0_a, queue1_a, queue2_a, queue0_b, queue1_b, queue2_b;

////START OF QUEUE MODEL////
  always @ (posedge clk)
  begin
    if (rst)
    begin
      queue_a = {};
      queue_b = {};
    end
    else
    ////DO MODELLING HERE////
    begin
      if (push)
      begin                          //blocking assignments and function calls can be used between these begin and end
        queue_a.push_back (up_data);
        queue_b.push_back (up_data);
      end
      if (pop_a)
      begin
        if (queue_a.size () != 0)
        begin
          queue_a.delete (0);          // queue.delete(0) is used because "queue.pop_front()" method doesn't work in IcarusVerilog
        end
      end
      if (pop_b)
      begin
        if (queue_b.size () != 0)
        begin
          queue_b.delete (0);          // queue.delete(0) is used because "queue.pop_front()" method doesn't work in IcarusVerilog
        end
      end
    end

    //The Model doesn't interact with RTL but let's use non-blocking assigments for final model values,
    //it is just a good parctice that will help avoid races between RTL and Model
    qsize_a <= queue_a.size ();
    qsize_b <= queue_b.size ();
    //Cocotb cannot access queue[$] via hierarchical reference but can access queue0, queue1, queue2 with constant indexes
    queue0_a <= queue_a [0];
    queue1_a <= queue_a [1];
    queue2_a <= queue_a [2];
    down_data_a <= queue_a [0];
    queue0_b <= queue_b [0];
    queue1_b <= queue_b [1];
    queue2_b <= queue_b [2];
    down_data_b <= queue_b [0];

  end
////END OF QUEUE MODEL////

endmodule
