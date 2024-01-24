import curses
from lib.common.gadgettop_class import gadgettop
from lib.common.helper_class import helper

class gadget_shiftregtr(gadgettop):

        def __init__(self):
                super().__init__()

                #Logic state
                self.logicstate_pre = {'rst':[None], 'up_valid':[None], 'down_ready':[None]}
                self.logicstate_post = {'rst':[None], 'up_valid':[None], 'down_ready':[None]}

                #Transactions state (balls representing transactions)
                self.transstate_pre = {'balls':[None,None,None,None,None,None]}
                self.transstate_post = {'balls':['g','g','g','g','g','g']}

                #Pockets state (only for 2D CURSES version, 3D will use transaction states only)
                self.pocketsstate_pre = {'a':[None], 'b':[None], 'c':[None], 'd':[None], 'e':[None], 'f':[None], 'g':[None]}
                self.pocketsstate_post = {'a':['0'], 'b':['0'], 'c':['0'], 'd':['0'], 'e':['0'], 'f':['0'], 'g':['0']}


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
                helper.put_hdl_vector_to_dict(self.logicstate_post['down_ready'], hdlpath.down_ready.value.binstr)


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
                if (simphase == 1 and self.logicstate_pre['down_ready'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'b','a')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN C-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c','g')
                if (simphase == 1 and self.logicstate_pre['down_ready'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'c','b')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN D-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d','g')
                if (simphase == 1 and self.logicstate_pre['down_ready'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'d','c')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN E-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'e','g')
                if (simphase == 1 and self.logicstate_pre['down_ready'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'e','d')
                if (simphase == 2):
                        pass
                #PROCESS TRANSACTIONS (BALLS) IN F-POCKET
                if (simphase == 0):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','g')
                if (simphase == 1 and self.logicstate_pre['up_valid'][0] == '1' and self.logicstate_pre['down_ready'][0] == '1'):
                        helper.convert_single_transaction_of_some_state(self.transstate_post['balls'],'f','e')
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
                #GET STATE OF C-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'c'):
                    self.pocketsstate_post['c'][0] = '1'
                else:
                    self.pocketsstate_post['c'][0] = '0'
                #GET STATE OF D-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'d'):
                    self.pocketsstate_post['d'][0] = '1'
                else:
                    self.pocketsstate_post['d'][0] = '0'
                #GET STATE OF E-POCKET
                if helper.check_transaction_of_some_state_exists(self.transstate_post['balls'],'e'):
                    self.pocketsstate_post['e'][0] = '1'
                else:
                    self.pocketsstate_post['e'][0] = '0'
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
                    self._wctx.addstr(4,34, u'\u00D7'.encode('utf-8'), curses.color_pair(1))
                ####B-POCKET####
                if (self.pocketsstate_post['b'][0] == '1'):
                    self._wctx.addstr(7,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['b'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(7,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####C-POCKET####
                if (self.pocketsstate_post['c'][0] == '1'):
                    self._wctx.addstr(5,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['c'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(5,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####D-POCKET####
                if (self.pocketsstate_post['d'][0] == '1'):
                    self._wctx.addstr(3,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['d'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(3,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####E-POCKET####
                if (self.pocketsstate_post['e'][0] == '1'):
                    self._wctx.addstr(1,27, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['e'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(1,27, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####F-POCKET####
                if (self.pocketsstate_post['f'][0] == '1'):
                    self._wctx.addstr(4,11, u'\u274B'.encode('utf-8'), curses.color_pair(2))
                elif (self.pocketsstate_post['f'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(4,11, u'\u00D7'.encode('utf-8'), curses.color_pair(2))
                ####G-POCKET####
                if (self.pocketsstate_post['g'][0] == '1'):
                    pass
                elif (self.pocketsstate_post['g'][0] == '0'):
                    pass
                else:
                    self._wctx.addstr(3,10, u'\u00D7'.encode('utf-8'), curses.color_pair(2))

                self._wctx.refresh()
