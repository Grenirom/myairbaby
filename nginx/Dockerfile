FROM nginx

# Удаляем стандартный конфиг Nginx
RUN rm /etc/nginx/conf.d/default.conf

# Копируем ваш кастомный конфиг Nginx
COPY nginx/default.conf /etc/nginx/conf.d/

# Открываем порт 80
EXPOSE 80
