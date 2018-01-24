import os
import gdclass
import gdvariable
import gdfunction
from constants import constants
from string import Template
from shutil import copyfile

def get_template(template):
    content = ""
    with open(template, "r") as f:
        content = f.read()
    f.close()

    return content

#searches directory recursively for gd scripts and returns a list of all gd scripts
def discover_scripts_recur(dir_path):
    file_list = []
    full_path = dir_path+"\\"    

    for item in os.listdir(str(full_path)):
        current = full_path+item

        #append files and delve into directories
        if(os.path.isfile(current)):
            if(is_gdscript(item)):
                file_list.append(current)
        elif(os.path.isdir(current)):
            file_list.extend(discover_scripts_recur(current))

    return file_list

#checks the files extension to see if its a gd script and return true if it is
def is_gdscript(filepath):
    return True if filepath[-3:] == ".gd" else False

def process_script(filepath):
    
    #all gdscript files are classes
    current_class = gdclass.gdclass(filepath)

    with open(filepath, "r") as f:
        
        line = f.readline()
        comment_buffer = "" #comment storage for description finding

        #read the file line by line
        while line != "":
            

            #if our line is not blank skip it
            if line[0] == "\n" or line[0] == "\r":
                line = f.readline()
                continue

            #find our indentation level
            indent_level = 0
            for char in line:
                if char == "\t" or char == "   ":
                    indent_level += 1
                else:                    
                    break
            
            #at the moment we will just deal with immediate declarations of variables and funcs for a class
            #if the indent level is more than 1 that indicates we are in a function or sub class and we can skip it
            if indent_level > 1:
                comment_buffer = ""
                line = f.readline()
                continue
                        
            if line[0] == "#":
                #add our comment to our buffer
                comment_buffer += line.replace("#", " ")
                pass
            elif line.find("var") != -1:                               
                #add a variable to our current class
                new_variable = gdvariable.gdvariable(line, comment_buffer)
                current_class.add_variable(new_variable)

                comment_buffer = "" #clear the buffer
            elif line.find("func") != -1:
                #add a func to our current class
                new_func = gdfunction.gdfunction(line, comment_buffer)
                current_class.add_func(new_func)

                comment_buffer = ""
            
            line = f.readline()
    f.close()

    return current_class

def export_to_html(project_dir, export_dir, scripts):
        #append \ to our dirs if it doesnt already have it
        working_dir = export_dir if export_dir[-1:] == "\\" else export_dir+"\\"
        relative_path = project_dir if project_dir[-1:] == "\\" else project_dir+"\\"

        #make sure our export directory exists
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        #begin our crude menu html doc
        menu_template = Template(get_template(constants.MENU_TEMPLATE_FILE))        
        menu_list = ""

        

        fnames = {}

        #add each scripts markup
        for script in scripts:
            
            #workout filename
            full_path = script.get_filename()
            cur_rel_parth = full_path[len(relative_path):] #get the project relative path

            fname_parts = full_path.split("\\")
            fname = fname_parts[len(fname_parts)-1].split(".")[0]

            #check for duplicate file names
            #increment the index number if it exists and add it to the filename
            if(fname in fnames):
                fnames[fname] += 1
                fname += str(fnames[fname])
            else:
                fnames[fname] = 0
            
            #add file extension for html and add to the menu
            fname = fname+".html"
            menu_list += "<li><a href=\""+fname+"\">"+cur_rel_parth+"</a></li>"

            #generate the markup            
            export_markup = script.get_markup()

            #save the class documentation            
            with open(working_dir+fname, "w") as script_file:
                script_file.write(export_markup)
            script_file.close()     
        
        #compile index html doc
        index_html = menu_template.substitute(project_name="", menu=menu_list)
        
        #write the doc to the file
        with open(working_dir+"index.html", "w") as f:
            f.write(index_html)
        f.close()

        #copy css
        if not os.path.exists(working_dir+"css"):
            os.makedirs(working_dir+"css")
        copyfile(constants.CSS_TEMPLATE_FILE, working_dir+"css\\style.css")

