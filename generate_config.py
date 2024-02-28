import os
from utils.dist_file_processor import process_dist_file

source_dir = 'features/core_config/.dist'
dest_dir = 'features/core_config'

dist_files = [f for f in os.listdir(source_dir) if f.endswith('.dist')]
template_files = [f for f in os.listdir(source_dir) if f.endswith('.template')]

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for dist_file in dist_files:
    src_file = os.path.join(source_dir, dist_file)
    dest_file_name = os.path.splitext(dist_file)[0] + '.ini'
    process_dist_file(source_dir, dest_dir, src_file, dest_file_name)
