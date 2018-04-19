
from string import digits

class WekaFile(object):

    def __init__(self, filename, relation):
        self.filename = filename
        self.relation = relation
        self.file = open(filename+".arff", "w")

    def write_template(self):
        self.file.write("@RELATION " + self.relation+"\n\n@ATTRIBUTE id string\n@ATTRIBUTE text string\n@ATTRIBUTE class {E,D}\n\n\n@DATA\n\n")

    def write(self, id, text, classType):
        text = text.replace('\'',' ').replace('\t','').replace('\n','').replace('  ', '').replace('“',' ').replace('”',' ').replace('"', ' ').replace('  ', ' ')
        text= text.replace(' ',' ')
        remove_digits = str.maketrans('', '', digits)
        text = text.translate(remove_digits)
        text=' '.join(text.split())
        self.file.write(str(id)+", '" + text+ "', "+classType+"\n")

    def close(self):
        self.file.close()


