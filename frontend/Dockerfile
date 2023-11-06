# # Build step #1: build the React front end
# FROM node:lts-alpine as build-step
# WORKDIR /app
# ENV PATH /app/node_modules/.bin:$PATH
# COPY package.json  ./
# COPY ./src ./src
# COPY ./public ./public
# RUN npm install
# RUN npm run build

# # Build step #2: build an Caddy container
# FROM caddy:alpine
# EXPOSE 80
# EXPOSE 443
# COPY --from=build-step /app/build /usr/share/caddy


# Use the official Node.js image as a base image
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY . /app/

# Install dependencies

RUN cd  /app

RUN rm -rf  node_modules/

# RUN npm install --global yarn
# Install dependencies

# Expose the port the application runs on
EXPOSE 3000
