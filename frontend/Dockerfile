FROM node:18

WORKDIR /app

# Fix per OpenSSL e Vite
ENV NODE_OPTIONS=--openssl-legacy-provider

COPY package*.json ./

RUN npm install --legacy-peer-deps

COPY . .

CMD ["npm", "run", "dev", "--", "--host"]

