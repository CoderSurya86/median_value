'''-*************************************************************
Date created : Jan 17, 2019                                     *
@author      : Surya Tej Nimmakayala                            *
File Name    : main.py                                          *
Description  : Main module to start the application that finds  *
               the median of a given set of input numbers.      *
*************************************************************-'''

import sys
import median_computer

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print('Insufficient arguments !!')
        print('Usage: python main.py <input-filename>')
        print('Sample Usage: python main.py ../input/input.txt')
        exit(-1)
    else: # run the code to find the median
        medComp = median_computer.medianComputer(sys.argv[1])
        medComp.extractInpData()
        
        try:
            medianValue = medComp.findMedian()
        except Exception as e:
            print('Exception type: ', type(e))
            print('Exception message: ', e)
        else: # executed only when there is no exception or median is successfully found.
            print('\nInput Data: ', medComp.getInpList(),'\n')
            print('\nSorted Input Data: ', medComp.getSortedInpList(), '\n')
            print('\nMedian value is: ', medianValue, '\n')
        
        
    