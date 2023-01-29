class Solution(object):
    def destCity(self, paths):
        dict1 = {}
        for trip in paths:
            for city in trip:
                if city in dict1.keys():
                    dict1[city] = dict1[city] + 1
                else:
                    if city == trip[1]:
                        dict1[city] = 1
                    else:
                        dict1[city] = 2
        return min(dict1, key=dict1.get)
                
        