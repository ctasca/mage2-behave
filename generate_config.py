import os
import shutil
import configparser

# Specify source directory (where your .dist files are) and destination directory
source_dir = 'features/core_config/.dist'
dest_dir = 'features/core_config'

# Get list of .dist files
dist_files = [f for f in os.listdir(source_dir) if f.endswith('.dist')]

# Create destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Loop over each .dist file
for dist_file in dist_files:
    src_file = os.path.join(source_dir, dist_file)
    dest_file_name = os.path.splitext(dist_file)[0] + '.ini'
    dest_file = os.path.join(dest_dir, dest_file_name)

    # If the file doesn't exist in destination directory, copy it
    if not os.path.exists(dest_file):
        shutil.copy2(src_file, dest_file)
    else:
        # If the file does exist, merge variables

        # Parse source config file
        src_config = configparser.ConfigParser()
        src_config.read(src_file)

        # Parse destination config file
        dest_config = configparser.ConfigParser()
        dest_config.read(dest_file)

        # Iterate over each variable in source config file
        for section in src_config.sections():
            for key in src_config[section]:
                # If the variable isn't in the destination config file, prompt the user to set it
                if not dest_config.has_option(section, key):
                    print(f'Variable {key.upper()} in section {section} is not set.')
                    value = input('Please provide a value, or press enter to skip: ')
                    if value is None or value.strip() == '':
                        continue
                    dest_config.set(section, key, value)

        # Write updated config to destination file
        with open(dest_file, 'w') as configfile:
            dest_config.write(configfile)
