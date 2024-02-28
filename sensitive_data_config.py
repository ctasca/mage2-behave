import os
from dist_file_processor import process_dist_file

root_dir = os.getcwd()

dist_files = [f for f in os.listdir(root_dir) if f.endswith('.dist')]
template_files = [f for f in os.listdir(root_dir) if f.endswith('.template')]

for dist_file in dist_files:
    src_file = os.path.join(root_dir, dist_file)
    dest_file_name = os.path.splitext(dist_file)[0]
    process_dist_file(root_dir, root_dir, src_file, dest_file_name)
