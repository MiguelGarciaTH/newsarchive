class WekaFile(object):

    def __init__(self, filename, relation):
        self.filename= filename
        self.relation= relation
        self.file = open(filename+".arff", "w")

    def write_template(self):
        self.file.write("@RELATION " + self.relation+"\n@ATTRIBUTE id integer\n@ATTRIBUTE text string\n@ATTRIBUTE class {E,D}\n\n@DATA\n")

    def write(self, id, text, classType):
        self.file.write(str(id) + ", '" + str(text) + "', '"+classType+"'\n")

    def close(self):
        self.file.close()


