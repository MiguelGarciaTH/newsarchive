from WekaFile import WekaFile

weka= WekaFile("teste","test")
weka.write_template()
weka.write(0,"teste teste","R")
weka.close()
