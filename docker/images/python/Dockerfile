FROM python:3.12.1-alpine

WORKDIR /usr/src/app

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Install bash and dependencies
RUN apk add bash postgresql-dev gcc python3-dev musl-dev nodejs npm

# Upgrade npm and install nodemon
RUN npm update npm -g && npm install nodemon -g

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install dependencies without cache and without compiling .pyc files
COPY ./requirements.txt ./
RUN pip install --no-compile --no-cache-dir -r requirements.txt

# Run the script
CMD (sed -i 's/\r$//' ./run.sh) && (chmod +x ./run.sh) && (./run.sh)
