'''
needed because python import system is weird
'''
import sys
sys.path.append('')
'''
'''
def UpdateLocalTagList(PLCIPAddress:str ):
    """ 
    Enter the PLC Address as a string and saves all PLC tags to file
    """
    IPAddress = PLCIPAddress

    #open the file, read its current list
    with open(r'D:\pylogix\ProtoProduction\ControllerTagList.txt', mode="r", encoding='UTF-8') as tagListFile:
        oldtagList = tagListFile.read()
        print(oldtagList)

    #setup stuff to access the PLC
    #get all tags from PLC(false) <-- false means controller tags only
    from pylogix import PLC
    allTagsToWrite = ''
    with PLC(IPAddress) as DiamondElements:
        allTagsOnPLC = DiamondElements.GetTagList(False)
        with open(r'D:\pylogix\ProtoProduction\ControllerTagList.txt', mode="w", encoding='UTF-8') as tagListFile:
            for tags in allTagsOnPLC.Value:
                allTagsToWrite += tags.TagName
        
    #take all tags from PLC and write to a file
    
        tagListFile.writelines(str(allTagsToWrite))


UpdateLocalTagList('192.168.1.10')