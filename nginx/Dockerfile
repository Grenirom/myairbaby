FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx/default.conf /etc/nginx/conf.d/

EXPOSE 81

RUN mkdir -p /etc/letsencrypt/live/myairbaby.net

COPY --from=certbot /etc/letsencrypt/live/myairbaby.net/fullchain.pem /etc/letsencrypt/live/myairbaby.net/fullchain.pem
COPY --from=certbot /etc/letsencrypt/live/myairbaby.net/privkey.pem /etc/letsencrypt/live/myairbaby.net/privkey.pem
