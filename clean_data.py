import os
 
def list_md_files(directory):
    return [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(directory)) for f in fn if f.endswith('.md')]
 
directory = '/Users/lixiaoyi/Desktop/word'
for md_file in list_md_files(directory):
    with open(md_file, 'r') as original_file, open('temp.txt', 'w') as new_file:
        next(original_file)
        next(original_file)
        for line in original_file:
            new_file.write(line)
        os.remove(md_file)
        os.rename('temp.txt', md_file)