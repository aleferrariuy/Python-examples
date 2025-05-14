import paho.mqtt.client as mqtt # protocolo de conexión con PLC
from datosSecretos import *

cliente = mqtt.Client(protocol=mqtt.MQTTv5)
cliente.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
cliente.username_pw_set(usuario, contraseña)
cliente.connect(servidor,puerto)

cliente.publish("sensor",valor)
