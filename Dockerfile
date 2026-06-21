# Usa uma imagem oficial e leve do Python
FROM python:3.10-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências primeiro (otimização de cache)
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta que a API FastAPI utilizará
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]