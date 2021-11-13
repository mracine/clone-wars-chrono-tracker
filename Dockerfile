FROM node:lts-alpine as frontend
WORKDIR /app
COPY ./web/package*.json ./
RUN npm install
COPY ./web ./
RUN npm run build

FROM nginx:stable-alpine as production-stage
COPY ./api /opt/clone-wars-chrono-tracker

WORKDIR /opt/clone-wars-chrono-tracker
RUN apk add --no-cache python3 py3-pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY --from=frontend /app/dist /usr/share/nginx/html
COPY ./docker /
RUN rm /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["/usr/local/bin/start_tracker"]
