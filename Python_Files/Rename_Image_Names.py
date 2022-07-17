# import os
# for dirname in os.listdir(".\\Images\\Joe_Bidden"):
#     if os.path.isdir(dirname):
#         for i, filename in enumerate(os.listdir(dirname)):
#             print(filename)
#             os.rename(dirname + "/" + filename, dirname + "/" + "Joe_Biden_" + ".jpg")


import os
# Function to rename multiple files
def main():
   i = 0
   path="C:\\Users\\Murli's Lappy\\Documents\\Jupyter\\Project_2\\Images\\Ivan_Duque_Marquez\\"
   for filename in os.listdir(path):
      my_dest ="Ivan_Duque_Marquez_" + str(i) + ".jpg"
      my_source =path + filename
      my_dest =path + my_dest
      # rename() function will
      # rename all the files
      os.rename(my_source, my_dest)
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()