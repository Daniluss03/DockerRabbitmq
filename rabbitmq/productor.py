import pika

# Establecer la conexión con el servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declarar la cola a la que se enviarán los mensajes
channel.queue_declare(queue='ejemplo')

# Enviar un mensaje
channel.basic_publish(exchange='', routing_key='ejemplo', body='Hola, mundo!')
print(" [x] Enviado 'Hola, mundo!'")

# Cerrar la conexión
connection.close()
