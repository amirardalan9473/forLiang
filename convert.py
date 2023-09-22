import os
import numpy as np
import logging

# Configure logging
logging.basicConfig(filename='convert_hips_to_tensors.log', level=logging.INFO)

def extract_tensor_from_hips(file_path):
    try:
        # Insertion
        pass
    except Exception as e:
        logging.error(f'Error extracting tensor from {file_path}: {e}')
        return None

def save_tensor(tensor, save_path):
    try:
        np.save(save_path, tensor)
    except Exception as e:
        logging.error(f'Error saving tensor to {save_path}: {e}')

def convert_hips_to_tensors(root_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for foldername, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.hips'):
                file_path = os.path.join(foldername, filename)

                # Extract tensor from .hips file
                tensor = extract_tensor_from_hips(file_path)
                if tensor is None:
                    continue

                # Construct the output path
                relative_path = os.path.relpath(foldername, root_dir)
                save_folder = os.path.join(output_dir, relative_path)
                if not os.path.exists(save_folder):
                    os.makedirs(save_folder)
                save_path = os.path.join(save_folder, os.path.splitext(filename)[0] + '.npy')

                # Check if file already exists
                if os.path.exists(save_path):
                    logging.warning(f'File {save_path} already exists. Skipping...')
                    continue

                # Save the tensor
                save_tensor(tensor, save_path)
                logging.info(f'Saved tensor at {save_path}')

if __name__ == '__main__':
    root_dir = 'path_to_your_root_directory'
    output_dir = 'path_to_output_directory'
    convert_hips_to_tensors(root_dir, output_dir)
