import os
import argparse
import numpy as np
import pandas as pd

parser = argparse.ArgumentParser(description = 'Train Data info')
parser.add_argument('--path', default = "data/all_in")
parser.add_argument('--split_percent', default = 0.25)
args = parser.parse_args()

np.random.seed(0)

datapath = os.path.join(args.path, "images")
folders_paths = [ folder_name
	for folder_name in os.listdir(datapath)
	if os.path.isdir(os.path.join(datapath, folder_name))]

np.random.shuffle(folders_paths)

data = []
image_id = 1
class_id = 1
for folder_path in folders_paths:
	
	imgs_paths = os.listdir(os.path.join(datapath, folder_path))
	imgs_paths = [ os.path.join("images", folder_path, img_name) 
	for img_name in os.listdir(os.path.join(datapath, folder_path))]

	if len(imgs_paths) > 2:

		for img_path in imgs_paths:
			data.append([image_id, class_id, 1, img_path])
			image_id += 1
		
		class_id += 1

	


data = pd.DataFrame(data, columns=['image_id', 'class_id', 'super_class_id', 'path'])
split_percent = float(args.split_percent)
split_point = int(class_id * ( 1 - split_percent))


train_data = data.loc[data['class_id'] <= split_point]
test_data = data.loc[data['class_id'] > split_point]


train_data.to_csv(os.path.join(args.path, "train.txt"), index=None, sep = ' ')
test_data.to_csv(os.path.join(args.path, "test.txt"), index=None, sep = ' ')
