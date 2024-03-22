# Use a base image with Node.js and Python
FROM node:14 AS sabaki
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install Sabaki
COPY --from=sabaki /usr/local/bin /usr/local/bin
COPY --from=sabaki /usr/local/lib /usr/local/lib

# Install git to clone the repository
RUN apt-get update && apt-get install -y git

# Clone your bot script from GitHub
RUN git clone https://github.com/lolzhub/GO/.git

RUN mv GO/* /app

# Expose any ports needed for communication with your bot
EXPOSE 5000

# Command to start Sabaki and your bot
CMD ["sabaki", "--gtp", "bodvar14.py", "--port", "5000"]
