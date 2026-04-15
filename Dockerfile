# Use official lightweight Nginx image
FROM nginx:alpine
# Remove default content
RUN rm -rf /usr/share/nginx/html/*
# Copy your app.html into the default Nginx public folder
COPY app.html /usr/share/nginx/html/index.html
# Expose port 80
EXPOSE 80
# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]
