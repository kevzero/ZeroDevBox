FROM node:18-bullseye

# Imposta la working directory
WORKDIR /app

# Copia solo i file di dipendenze per sfruttare la cache
COPY package*.json ./

# Installa le dipendenze
RUN npm install --legacy-peer-deps

# Copia il resto del codice
COPY . .

# Espone la porta Vite
EXPOSE 5173

# Avvia Vite con host accessibile
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]



