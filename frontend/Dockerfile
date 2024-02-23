

FROM node:18-alpine

WORKDIR /app

# want to install dependencies first
#COPY (para1: local package.json, para2: where we want to copy it in the container, which is the current directory)
COPY package*.json  ./

RUN npm install
COPY . .

#RUN npm run build

ENV PORT=3000
EXPOSE 3000

CMD [ "npm", "run", "dev" ]
#in production CMD [ "npm", "run", "serve" ]
#and in package.json under scripts dev: vite to "serve": "vite preview"
#docker image: list all images
#docker run image_id

#docker stop container_id to stop the container
#docker rm container_id to delete the container