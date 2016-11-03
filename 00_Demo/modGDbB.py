import datetime
def validateDate(date_txt):
    try:
        dT = datetime.datetime.strptime(date_txt, '%m-%d-%y')
        return dT
    except:
        pass
        #raise ValueError("Incorrect Data Format, should be MM-DD-YY")
    
class year:
    typeDT = type( datetime.datetime.strptime("10-10-10", '%m-%d-%y') )
    listObjShow = []   
    def __init__(self,pathToYear):
        self.indxShows = []     
        with open(pathToYear) as f:
            self.data = f.readlines()
        
        
    def parseShows(self):
        k = 0
        for items in self.data:
            entry1 = items.split(" ")[0]
            #print entry1
            test = validateDate(entry1)
            #print type(test)
            #print test
            try:
                thisDay = test.day
                self.indxShows.append(k)
            #if type(test) == self.typeDT:
            #    self.indxShows.append(k)
                print entry1
            except:
                pass
            k = k + 1
        #build index of showStartStop
        self.numShows = len(self.indxShows)
        self.indxShowStartEnd = []
        indxEnd = len(self.data)
        for i in range(0,self.numShows):
            if i < self.numShows -1 :
                tupleStartEnd = ( self.indxShows[i], self.indxShows[i+1] - 1 )
                self.indxShowStartEnd.append( tupleStartEnd )
            else:
                self.indxShowStartEnd.append( (self.indxShows[i], len(self.data) -1 ) )
        #build listObjShow
        #for items in self.indxShowStartEnd:
        #    self.listObjShow.append(  show(self, items) )
        
class show:
    def __init__(self, objYear, tupleStartEnd):
        self.listFile = objYear.data[tupleStartEnd[0] : tupleStartEnd[1] ]
        thisDate = self.listFile[0].split(" ")[0]
        self.strDate = thisDate
        self.objDate = validateDate( thisDate )
        self.numSets = 0L

        # set up sets
        emptyLines = []
        k = 0
        for items in self.listFile:
            if items.strip() == '': emptyLines.append(k)
            k = k + 1

        self._emptyLines = emptyLines
        self.numSets = int(len(self._emptyLines) - 2)
        if not 1 in emptyLines:
            raise TypeError
        # 1 is for the header
        
        self.Sets = {}

        print self.strDate
        #print self.listFile
        if self.numSets > 1:
            set1 = self.listFile[self._emptyLines[0]+1:self._emptyLines[1]]
        if self.numSets == 2:
            set2 = self.listFile[self._emptyLines[1]+1:self._emptyLines[2]]
            encore = self.listFile[self._emptyLines[2]+1]
        else:
            set2 = []

        if self.numSets == 3:
            set3 = self.listFile[self._emptyLines[2]+1:self._emptyLines[3]]
            encore = self.listFile[self._emptyLines[3]+1]
        
        
        try :
            print "set1: ",set1
            print "set2: ",set2
            print "set3: ",set3
        except: pass
        try:
            print "encore: ", encore
        except : pass
        
    def __repr__(self):
        return self.strDate
    
        
    
        


iF = r"E:\\dbGD\\01_dbGD\\72"
        
if __name__ == '__main__':
    thisYear = year(iF)
    thisYear.data[0]
    thisYear.parseShows()
    test = year.listObjShow[0].listFile
    tS = year.listObjShow[0]
