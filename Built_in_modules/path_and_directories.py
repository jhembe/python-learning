from pathlib import Path

# #NOTE there are two basic ways to do this:
# #Absolute Path  -- This starts from the the root of the hard drives to the required files
# #Relative Path  -- This starts from the current directory towards the required files

# #NOTE we  can check if the path exists by using the .exists() method
# path = Path("ecommerce")
# print(path.exists())

# #NOTE we can also create a new directory by using the finction .mkdir()
# path1 = Path("test")
# path1.mkdir()

# #NOTE we can remove the directory by using the function .rmdir()
# path2 = Path("email")
# path2.rmdir()
# print(path2.exists())

#NOTE we can also use this module to display files..
path_global = Path()
path_global.glob("*.*") # this is the generator object. For us to vissualise we need to itterate using a loop

for python_file in path_global.glob("*.*"):
    print(python_file)