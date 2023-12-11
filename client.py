import socket
import tkinter as tk


def send_command():
    user_command = entry.get()
    try:
        client_socket.sendto(user_command.encode('utf-8'), server_address)
        print("Done!")
    except Exception as e:
        print(f"Помилка відправки команди: {e}")


def main():
    global client_socket, server_address, entry

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 3306)

    root = tk.Tk()
    root.title("Кліент")

    canvas = tk.Canvas(root, width=700, height=10)
    canvas.pack()

    entry = tk.Entry(root, width=100)
    entry.pack()

    send_button = tk.Button(root, text="Send Command", command=send_command)
    send_button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
