# Stage: Frontend build
FROM node:18-slim AS builder
WORKDIR /frontend

# Copy dependency file first for better caching
COPY package.json ./
RUN npm install

# Copy all application code
COPY . .

# Framework-specific instructions
RUN npm install -g serve

# Verify entry point exists
RUN test -f index.js || (echo "Entry point index.js not found" && exit 1)

# Build the application
RUN npm run build

# Production stage
FROM nginx:alpine
WORKDIR /usr/share/nginx/html

# Copy everything from builder
COPY --from=builder /frontend ./

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]