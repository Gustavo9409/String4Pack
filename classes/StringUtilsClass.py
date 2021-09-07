import collections

class StringUtils:

    def __init__(self, mainString='It is a main string'):
        self.mainString = mainString
        self.nCharacters = 4

    # This function create an array of subtrings with nCharacters
    # Description: In each iteration of the loop a temporal variable
    #              store one character of the main string and when it
    #              check the condition of nCharacters delete the ferst item
    #              in the temporal variable, add a new one and store it in
    #              an array.
    # self: The self parameter is a reference to the current instance of the class.
    # Returns an array of strings
    def makeArray(self):
        temp_str = ""
        dataArr = []
        for element in self.mainString:
            if len(temp_str) == self.nCharacters:
                 dataArr.append(temp_str)
                 temp_str = temp_str[1:]
            else:
                temp_str += element
                if len(temp_str) == self.nCharacters:
                    dataArr.append(temp_str)
                    temp_str = temp_str[1:]
            
        return dataArr
 
    # This function evaluate throught an array of substrings how many times exist each item 
    # and if there are repetead values.
    # self: The self parameter is a reference to the current instance of the class.
    # Returns an array of dicts   
    def stringInfo(self):
        data = self.makeArray()
        output = []
        
        # Code of StackOverFlow Answer
        # https://stackoverflow.com/a/9835819
        ## ---------------------------------------- ##
        seen = {}
        dupes = []
        for x in data:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1
        ## ---------------------------------------- ##
        
        for val in dupes:
            output.append({ 'Substring' : val,
                            'Num_appearances' : seen[val] 
                          })

        return output
    
    # This create a message to the user showing the response.
    # self: The self parameter is a reference to the current instance of the class.
    # Returns a string message
    def msgOutput(self):
        dictOut = self.stringInfo()
        msg = ""
        if len(dictOut) > 0:
            msg += "\n"
            msg += "############## INFO IN A DATA STRUCTURE (DICTIONARIES) ##############"
            msg += "\n"
            for item in dictOut:
                msg += str(item)
                msg += "\n"
            msg += "#####################################################"
            msg += "\n"
        else:
            msg += "############## THERE ARE NOT SUBSTRINGS REPEATED ##############"
            
        return msg