import pika
import json

def sendqueue(data):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='hello', durable=True)

    data = data['userId'] + " 님이 " + data['contentWriter']+" 님의 글에 댓글을 달았습니다."

    channel.basic_publish(exchange='', routing_key='hello', body=data)

    print(data)

    connection.close()


# import pika

# # 서버와 연결
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# # 연결된 서버 안에서 채널 생성
# channel = connection.channel()

# # 만들어진 채널 안에서 큐를 생성
# channel.queue_declare(queue = 'hello')

# for i in range(200):
#     channel.basic_publish(exchange='', routing_key='hello', body=str(i))
#     print(" # 메시지를 보냈습니다!" + str(i))

# # 서버와 연결 종료
# connection.close()