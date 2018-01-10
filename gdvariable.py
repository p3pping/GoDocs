class gdvariable:
    
    def __init__(self, code, leading_comments):
        assign_location = code.find("=")
        var_location = code.find("var")

        #isolate variable name
        self._name = code[(var_location+len("var ")) if var_location != -1 else 0: assign_location if assign_location != -1 else len(code)]

        #set public or private based on pythonic/gdscript naming convention
        self._public = True if self._name[0] != "_" else False

        #determine if its an export
        self._is_export = True if code.find("export") != -1 else False       

        #any trailing comments on the same line will become the description
        #other wise search the leading comments for a description and use that
        self._desc = ""
        comment_location = code.find("#")
        if(comment_location != -1):
            self._desc = code[comment_location+1:]
        else:
            #process leading comments
            if(leading_comments != "" or leading_comments != None):
                desc_location = leading_comments.lower().find("description:")
                if(desc_location != -1):
                    self._desc = leading_comments[desc_location+len("description:"):]
                else:
                    self._desc = leading_comments
            else:
                elf._desc = ""
    
    def get_name(self):
        return self._name
    
    def is_export(self):
        return self._is_export    
    
    def is_public(self):
        return self._public

    def get_desc(self):
        return self._desc

    def set_desc(desc):
        self._desc = desc
    
    def concat_desc(desc):
        self._desc += desc  
    
    def get_markup(self):
        markup = str("")
        markup += "<div>"
        markup += "<h4>Name:"+self._name+" "+("(EXPORT)" if self._is_export else "")+"</h4>"        
        markup += "<p>Description: "+self._desc+"</p>"
        markup += "</div>"
        return markup