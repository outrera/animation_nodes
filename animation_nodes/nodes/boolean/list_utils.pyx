from ... data_structures cimport DoubleList, BooleanList, LongList

def convert_DoubleList_to_BooleanList(DoubleList inList):
    cdef BooleanList outList = BooleanList(length = inList.length)
    cdef long i
    for i in range(len(inList)):
        outList.data[i] = inList.data[i] != 0
    return outList

def convert_BooleanList_to_LongList(BooleanList inList):
    cdef LongList outList = LongList(length = inList.length)
    cdef long i
    for i in range(len(inList)):
        outList.data[i] = inList.data[i] != 0
    return outList
