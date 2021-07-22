#http://adpubwco:5MlpDbbndBbZWMKZoMKNfuNMTvTBBSic@beaver.rmq.cloudamqp.com/adpubwco

import pika,json
params=pika.URLParameters('http://adpubwco:5MlpDbbndBbZWMKZoMKNfuNMTvTBBSic@beaver.rmq.cloudamqp.com/adpubwco')
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost',heartbeat=600,blocked_connection_timeout=300))
channel=connection.channel()
channel.queue_declare(queue='service')
def publish(method,body):
    properties=pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='service',body=json.dumps(body),properties=properties)

    # channel.basic_publish(exchange='', routing_key='service', body='Hello World!')
print("[x] Sent 'hello world'")



'''

import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='service')

channel.basic_publish(exchange='', routing_key='service', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()'''

