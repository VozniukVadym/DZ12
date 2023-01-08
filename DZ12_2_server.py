import socket
import asyncio
                                            #Налаштування сервера
new_socket = socket.socket()

new_socket.bind(('127.0.0.1', 55000))

name = 'Server'

new_socket.listen(1)

conn, add = new_socket.accept()

client = (conn.recv(1024)).decode()

conn.send(name.encode())
x=0
y=0
fl=1
                              #Сервер приймає по черзі два числа х та у та виходить з безкінечного циклу
while True:
    print (x, y)
    message = conn.recv(1024)
    message = message.decode()
    if fl==1:
        x=int(message)
        fl=0
    elif fl==0:
        y=int(message)
        fl=2
    else:
        break
                                #  асинхронні функції
async def suma(x,y)
    z=x+y
    await asyncio.sleep(0)

async def rizn(x,y)
    z=x-y
    await asyncio.sleep(0)
async def dobutok(x,y)
    z=x*y
    await asyncio.sleep(0)
                                    #запускаєм функції
ioloop = asyncio.get_event_loop()
tasks=[ioloop.create_task(suma()),ioloop.create_task(rizn()),ioloop.create_task(dobutok())]
wait_task=asyncio.wait(tasks)
ioloop.run_until_complete(wait_task)
ioloop.close()
