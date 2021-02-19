import os 
import re
  
def main(): 
	for count, dirname in enumerate(os.listdir()): 
		if not os.path.isdir(dirname):
			continue
		if os.path.isfile(dirname+"\\folder.jpg"):
			continue
		if os.path.isfile(dirname+"\\cover.jpg"):
			continue
		if os.path.isfile(dirname+"\\folder.png"):
			continue
		if os.path.isfile(dirname+"\\cover.png"):
			continue

		print(dirname)



if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
