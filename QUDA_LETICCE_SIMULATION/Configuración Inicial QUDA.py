# install_quda.py
import subprocess
import os
import numpy as np

def setup_quda_environment():
    """Configura QUDA en Google Colab o entorno local"""
    
    # 1. Instalar dependencias
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'install', '-y', 
                   'build-essential', 'cmake', 'git',
                   'libopenmpi-dev', 'openmpi-bin'])
    
    # 2. Clonar QUDA
    if not os.path.exists('quda'):
        subprocess.run(['git', 'clone', 'https://github.com/lattice/quda.git'])
    
    # 3. Compilar para GPU (Colab tiene T4 GPU)
    os.chdir('quda')
    subprocess.run(['mkdir', '-p', 'build'])
    os.chdir('build')
    
    cmake_cmd = [
        'cmake', '..',
        '-DQUDA_GPU_ARCH=sm_75',  # T4 GPU
        '-DQUDA_DIRAC_WILSON=ON',
        '-DQUDA_FORCE_GAUGE=ON',
        '-DQUDA_BUILD_SHAREDLIB=ON'
    ]
    
    subprocess.run(cmake_cmd)
    subprocess.run(['make', '-j4'])
    
    return True

# Ejecutar solo una vez
# setup_quda_environment()