FROM alpine:latest

RUN apk add --update --no-cache bash socat su-exec && adduser -S buggy
COPY . /app
RUN chmod 550 /app/drop
WORKDIR /app

CMD ["/app/drop"]
