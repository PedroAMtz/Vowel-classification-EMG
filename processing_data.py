import os
import pandas as pd 
import numpy as np
import json

path = 'Dataset/'
vowels = ['A','E','I','O','U']

def map_letter_data(letters, dataset_path, letter_idx):
    letter_paths = os.path.join(dataset_path, letters[letter_idx])
    letter_files = os.listdir(letter_paths)
    print(f"Reading files from letter: {letters[letter_idx]}")
    return letter_files

def cargar_emg(emg_path):
    try:
        with open(emg_path, 'r') as file:
            sign_data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"El archivo {emg_path} no se encontró.")

    imu_data = pd.DataFrame(sign_data.get('imu', {}).get('data', []))
    g_xyz = pd.DataFrame(imu_data.get('gyroscope', []).tolist(), columns=['gx', 'gy', 'gz'])
    a_xyz = pd.DataFrame(imu_data.get('acceleration', []).tolist(), columns=['ax', 'ay', 'az'])

    emg_data = pd.DataFrame(sign_data.get('emg', {}).get('data', []),
                             columns=['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8'])

    all_data = pd.concat([emg_data, g_xyz, a_xyz], axis=1)

    fs = sign_data.get('emg', {}).get('frequency', None)

    if fs is None:
        raise ValueError("Frecuencia no encontrada en los datos EMG.")
    return all_data, fs

if __name__ == "__main__":

    features = []
    labels = []

    # Reading all features from EMG signals from all vowels
    for idx, vowel in enumerate(vowels):
        letter_files= map_letter_data(vowels, path, idx)
        letter_paths = os.path.join(path,vowel)
        
        for letter_file in letter_files:
            all_data, fs = cargar_emg(os.path.join(letter_paths,letter_file))
            features.append(all_data)
            labels.append(vowel)
    
    X_data = np.array(features)
    X_data = X_data.reshape(X_data.shape[0], -1)
    print('X_data: ',X_data.shape)

    Y_data = np.array(labels)
    print('Y_data: ',Y_data.shape)

    all_data_dir = "./training_data"
    if not os.path.exists(all_data_dir):
        os.makedirs(all_data_dir)
        print("Succesfully created training data directory!")
    
    with open(f'{all_data_dir}/train.npy', 'wb') as f:
            np.save(f, X_data)
            np.save(f, Y_data)
    print(X_data.shape, Y_data.shape)
    print("Succesfully saved training data!")