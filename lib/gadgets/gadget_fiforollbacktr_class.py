import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_fiforollbacktr(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'rst':[None], 'up_valid':[None], 'push':[None], 'write_commit':[None], 'muxrollback':[None], 'pop':[None], 'wr_ptr':[None,None,None,None], 'rd_ptr':[None,None,None,None]}
                self.logicstate_post = {'rst':[None], 'up_valid':[None], 'push':[None], 'write_commit':[None], 'muxrollback':[None], 'pop':[None], 'wr_ptr':[None,None,None,None], 'rd_ptr':[None,None,None,None]}

                #Transactions state (balls representing transactions)
                self.transstate_pre = {'balls':[None,None,None,None,None,None,None,None,None]}
                self.transstate_post = {'balls':['g','g','g','g','g','g','g','g','g']}

                #Pockets state (only for 2D CURSES version, 3D will use transaction states only)
                self.pocketsstate_pre = {'a':[None], 'b':[None], 'c0':[None], 'c1':[None], 'c2':[None], 'c3':[None], 'c4':[None], 'c5':[None], 'c6':[None], 'c7':[None], 'd0':[None], 'd1':[None], 'd2':[None], 'd3':[None], 'd4':[None], 'd5':[None], 'd6':[None], 'd7':[None], 'f':[None], 'g':[None]}
                self.pocketsstate_post = {'a':['0'], 'b':['0'], 'c0':['0'], 'c1':['0'], 'c2':['0'], 'c3':['0'], 'c4':['0'], 'c5':['0'], 'c6':['0'], 'c7':['0'], 'd0':['0'], 'd1':['0'], 'd2':['0'], 'd3':['0'], 'd4':['0'], 'd5':['0'], 'd6':['0'], 'd7':['0'], 'f':['0'], 'g':['0']}


        def __del__(self):
                super().__del__()

        def setup_2d_model (self, wctx):
                self._wctx = wctx
                self._wctx.erase()
                self._wctx.bkgd(' ', curses.color_pair(1))
                self._wctx.refresh()

        def process_input_stimulus (self, hdlpath, key):
                pass

        def get_logic_state_data_from_simulator (self, hdlpath):
                #Copy post logic state into pre logic state
                helper.dictcopy(self.logicstate_post, self.logicstate_pre)

                helper.put_hdl_vector_to_dict(self.logicstate_post['rst'], hdlpath.rst.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['up_valid'], hdlpath.up_valid.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['push'], hdlpath.push.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['write_commit'], hdlpath.write_commit.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['muxrollback'], hdlpath.muxrollback.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['pop'], hdlpath.pop.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['wr_ptr'], hdlpath.fullwidth_wr_ptr.value.binstr)
                helper.put_hdl_vector_to_dict(self.logicstate_post['rd_ptr'], hdlpath.fullwidth_rd_ptr.value.binstr)


        def post_process_logic_state (self, phase):
                #calculate new_transaction_state based on new_logic_state - this method is called after logic state has been updated

                #Copy post transaction state into pre transaction state
                helper.dictcopy(self.transstate_post, self.transstate_pre)

                simphase = None
                #SIMPHASE (0-RESET_PHASE; 1-CLOCK_PHASE; 2-COMB_PHASE)
                if (phase == 1 and self.logicstate_pre['rst'][0] == '1'):
                        simphase = 0
                elif (phase == 1 and self.logicstate_pre['rst'][0] == '0'):
                        simphase = 1
                elif (phase == 0):
                        simphase = 2


                #PROCESS TRANSACTIONS (BALLS) IN A-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'a','g')
                if (simphase == 1):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'a','g')
                if (simphase == 2):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'a','g')
                #PROCESS TRANSACTIONS (BALLS) IN B-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'b','g')
                if (simphase == 1):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'b','g')
                if (simphase == 2):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'b','g')
                #PROCESS TRANSACTIONS (BALLS) IN C0-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c0','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '0' and self.logicstate_pre['rd_ptr'][2] == '0' and self.logicstate_pre['rd_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c0','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C1-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c1','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '0' and self.logicstate_pre['rd_ptr'][2] == '0' and self.logicstate_pre['rd_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c1','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C2-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c2','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '0' and self.logicstate_pre['rd_ptr'][2] == '1' and self.logicstate_pre['rd_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c2','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C3-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c3','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '0' and self.logicstate_pre['rd_ptr'][2] == '1' and self.logicstate_pre['rd_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c3','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C4-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c4','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '1' and self.logicstate_pre['rd_ptr'][2] == '0' and self.logicstate_pre['rd_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c4','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C5-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c5','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '1' and self.logicstate_pre['rd_ptr'][2] == '0' and self.logicstate_pre['rd_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c5','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C6-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c6','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '1' and self.logicstate_pre['rd_ptr'][2] == '1' and self.logicstate_pre['rd_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c6','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C7-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c7','g')
                if (simphase == 1 and self.logicstate_pre['pop'][0] == '1' and self.logicstate_pre['rd_ptr'][1] == '1' and self.logicstate_pre['rd_ptr'][2] == '1' and self.logicstate_pre['rd_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c7','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D0-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d0','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d0','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d0','c0')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D1-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d1','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d1','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d1','c1')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D2-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d2','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d2','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d2','c2')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D3-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d3','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d3','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d3','c3')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D4-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d4','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d4','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d4','c4')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D5-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d5','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d5','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d5','c5')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D6-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d6','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d6','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d6','c6')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D7-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d7','g')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['muxrollback'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d7','b')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d7','c7')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN F-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','g')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c0')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d0')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c1')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d1')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c2')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d2')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c3')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '0' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d3')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c4')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d4')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c5')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '0' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d5')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c6')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '0'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d6')
                if (simphase == 1 and self.logicstate_pre['write_commit'][0] == '1' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','c7')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '1' and self.logicstate_pre['write_commit'][0] == '0' and self.logicstate_pre['muxrollback'][0] == '0' and self.logicstate_pre['wr_ptr'][1] == '1' and self.logicstate_pre['wr_ptr'][2] == '1' and self.logicstate_pre['wr_ptr'][3] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','d7')
                if (simphase == 1 and self.logicstate_pre['push'][0] == '0' and self.logicstate_post['up_valid'][0] == '0' and helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'f')):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','g')            #this covers ERROR condition when MASTER drops VALID without sucessful hadshaking
                if (simphase == 2 and self.logicstate_post['up_valid'][0] == '0' and helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'f')):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','g')
                #PROCESS TRANSACTIONS (BALLS) IN G-POCKET
                if (simphase == 0 and self.logicstate_post['up_valid'][0] == '1' and not helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'f')):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'g','f')
                if (simphase == 1 and self.logicstate_post['up_valid'][0] == '1' and not helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'f')):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'g','f')
                if (simphase == 2 and self.logicstate_post['up_valid'][0] == '1' and not helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'f')):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'g','f')

                self._update_pocket_state()                                      #This call is only for 2D version

        def _update_pocket_state (self):
                #THIS METHOD ONLY USED IN 2D VERSION. IN 3D VERSION TRANSACTIONS ARE REPRESENTED BY BALLS. IN 3D BALLS WILL BE MOVED
                #calculate new_pocket_states based on new_transactions_state - this method is called after transaction states have been updated
                #Copy post pocket state into pre pocket state
                helper.dictcopy(self.pocketsstate_post, self.pocketsstate_pre)

                #GET STATE OF A-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'a'):
                    self.pocketsstate_post['a'][0] = '1'
                else:
                    self.pocketsstate_post['a'][0] = '0'
                #GET STATE OF B-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'b'):
                    self.pocketsstate_post['b'][0] = '1'
                else:
                    self.pocketsstate_post['b'][0] = '0'
                #GET STATE OF C0-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c0'):
                    self.pocketsstate_post['c0'][0] = '1'
                else:
                    self.pocketsstate_post['c0'][0] = '0'
                #GET STATE OF C1-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c1'):
                    self.pocketsstate_post['c1'][0] = '1'
                else:
                    self.pocketsstate_post['c1'][0] = '0'
                #GET STATE OF C2-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c2'):
                    self.pocketsstate_post['c2'][0] = '1'
                else:
                    self.pocketsstate_post['c2'][0] = '0'
                #GET STATE OF C3-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c3'):
                    self.pocketsstate_post['c3'][0] = '1'
                else:
                    self.pocketsstate_post['c3'][0] = '0'
                #GET STATE OF C4-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c4'):
                    self.pocketsstate_post['c4'][0] = '1'
                else:
                    self.pocketsstate_post['c4'][0] = '0'
                #GET STATE OF C5-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c5'):
                    self.pocketsstate_post['c5'][0] = '1'
                else:
                    self.pocketsstate_post['c5'][0] = '0'
                #GET STATE OF C6-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c6'):
                    self.pocketsstate_post['c6'][0] = '1'
                else:
                    self.pocketsstate_post['c6'][0] = '0'
                #GET STATE OF C7-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c7'):
                    self.pocketsstate_post['c7'][0] = '1'
                else:
                    self.pocketsstate_post['c7'][0] = '0'
                #GET STATE OF D0-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d0'):
                    self.pocketsstate_post['d0'][0] = '1'
                else:
                    self.pocketsstate_post['d0'][0] = '0'
                #GET STATE OF D1-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d1'):
                    self.pocketsstate_post['d1'][0] = '1'
                else:
                    self.pocketsstate_post['d1'][0] = '0'
                #GET STATE OF D2-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d2'):
                    self.pocketsstate_post['d2'][0] = '1'
                else:
                    self.pocketsstate_post['d2'][0] = '0'
                #GET STATE OF D3-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d3'):
                    self.pocketsstate_post['d3'][0] = '1'
                else:
                    self.pocketsstate_post['d3'][0] = '0'
                #GET STATE OF D4-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d4'):
                    self.pocketsstate_post['d4'][0] = '1'
                else:
                    self.pocketsstate_post['d4'][0] = '0'
                #GET STATE OF D5-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d5'):
                    self.pocketsstate_post['d5'][0] = '1'
                else:
                    self.pocketsstate_post['d5'][0] = '0'
                #GET STATE OF D6-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d6'):
                    self.pocketsstate_post['d6'][0] = '1'
                else:
                    self.pocketsstate_post['d6'][0] = '0'
                #GET STATE OF D7-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d7'):
                    self.pocketsstate_post['d7'][0] = '1'
                else:
                    self.pocketsstate_post['d7'][0] = '0'
                #GET STATE OF F-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'f'):
                    self.pocketsstate_post['f'][0] = '1'
                else:
                    self.pocketsstate_post['f'][0] = '0'
                #GET STATE OF G-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'g'):
                    self.pocketsstate_post['g'][0] = '1'
                else:
                    self.pocketsstate_post['g'][0] = '0'


        def write_to_log (self, strprefix, logfile):
                logfile.write(strprefix + ", transactionstate_pre:" + str(self.transstate_pre) + "\n")
                logfile.write(strprefix + ", pocketsstate_pre:" + str(self.pocketsstate_pre) + "\n")

                logfile.write(strprefix + ", transactionstate_post:" + str(self.transstate_post) + "\n")
                logfile.write(strprefix + ", pocketsstate_post:" + str(self.pocketsstate_post) + "\n")

        def drive_2d_model (self):
                #WHEN 3D MODEL WILL BE IMPLEMENTED BALLS ITSELF WILL BE DYNAMICALLY MOVED FROM POCKET TO POCKET. IN 3D BALLS FOR EACH FIFO...
                #...WILL BE SEPARATE vobject.
                #FOR CURSES 2D VERSION WE ARE DEALING WITH STATIC DATA SO WE NEED TO TRACK CHANGES OF STATES OF POCKETS AND VISUALISE POCKETS INSTEAD OF BALLS
                ####A-POCKET####
                if (self.pocketsstate_post['a'][0] == '1'):
                    pass
                elif (self.pocketsstate_post['a'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(4,34, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####B-POCKET####
                if (self.pocketsstate_post['b'][0] == '1'):
                    pass
                elif (self.pocketsstate_post['b'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(1,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C0-POCKET####
                if (self.pocketsstate_post['c0'][0] == '1'):
                    self._wctx.addstr(1,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c0'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(1,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C1-POCKET####
                if (self.pocketsstate_post['c1'][0] == '1'):
                    self._wctx.addstr(3,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c1'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(3,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C2-POCKET####
                if (self.pocketsstate_post['c2'][0] == '1'):
                    self._wctx.addstr(5,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c2'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(5,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C3-POCKET####
                if (self.pocketsstate_post['c3'][0] == '1'):
                    self._wctx.addstr(7,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c3'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(7,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C4-POCKET####
                if (self.pocketsstate_post['c4'][0] == '1'):
                    self._wctx.addstr(9,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c4'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(9,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C5-POCKET####
                if (self.pocketsstate_post['c5'][0] == '1'):
                    self._wctx.addstr(11,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c5'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(11,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C6-POCKET####
                if (self.pocketsstate_post['c6'][0] == '1'):
                    self._wctx.addstr(13,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c6'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(13,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C7-POCKET####
                if (self.pocketsstate_post['c7'][0] == '1'):
                    self._wctx.addstr(15,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c7'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(15,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D0-POCKET####
                if (self.pocketsstate_post['d0'][0] == '1'):
                    self._wctx.addstr(1,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d0'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(1,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D1-POCKET####
                if (self.pocketsstate_post['d1'][0] == '1'):
                    self._wctx.addstr(3,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d1'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(3,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D2-POCKET####
                if (self.pocketsstate_post['d2'][0] == '1'):
                    self._wctx.addstr(5,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d2'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(5,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D3-POCKET####
                if (self.pocketsstate_post['d3'][0] == '1'):
                    self._wctx.addstr(7,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d3'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(7,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D4-POCKET####
                if (self.pocketsstate_post['d4'][0] == '1'):
                    self._wctx.addstr(9,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d4'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(9,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D5-POCKET####
                if (self.pocketsstate_post['d5'][0] == '1'):
                    self._wctx.addstr(11,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d5'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(11,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D6-POCKET####
                if (self.pocketsstate_post['d6'][0] == '1'):
                    self._wctx.addstr(13,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d6'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(13,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D7-POCKET####
                if (self.pocketsstate_post['d7'][0] == '1'):
                    self._wctx.addstr(15,18, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d7'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(15,18, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####F-POCKET####
                if (self.pocketsstate_post['f'][0] == '1'):
                    self._wctx.addstr(12,11, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['f'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(12,11, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####G-POCKET####
                if (self.pocketsstate_post['g'][0] == '1'):
                    pass
                elif (self.pocketsstate_post['g'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(3,10, u'\u00D7'.encode('utf-8'), curses.color_pair(2))

                self._wctx.refresh()
