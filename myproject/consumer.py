import pika,json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from webapp.models import Product
#params=pika.URLParameters('http://adpubwco:5MlpDbbndBbZWMKZoMKNfuNMTvTBBSic@beaver.rmq.cloudamqp.com/adpubwco')
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost',heartbeat=600,blocked_connection_timeout=300))
channel=connection.channel()


channel.queue_declare(queue='admin')

def callback(ch,method,properties,body):
    print("[x] Received in main")

    data=json.loads(body)
    print(data)
    product=Product.objects.get(id=data)
    print(product.likes)
    product.likes=product.likes+1
    print(product.likes)
    product.save()
    print('product likes increased')

channel.basic_consume(queue='admin',auto_ack=True,on_message_callback=callback)
print('started Consuming')

channel.start_consuming()



