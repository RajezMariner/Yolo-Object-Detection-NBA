import glob

f = glob.glob('data/**txt')

f

labels = {'15': '0', '16': '1', '17': '2' }

for i in range(len(f)):
    with open(f[i], 'r') as fr:
        annotation_params = fr.readlines()
        fr.close()

    with open(f[i], 'w') as fw:
        print(annotation_params)
        index = annotation_params[0].split(' ')[0]
        updated_val = annotation_params[0].replace(index, labels[index], 1)
        fw.write(updated_val)

