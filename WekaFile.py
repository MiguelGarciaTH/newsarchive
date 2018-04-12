class WekaFile(object):

    def __init__(self, filename, relation):
        self.filename = filename
        self.relation = relation
        self.file = open(filename+".arff", "w")

    def write_template(self):
        self.file.write("@RELATION " + self.relation+"\n\n@ATTRIBUTE id nominal\n@ATTRIBUTE text string\n@ATTRIBUTE class {E,D}\n\n\n@DATA\n\n")

    def write(self, id, text, classType):
        text=text.replace('\'','').replace('\n', '').replace('“','').replace('”',' ')
        self.file.write(str(id)+", '" + text + "', "+classType+"\n")
        
    def close(self):
        self.file.close()


