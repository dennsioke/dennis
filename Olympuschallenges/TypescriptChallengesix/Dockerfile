FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
