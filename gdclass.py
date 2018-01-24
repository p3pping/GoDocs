import os
import utils
from constants import constants
from string import Template

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

        class_temp = Template(utils.get_template(constants.CLASS_TEMPLATE_FILE))
        
        pub_mems = ""
        pub_mems_brief = ""
        for member in self._public_vars:
            pub_mems += member.get_full_markup()
            pub_mems_brief += member.get_brief_markup()

        pub_funcs = ""
        pub_funcs_brief = ""
        for func in self._public_funcs:
            pub_funcs += func.get_full_markup()
            pub_funcs_brief += func.get_brief_markup()
        
        markup = class_temp.substitute(title=self._filename, name=self._filename, public_members=pub_mems_brief, public_funcs=pub_funcs_brief, full_mem_markup=pub_mems, full_func_markup=pub_funcs)
        return markup
    
