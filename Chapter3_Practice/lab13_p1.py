class AvgList(list):
    def computeAvg(self):
        '''Computes the average of a list of numeric types.
        Raises the ValueError exception if a list element is neither
        an 'int' nor a 'float' object.
        '''
        for i in range(len(self)):
            if type(self[i])!=int and type(self[i])!=float:
                raise ValueError
        return sum(self)/len(self)
