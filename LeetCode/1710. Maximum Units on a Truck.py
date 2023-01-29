class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        
        sum = 0
        boxesno = []
        unitsperboxes = []
        for box in boxTypes:
            boxesno.append(box[0])
            unitsperboxes.append(box[1])
        boxTypes = None
        del boxTypes
        
        while truckSize > 0:
            #print(boxesno, unitsperboxes, truckSize, sum)
            if len(boxesno) == 0:
                break
                
            maxval = max(unitsperboxes)
            index = unitsperboxes.index(maxval)
            if truckSize <= boxesno[index]:
                sum += maxval*truckSize
                truckSize = 0
            else:
                sum += maxval * boxesno[index]
                truckSize -= boxesno[index]
                boxesno[index] = 0
            if boxesno[index] == 0:
                boxesno.remove(boxesno[index])
                unitsperboxes.remove(unitsperboxes[index])
        return sum
        