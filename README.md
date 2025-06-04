Coletor de Cotação do Bitcoin com Python + SQLite
Este projeto realiza uma coleta periódica da cotação do Bitcoin (BTC) em tempo real utilizando a API pública do Coinbase. Os dados são transformados e armazenados localmente em um banco SQLite, com agendamento automático usando o pacote schedule.

🚀 Funcionalidades
🔍 Extração automática do valor do BTC via API

🧼 Transformação dos dados com formatação de data, moeda e valor

🗃️ Armazenamento local com banco de dados SQLite (cotacoes.db)

🕒 Agendamento periódico de coleta (por padrão, a cada 1 minuto)

🧠 Tecnologias usadas
Tecnologia	Função
Python 3	Linguagem principal
requests	Requisição HTTP para API da Coinbase
sqlite3	Armazenamento local e persistência dos dados
schedule	Agendamento de execução automatizada
datetime	Registro de data e hora

🗂️ Estrutura do Projeto
graphql
Copiar
Editar
coletor_bitcoin/
├── coletor.py         # Script principal com funções ETL e agendamento
├── cotacoes.db        # Banco SQLite gerado automaticamente
├── requirements.txt   # (opcional) Bibliotecas necessárias
└── README.md          # Este arquivo
🛠️ Como usar


📅 Agendamento
O script coleta o preço do Bitcoin a cada 1 minuto, utilizando o pacote schedule. Você verá mensagens como:


🗃️ Banco de Dados
O script cria um banco chamado cotacoes.db com a seguinte estrutura:

Campo	Tipo
id	INTEGER (autoincremento)
data	TEXT
valor	REAL
criptomoeda	TEXT
moeda	TEXT

📊 Próximos passos (ideias para evolução)
📤 Exportar os dados para CSV ou Google Sheets

🌐 Criar um dashboard com Streamlit ou Dash

☁️ Deploy em nuvem (EC2, Heroku, etc.)

🧠 Adicionar logging e tratamento de erros avançado

⏱ Agendar com cron ou systemd para rodar como serviço

