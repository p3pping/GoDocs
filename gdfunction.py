class gdfunction:
    def __init__(self, def_line, leading_comments):
        args_location = def_line.find("(")
        args_end_location = def_line.find(")")
        func_location = def_line.find("func")

        #isolate func name
        self._name = def_line[(func_location+len("func ")): args_location]

        #set public or private based on pythonic/gdscript naming convention
        self._public = True if self._name[0] != "_" else False

        #determine parameters
        if(args_location+1 == args_end_location):
            #no arguments
            self._args = None
        elif (def_line.find(",") == -1):
            #one arg
            self._args = []
            self._args.append(def_line[args_location+1:args_end_location])
        else:
            arg_list = def_line[args_location+1:args_end_location]
            self._args = arg_list.split(",")
            pass
        
        #process leading comments
        if(leading_comments != "" or leading_comments != None):
            desc_location = leading_comments.lower().find("description:")
            if(desc_location != -1):
                self._desc = leading_comments[desc_location+len("description:"):]
            else:
                self._desc = leading_comments
        else:
            self._desc = ""
            
    
    def get_name(self):
        return self._name
    
    def get_args(self):
        return self._args    

    def get_desc(self):
        return self._desc

    def is_public(self):
        return self._public

    def get_markup(self):
        markup = str("")
        markup += "<div>"
        markup += "<h4>Name:"+self._name+"</h4>"        
        markup += "<h5>Args: "
        if self._args == None:
            markup += "None"
        else:
            for arg in self._args:
                markup += arg+"&nbsp;"
        markup += "</h5>"
        markup += "<p>Description: "+self._desc+"</p>"
        markup += "</div>"
        return markup