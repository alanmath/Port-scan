# Port-scan

Port-Scan é uma ferramenta simples de escaneamento de portas TCP desenvolvida em Python. Esta aplicação permite que você escaneie um intervalo de portas em um endereço IP ou nome de host (site) especificado, identificando quais portas estão abertas e os serviços conhecidos associados a elas. A aplicação possui uma interface gráfica amigável usando `tkinter`.

## Funcionalidades

- **Escaneamento de portas TCP:** Identifica portas abertas em um endereço IP ou host especificado.
- **Interface gráfica amigável:** Desenvolvido com `tkinter` para facilitar o uso.
- **Resolução de nomes de host:** Converte automaticamente nomes de host (ex: `www.example.com`) para endereços IP.
- **Serviços conhecidos:** Lista serviços associados a portas conhecidas, como HTTP, FTP, SSH, etc.
- **Multithreading:** Utiliza threads para acelerar o escaneamento de portas, tornando o processo mais eficiente.

## Requisitos

- Python 3.x
- Bibliotecas padrão do Python (`socket`, `threading`, `tkinter`)

## Como Usar

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/port-scan.git
   cd port-scan
  ``

2. **Interface Gráfica:**
   
    ![image](https://github.com/user-attachments/assets/9c4f125c-ff9e-47be-ad2f-277515316f10)


   - **Nome do Host:** Insira o nome do host ou endereço IP que você deseja escanear (ex: `www.example.com` ou `192.168.1.1`).
   - **Porta Inicial:** Insira a porta inicial do intervalo que deseja escanear (ex: `20`).
   - **Porta Final:** Insira a porta final do intervalo que deseja escanear (ex: `1024`).
   - Clique no botão **"Iniciar Escaneamento"** para começar o processo.

4. **Resultados:**

   - O aplicativo exibirá as portas abertas e os serviços conhecidos associados na área de texto abaixo dos campos de entrada.
