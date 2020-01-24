"""
needed because fuck python import system
"""

import sys
sys.path.append('')


def timeTestforReadWrite():
    '''
    testing the time to read and write to the PLC
    '''
    from pylogix import PLC
    import time
    DiamondElements = PLC('192.168.1.10') #AB PLC IP Address

    count = 0 
    targetCycleCount = 1000

    startTime = time.time()

    """
    read the bool, write its opposite value, read it again.
    """
    while True:
        
        returnedValue = DiamondElements.Read('IO_NEEDED_HERE')

        
        print('Currently read value of ' + returnedValue.TagName + ': ' + str(returnedValue.Value))

        if returnedValue.Value == True:
            boolToWrite = 0
        else:
            boolToWrite = 1

        DiamondElements.Write('IO_NEEDED_HERE', boolToWrite)
        
        newReturnedValue = DiamondElements.Read('IO_NEEDED_HERE')
        
        print('New value after writing: ' + str(newReturnedValue.Value))

        if count >= targetCycleCount:
            break

        count += 1

    EndTime = time.time()
    totalTime = EndTime-startTime
    print(f"{totalTime:.4f} seconds with {targetCycleCount} read/write cycles")


timeTestforReadWrite()