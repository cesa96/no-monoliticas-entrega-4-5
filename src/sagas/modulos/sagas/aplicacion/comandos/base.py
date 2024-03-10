from sagas.seedwork.aplicacion.comandos import ComandoHandler
from sagas.modulos.sagas.infraestructura.fabricas import FabricaRepositorio
from sagas.modulos.sagas.dominio.fabricas import Fabricasagas

class CrearSagaBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_sagas: Fabricasagas = Fabricasagas()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_sagas(self):
        return self._fabrica_sagas    
    