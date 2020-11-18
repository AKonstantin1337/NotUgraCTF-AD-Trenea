FROM alpine:latest

RUN apk add --no-cache npm nodejs
COPY . /app
WORKDIR /app
RUN npm install

CMD ["npm", "start"]
