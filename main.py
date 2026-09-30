"""
Colegio Las Américas - Feria Científica (9no Grado)
Proyecto: Barco Robot
Integrantes: Gisselle Aguilar, Arianna de León, Evelyn Aguilar, 
             Angie Méndez, Carlos Samayoa, Dafne Estefanía
"""

class MotorReductor:
    """Clase que representa cada uno de los motores amarillos de 50 RPM."""
    def __init__(self, posicion: str, pin_pwm: int):
        self.posicion = posicion
        self.pin_pwm = pin_pwm
        self.rpm = 0

    def ajustar_velocidad(self, velocidad_rpm: int):
        self.rpm = velocidad_rpm
        print(f"⚙️ Motor {self.posicion} (Pin {self.pin_pwm}): operando a {self.rpm} RPM.")


class ModuloBluetoothHC05:
    """Clase para simular la conexión inalámbrica Bluetooth."""
    def __init__(self, nombre_dispositivo: str = "BarcoRobot_9noB"):
        self.nombre = nombre_dispositivo
        self.conectado = True

    def recibir_instruccion(self, comando: str) -> str:
        print(f"\n📡 Bluetooth [{self.nombre}] recibió instrucción: '{comando}'")
        return comando.upper()


class ControlBarcoRobot:
    """Clase principal que integra la electrónica del Barco Robot."""
    def __init__(self):
        self.motor_izquierdo = MotorReductor("Izquierdo", pin_pwm=5)
        self.motor_derecho = MotorReductor("Derecho", pin_pwm=6)
        self.bluetooth = ModuloBluetoothHC05()
        self.flotando = True

    def procesar_navegacion(self, comando: str):
        instruccion = self.bluetooth.recibir_instruccion(comando)
        
        if instruccion == "ADELANTE":
            print("🌊 Impulsando barco hacia adelante (Tercera Ley de Newton)")
            self.motor_izquierdo.ajustar_velocidad(50)
            self.motor_derecho.ajustar_velocidad(50)
        elif instruccion == "IZQUIERDA":
            print("🔄 Giro diferencial: Desactivando motor izquierdo")
            self.motor_izquierdo.ajustar_velocidad(0)
            self.motor_derecho.ajustar_velocidad(50)
        elif instruccion == "DERECHA":
            print("🔄 Giro diferencial: Desactivando motor derecho")
            self.motor_izquierdo.ajustar_velocidad(50)
            self.motor_derecho.ajustar_velocidad(0)
        elif instruccion == "PARAR":
            print("🛑 Deteniendo propulsión de hélices")
            self.motor_izquierdo.ajustar_velocidad(0)
            self.motor_derecho.ajustar_velocidad(0)
        else:
            print("⚠️ Comando no reconocido.")


if __name__ == "__main__":
    barco = ControlBarcoRobot()
    print("=== SIMULACIÓN EN CONSOLA: BARCO ROBOT 9NO GRADO ===")
    
    # Pruebas de navegación
    barco.procesar_navegacion("ADELANTE")
    barco.procesar_navegacion("IZQUIERDA")
    barco.procesar_navegacion("PARAR")