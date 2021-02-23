import pika, sys, os
from threading import Thread
# from mq import sender as mqSender

def receivequeue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    def callback(ch, method, properties, body):
        print("%r" % body.decode('utf-8'))

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)   

    print(' [*] Waiting for messages. To exit press CTRL+C')

    thread = Thread(target = channel.start_consuming)
    thread.start()


# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)