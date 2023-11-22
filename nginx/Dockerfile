FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/default.conf /etc/nginx/conf.d/

EXPOSE 81

RUN mkdir -p /etc/letsencrypt/live/myairbaby.net

COPY path/to/your/fullchain.pem /etc/letsencrypt/live/myairbaby.net/fullchain.pem
COPY path/to/your/privkey.pem /etc/letsencrypt/live/myairbaby.net/privkey.pem

