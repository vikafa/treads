import socket
Создаем сокет для клиента
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9090))  # Подключаемся к серверу

while True:
# Получаем сообщение от пользователя
     message = input("Введите сообщение (или 'quit' для выхода): ")
     if message.lower() == 'quit':
         break
# Отправляем сообщение серверу
     client_socket.send(message.encode())
# Получаем ответ от сервера
     response = client_socket.recv(1024)
     print(f"Ответ сервера: {response.decode()}")

#Закрываем соединение с сервером
client_socket.close()