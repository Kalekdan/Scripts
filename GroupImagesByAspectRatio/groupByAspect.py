import os
from PIL import Image
import math
import shutil

# Processes all files in the current directory and copies them into a directory under "_AspectRatios" named with the ratio of all images inside

count = 0
errCount = 0
errFiles = []

root_dir = '.'
aspects_dir = "_AspectRatios"

for directory, subdirectories, files in os.walk(root_dir):
	for file in files:
		#dont process this script or aspects_dir
		if (file == os.path.basename(__file__)) or (subdirectories == aspects_dir):
			continue
		try:
			#open image and calculate ratio
			im = Image.open(os.path.join(directory, file))
			width, height = im.size
			gcd = math.gcd(width, height)
			ratio = str(int(width / gcd)) + "-" + str(int(height/gcd))
			
			#copy file to directory
			srcPath = os.path.join(directory, file)
			destPath = aspects_dir + "/" + ratio
			print(srcPath + " - " + str(width) + "x" + str(height) + " - " + ratio)
			print(destPath)
			os.makedirs(destPath, exist_ok=True)
			shutil.copy(os.path.join(directory, file), destPath)
			
			im.close()
		except:
			errCount = errCount + 1
			errFiles.append(os.path.join(directory, file))
		count = count + 1


print("\n" + str(count) + " files processed")
print(str(errCount) + " errors " + str(errFiles))
