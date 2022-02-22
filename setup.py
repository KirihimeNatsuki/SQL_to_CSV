from cx_Freeze import setup, Executable
  
executables = [
        Executable(script = "SQL_to_CSV.py")
]
  
buildOptions = dict( 
        includes = ["re","shutil","numpy","sys","io","calendar","time","datetime"],
        excludes = ["tkinter"],
)
  
setup(
    name = "SQL_to_CSV",
    version = "1.0",
    description = "Script de conversion de fichier SQL en CSV",
    author = "Enzo Lemarchand",
    options = dict(build_exe = buildOptions),
    executables = executables
)