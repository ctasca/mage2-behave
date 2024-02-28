import os
from dist_file_processor import process_dist_file

# Specify source directory (where your .dist files are) and destination directory
root_dir = os.getcwd()

# Get list of .dist files
dist_files = [f for f in os.listdir(root_dir) if f.endswith('.dist')]
template_files = [f for f in os.listdir(root_dir) if f.endswith('.template')]


# Loop over each .dist file
for dist_file in dist_files:
    src_file = os.path.join(root_dir, dist_file)
    dest_file_name = os.path.splitext(dist_file)[0]
    process_dist_file(root_dir, root_dir, src_file, dest_file_name)
