FROM node:18.17.1 as builder

WORKDIR /usr/src/app

COPY package.json .

RUN yarn install

COPY . .

RUN yarn run build

FROM nginx:alpine

COPY nginx.conf /etc/nginx/
COPY --from=builder /usr/src/app/build /usr/share/nginx/html

EXPOSE 3000


# FROM node:alpine

# WORKDIR /usr/src/app

# COPY package.json .

# RUN yarn install

# COPY . .

# CMD ["yarn", "start"]