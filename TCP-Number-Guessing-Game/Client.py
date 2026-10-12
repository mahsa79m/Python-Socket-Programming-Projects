import socket

host = '127.0.0.1'
port = 11111

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.settimeout(10)  # تنظیم تایم‌اوت

def connect_to_server():
    try:
        clientSocket.connect((host, port))
        print("Connected to the server!")
    except socket.timeout:
        print("Connection timed out. Please try again later.")
        clientSocket.close()
        exit(1)
    except Exception as e:
        print(f"Error connecting to server: {e}")
        clientSocket.close()
        exit(1)

def send_guess():
    while True:
        guess = input('Enter your guess: ')
        
        # اعتبارسنجی ورودی
        if not guess.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        # ارسال داده به سرور
        clientSocket.sendall(guess.encode())
        
        # دریافت پاسخ از سرور
        try:
            data = clientSocket.recv(1024)
            if not data:
                print("No response from server.")
                break
            response = data.decode()
            print('Server response:', response)

            if response == 'Correct':
                print("You guessed the correct number!")
                break
        except socket.error as e:
            print(f"Network error: {e}")
            break

def main():
    connect_to_server()
    send_guess()

    clientSocket.close()
    print('Connection closed')

if __name__ == "__main__":
    main()
