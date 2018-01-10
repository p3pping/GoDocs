class gdclass:
    
    def __init__(self, filename):
        self._filename = filename
        self._public_vars = []
        self._private_vars = [] 
        self._public_funcs = []
        self._private_funcs = []
    
    def get_filename(self):
        return self._filename    

    def get_path(self):
        return self._filepath

    def set_path(self,path):
        self._filepath = path if self._filepath is None else self._filepath

    def add_variable(self, variable):
        if variable.is_public():
            self._public_vars.append(variable)
        else:
            self._private_vars.append(variable)

    def add_func(self, function):
        if function.is_public() :
            self._public_funcs.append(function)
        else:
            self._private_funcs.append(function)
    
    def get_markup(self):
        markup = str("<html><body>")
        markup += "<div>"
        markup += "<h1>Class: "+self._filename+"</h1>"
        markup += "<h2>Members:</h2>"

        markup += "<h3>Public: </h3>"
        for member in self._public_vars:
            markup += member.get_markup()

        markup += "<h3>Private </h3>"
        for member in self._private_vars:
            markup += member.get_markup()

        markup += "<h2>Functions:</h2>"

        markup += "<h3>Public: </h3>"
        for func in self._public_funcs:
            markup += func.get_markup()
        
        markup += "<h3>Private </h3>"
        for func in self._private_funcs:
            markup += func.get_markup()
        
        markup += "</body></html>"
        return markup
    
