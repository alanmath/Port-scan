import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

# Mapeamento de portas conhecidas
well_known_ports = {
    21: 'FTP',
    22: 'SSH',
    23: 'Telnet',
    25: 'SMTP',
    53: 'DNS',
    80: 'HTTP',
    110: 'POP3',
    443: 'HTTPS',
}

# Função para escanear uma porta específica
def scan_port(ip, port, output_widget):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            service_name = well_known_ports.get(port, 'Desconhecido')
            output_widget.insert(tk.END, f"Porta {port} aberta ({service_name})\n")
        sock.close()
    except Exception as e:
        output_widget.insert(tk.END, f"Erro ao escanear porta {port}: {e}\n")

# Função para escanear um intervalo de portas utilizando threads
def scan_ports(ip, start_port, end_port, output_widget):
    output_widget.insert(tk.END, f"Escaneando {ip} de {start_port} a {end_port}...\n")
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port, output_widget))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    output_widget.insert(tk.END, "Escaneamento completo.\n")

# Função para iniciar o escaneamento em uma thread
def start_scan():
    host = ip_entry.get()
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        output_text.insert(tk.END, f"Erro: Nome do host inválido '{host}'\n")
        return
    
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    
    thread = threading.Thread(target=scan_ports, args=(ip, start_port, end_port, output_text))
    thread.start()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Escaneador de Portas TCP com Threads")

tk.Label(root, text="Nome do Host (ex: www.example.com):").grid(row=0, column=0)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1)

tk.Label(root, text="Porta Inicial:").grid(row=1, column=0)
start_port_entry = tk.Entry(root)
start_port_entry.grid(row=1, column=1)

tk.Label(root, text="Porta Final:").grid(row=2, column=0)
end_port_entry = tk.Entry(root)
end_port_entry.grid(row=2, column=1)

scan_button = tk.Button(root, text="Iniciar Escaneamento", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2)

output_text = scrolledtext.ScrolledText(root, width=50, height=20)
output_text.grid(row=4, column=0, columnspan=2)

root.mainloop()
