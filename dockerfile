# Base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY poso/frontend/package*.json ./frontend/

# Install frontend dependencies
RUN cd frontend && npm install

# Copy package.json and package-lock.json to the container
COPY poso/backend/package*.json ./backend/
COPY poso/package*.json ./poso/

# Install backend dependencies
RUN cd backend && npm install

# Copy the frontend and backend code to the container
COPY poso/frontend ./frontend
COPY poso/backend ./backend
COPY poso/package.json ./app

# Build the frontend
RUN cd frontend && npm run build

# Build the backend
RUN cd backend && npm run build

# Expose the port that the server will run on
EXPOSE 3013
EXPOSE 3000

# Set the working directory to the backend folder
WORKDIR /app/backend

# Start the server
## Debug frontend
# CMD ["node", "index.js"]
## Debug backend
# CMD ["npm", "run", "serve", "--prefix", "../frontend"] 


# Install concurrently globally
RUN npm install -g concurrently
# Start the frontend and backend concurrently
CMD concurrently "node index.js" "npm run serve --prefix ../frontend"


# docker build -t poso-app .
# docker run -p 3013:3013 poso-app
# docker run -p 3013:3013 -p 3000:3000 poso-app


