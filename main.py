from classes.StringUtilsClass import StringUtils

if __name__ == '__main__':

    #Take the input
    inputString = input("Write the main string :")
    
    #Initialization of class with main parameter
    strU = StringUtils(inputString)
    
    #Call of the class function
    out = strU.msgOutput()
    
    #Print the result in command line
    print (out)