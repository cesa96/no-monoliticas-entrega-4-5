from sagas.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from sagas.seedwork.aplicacion.comandos import Comando
from sagas.seedwork.dominio.eventos import EventoDominio

from sagas.modulos.sagas.aplicacion.comandos.saga import RegistrarUsuario, ValidarUsuario
from sagas.modulos.sagas.aplicacion.comandos.pagos import PagarReserva, RevertirPago
from sagas.modulos.sagas.aplicacion.comandos.gds import ConfirmarReserva, RevertirConfirmacion
from sagas.modulos.sagas.dominio.eventos.pagos import ReservaPagada, PagoRevertido
from sagas.modulos.sagas.dominio.eventos.gds import ReservaGDSConfirmada, ConfirmacionGDSRevertida, ConfirmacionFallida


class CoordinadorReservas(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=CrearPropiedad, evento=PropiedadCreada, error=CrearPropiedadFallida, compensacion=CancelarReserva),
            Transaccion(index=2, comando=CrearInquilino, evento=InquilinoCreado, error=CrearInquilinoFallido, compensacion=RevertirPago),
            Transaccion(index=3, comando=AsociarPropiedad, evento=PropiedadAsociada, error=AsociarPropiedadFallida, compensacion=ConfirmacionGDSRevertida),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
