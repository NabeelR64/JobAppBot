# Use Node.js 18 as the base image to satisfy Angular CLI requirements
FROM node:18-alpine AS build

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application source code to the container
COPY . .

# Build the Angular app
RUN npm run build --prod

# Stage 2: Serve the app using nginx
FROM nginx:alpine

# Copy built files from the previous stage
COPY --from=build /app/dist/job-application-portal /usr/share/nginx/html

# Expose port 80 for the Angular app
EXPOSE 80

# Start NGINX server
CMD ["nginx", "-g", "daemon off;"]
