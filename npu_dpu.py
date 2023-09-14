import sys
import os
SAI_CODE_LOCATION = r'/home/ubuntuserver/dinesh/SAI/'


def get_header_files_paths():
    header_files = []
    for root, dirs, files in os.walk(SAI_CODE_LOCATION):
        for file in files:
            if 'experimental' in root:
                import pdb;pdb.set_trace()
            if file.endswith('.h'):
                header_files.append(os.path.join(root, file))
    return header_files

get_header_files_paths()