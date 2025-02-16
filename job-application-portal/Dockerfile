# Use official Node.js image as the base image
FROM node:18-alpine AS development

# Set working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to install dependencies
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the entire project to the working directory
COPY . .

# Expose the port that Angular serves the app on (default is 4200)
EXPOSE 4200

# Start the Angular app using ng serve
CMD ["npm", "run", "start"]
