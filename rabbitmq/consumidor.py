import pika

# Establecer la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola desde la que se recibirán los mensajes
channel.queue_declare(queue='ejemplo')

# Definir la función de callback para procesar los mensajes recibidos
def callback(ch, method, properties, body):
    print(" [x] Recibido %r" % body)

# Suscribir la función de callback a la cola
channel.basic_consume(queue='ejemplo', on_message_callback=callback, auto_ack=True)

# Comenzar a recibir mensajes
print(' [*] Esperando mensajes. Presione CTRL+C para salir.')
channel.start_consuming()
