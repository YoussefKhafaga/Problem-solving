class Solution(object):
    def reformatDate(self, date):
        date = date.split()
        result = ""
        result += date[2]
        dict1 = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        result+="-"
        result+= dict1[date[1]]
        result += "-"
        day = ""
        for i in date[0]:
            try:
                int(i)
                day+=str(i)
            except:
                break
        return result+"{:02d}".format(int(day))