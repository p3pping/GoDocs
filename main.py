import sys
import utils

def main():
    print("Started Running")

    working_dir = None

    #check if we have all arg directories to work with
    if len(sys.argv) == 1:
        print("Missing Argument - Project Directory\r\nexample: main.py C:\\project C:\\exports")
        return

    elif len(sys.argv) == 2:
        print("Missing Argument - Export Directory\r\nexample: main.py C:\\project C:\\exports")
        return
    
    working_dir = sys.argv[1]
    export_dir = sys.argv[2]

    print("Analyzing Directory: "+working_dir)

    #find all the scripts
    script_files = utils.discover_scripts_recur(working_dir)

    scripts = []
    #start processing each script
    for script in script_files:
        print("Processing Script: "+script)
        scripts.append(utils.process_script(script))
    

    #export
    utils.export_to_html(working_dir,export_dir, scripts)



#standard entry point
if __name__ == "__main__":
    main()