from datasets import load_dataset
dataset = load_dataset('json', data_files='my_file.json')
print(dataset)
