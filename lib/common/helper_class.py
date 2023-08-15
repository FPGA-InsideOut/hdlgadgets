class helper():

        @staticmethod
        def dictcopy (srcdict, dstdict):                                                               #Copy one dictionary into another
                for vectorname, vectorvalue in srcdict.items():
                    for vectorunit in range(len(vectorvalue)):
                        dstdict[vectorname][vectorunit] = srcdict[vectorname][vectorunit]

        @staticmethod
        def put_hdl_vector_to_dict (dstdictvectorname, hdlstrvectorvalue):                             #write logic vector into dictionary
                for vectorindex, vectorunit in enumerate(hdlstrvectorvalue):
                    dstdictvectorname[vectorindex] = vectorunit

        @staticmethod
        def show_dict_charlist_as_string (srcdictcharlist):                                            #convert list of chars into a string
                outstr = ''
                for ch in srcdictcharlist:
                    outstr += ch
                return outstr

        @staticmethod
        def check_transaction_of_some_state_exists (dictvectorname, matchingstate):                    #check that element exists in the list
                vectorindex = 0
                while vectorindex < len(dictvectorname):
                    if (dictvectorname[vectorindex] == matchingstate):
                        return True
                    else:
                        vectorindex = vectorindex + 1
                return False

        @staticmethod
        def convert_single_transaction_of_some_state (dictvectorname, matchingstate, newstate):        #find one element in a list and convert it
                vectorindex = 0
                while vectorindex < len(dictvectorname):
                    if (dictvectorname[vectorindex] == matchingstate):
                        dictvectorname[vectorindex] = newstate
                        vectorindex = len(dictvectorname)
                    else:
                        vectorindex = vectorindex + 1

