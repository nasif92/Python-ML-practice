from cx_Freeze import setup, Executable

base = None    

executables = [Executable("pygame_stuff.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Meta",
    options = options,
    version = "0.001",
    description = 'Meta',
    executables = executables
)