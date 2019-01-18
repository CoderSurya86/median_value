'''-*********************************************************
Date created: Jan 17, 2019                                  *
@author     : Surya Tej Nimmakayala                         *
Filename    : median_computer.py                            *
Description : Module with implementation to find the median *
              in a given set of input numbers from a file.  *
*********************************************************-'''


class medianComputer:
    '''
    medianComputer: Class with implementation of logic to 
    compute median from a given set of numbers.
    '''

    def __init__(self, inpFName):
        '''
        @precondition  : None
        @postcondition : Class variables initialized with
                         appropriate start-up values.
        @return        : None.
        @param inpFName: Input filename passed by client
                         during the creation of medianComputer
                         class instance. 
        Description    : Constructor of the class medianComputer
                         to initialize class variables.
        '''
        self.fName = inpFName
        self.numList = []
        self.sortedList = []
        
        
        
    def extractInpData(self):
        '''
        @precondition : class variables initialized with
                        input filename and empty list of 
                        input data.
        @postcondition: self.numList populated with data
                        from input file, if it is valid.
        @return       : None.
        @param None   : No input parameters. Works with
                        class variables created in __init__
                        or the class constructor.   
        Description   : Method to extract data
                        from the input file.
        '''
        try:
            ifile = open(self.fName)
        except Exception as e:
            print('Exception type: ', type(e))
            print('Exception message: ', e)
        else:
            for fNum in ifile:
                if(fNum != ''):
                    self.numList.append(int(fNum))
            ifile.close()     
            
        
            
    def findMedian(self):
        '''
        @precondition : Class variable 'self.numList' is
                        populated with data from input file.
                        List length should be > 0.
        @postcondition: No change to list data.
        @return       : Median value from list of numbers.
        @param None   : No input arguments. Deals with the
                        class variables.
        @raise PreconditionViolationException:
                        Raise exception to notify the client
                        of the violation of precondition, which
                        is to have a non-zero list length, or in
                        other words a non-empty input file. 
        Description   : Method to find the median value from 
                        the set of input numbers.
        '''
        # Sort list and compute the needed intermediate values
        self.sortedList = sorted(self.numList)
        listLen = len(self.sortedList)
        
        if(listLen == 0):
            raise ValueError('Input data file: ', self.fName,', should not be empty !!')
        else: 
            isListLenOdd = listLen % 2
            midListIdx = listLen // 2 # integer division
        
            if(isListLenOdd):
                return self.sortedList[midListIdx]
            else:
                return (self.sortedList[midListIdx-1] + self.sortedList[midListIdx]) / 2




    def getInpList(self):
        '''
        @precondition  : Class variable self.numList populated 
                         with required data. 
        @postcondition : No change to data in class variable
                         self.numList.
        @return        : Data in class variable: self.numList.
        @param None    : No input parameters.
        Description    : Method for client to retrieve the
                         input data as a list.
        '''
        return self.numList
    
    
    
    def getSortedInpList(self):
        '''
        @precondition  : Class variable self.sortedList populated 
                         with required data. 
        @postcondition : No change to data in class variable
                         self.sortedList.
        @return        : Data in class variable: self.sortedList.
        @param None    : No input parameters.
        Description    : Method for client to retrieve the
                         input data as a list.
        '''
        return self.sortedList