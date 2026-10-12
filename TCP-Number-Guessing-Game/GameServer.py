import socket
import random
import threading

def handle_client(connection, adr):
    realAnswer = random.randint(1, 100)
    print(f'Number to guess: {realAnswer}')

    try:
        while True:
            data = connection.recv(1024)
            if not data:
                print(f"Connection lost with {adr}")
                break

            try:
                guess = int(data.decode())  # تبدیل ورودی به عدد صحیح
            except ValueError:
                print(f"Invalid input from {adr}: Not a valid number.")
                connection.sendall(b"Invalid input. Please enter a number.")
                continue

            print('Received guess:', guess)

            if guess < realAnswer:
                response = 'Higher'
            elif guess > realAnswer:
                response = 'Lower'
            else:
                response = 'Correct'
                connection.sendall(response.encode())
                break

            connection.sendall(response.encode())

    except socket.timeout:
        print(f"Connection timeout with {adr}")
        connection.sendall(b"Connection timeout. Please try again later.")
    except socket.error as e:
        print(f"Network error: {e} with {adr}")
        connection.sendall(b"Network error occurred. Please try again later.")
    except Exception as e:
        print(f"Unexpected error: {e} with {adr}")
        connection.sendall(b"An unexpected error occurred.")
    finally:
        connection.close()
        print(f'Connection closed for {adr}')

host = '127.0.0.1'
port = 11111
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host, port))

serverSocket.listen(5)  # تعداد حداکثر کلاینت‌های قابل اتصال به سرور
print(f'Server is listening on {host}:{port}')

while True:
    connection, adr = serverSocket.accept()
    print('Connected by', adr)
    
    # برای هر کلاینت یک نخ جدید ایجاد می‌شود
    client_thread = threading.Thread(target=handle_client, args=(connection, adr))
    client_thread.start()
