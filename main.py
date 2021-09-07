from classes.StringUtilsClass import StringUtils

if __name__ == '__main__':

    inputString = input("Write the main string :")
    strU = StringUtils(inputString)
    out = strU.msgOutput()
    
    print (out)