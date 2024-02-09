FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

# Install additional dependencies
#RUN npm install @mui/material @mui/icons-material \
#    @emotion/react @emotion/styled \

COPY . .

RUN npm run build

EXPOSE 8080

CMD [ "npm", "run", "dev" ]
#in production CMD [ "npm", "run", "serve" ]
#and in package.json under scripts dev: vite to "serve": "vite preview"