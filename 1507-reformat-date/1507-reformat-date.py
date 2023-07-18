class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        
        date = list(date.split(" "))
        formattedDate = []
        
        if month.index(date[1])+1 < 10:
            mon = "0"+str(month.index(date[1])+1)
        else:
            mon = str(month.index(date[1])+1)
            
        if int(date[0][0:len(date[0])-2]) < 10:
            day = "0" + date[0][0:len(date[0])-2]
        else:
            day = date[0][0:len(date[0])-2]
            
        formattedDate.append(date[2])
        formattedDate.append(mon)
        formattedDate.append(day)
        
        return "-".join(formattedDate)
        