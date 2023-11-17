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
    return os.path.join(letter_paths,letter_files[letter_idx])

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
    letter_path = map_letter_data(vowels, path, 1)
    all_data, fs = cargar_emg(letter_path)
    print(all_data)