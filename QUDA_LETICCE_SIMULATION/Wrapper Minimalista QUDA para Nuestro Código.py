# quda_wrapper.py
import ctypes
import numpy as np
from numpy.ctypeslib import ndpointer

class QudaGaugeField:
    """Interfaz Python para campos gauge de QUDA"""
    def __init__(self, U, beta):
        # U: array numpy [Lt, Lz, Ly, Lx, 4, 3, 3]
        self.U = U
        self.beta = beta
        self.dims = U.shape[:4]
        
        # Cargar librería QUDA
        self.quda = ctypes.CDLL('./quda/build/lib/libquda.so')
        
    def load_to_quda(self):
        """Envía configuración gauge a QUDA"""
        # Convertir a formato QUDA (array plano column-major)
        U_flat = self.U.flatten()
        
        # Crear campo gauge en QUDA
        self.quda.create_gauge_field.restype = ctypes.c_void_p
        self.gauge_ptr = self.quda.create_gauge_field(
            ctypes.c_void_p(U_flat.ctypes.data),
            ctypes.c_int(self.dims[3]),  # Lx
            ctypes.c_int(self.dims[2]),  # Ly
            ctypes.c_int(self.dims[1]),  # Lz
            ctypes.c_int(self.dims[0]),  # Lt
            ctypes.c_double(self.beta)
        )
    
    def measure_plaquette_quda(self):
        """Mide placa usando QUDA (más rápido)"""
        self.quda.measure_plaquette.restype = ctypes.c_double
        plaq = self.quda.measure_plaquette(self.gauge_ptr)
        return plaq
    
    def free(self):
        """Liberar memoria QUDA"""
        self.quda.free_gauge_field(self.gauge_ptr)

class BenchmarkManager:
    """Gestiona comparativas entre nuestro código y QUDA"""
    def __init__(self, U, phi, beta):
        self.U = U
        self.phi = phi
        self.beta = beta
        self.quda_field = QudaGaugeField(U, beta)
        
    def run_validation(self):
        """Ejecuta validación cruzada"""
        results = {}
        
        # 1. Plaquette
        plaq_our = self._plaquette_our_code()
        self.quda_field.load_to_quda()
        plaq_quda = self.quda_field.measure_plaquette_quda()
        
        results['plaquette_diff'] = abs(plaq_our - plaq_quda)
        results['plaquette_match'] = results['plaquette_diff'] < 1e-10
        
        # 2. Polyakov loop
        poly_our = self._polyakov_our_code()
        # poly_quda = self.quda_field.measure_polyakov_quda()
        
        # 3. Tiempos de ejecución
        import time
        start = time.time()
        for _ in range(10):
            self._plaquette_our_code()
        time_our = time.time() - start
        
        start = time.time()
        for _ in range(10):
            self.quda_field.measure_plaquette_quda()
        time_quda = time.time() - start
        
        results['speedup'] = time_our / time_quda
        
        return results
    
    def _plaquette_our_code(self):
        """Nuestra implementación de placa"""
        # Usa el código que ya tenemos
        plaq = 0.0
        for t in range(self.U.shape[0]):
            for z in range(self.U.shape[1]):
                for y in range(self.U.shape[2]):
                    for x in range(self.U.shape[3]):
                        for mu in range(4):
                            for nu in range(mu+1, 4):
                                # Calcular placa U_{μν}
                                U_plaq = self._plaquette((t,z,y,x), mu, nu)
                                plaq += np.real(np.trace(U_plaq))
        return plaq / (6 * np.prod(self.U.shape[:4]))