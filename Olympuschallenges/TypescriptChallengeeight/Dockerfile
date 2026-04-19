FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY . .
RUN NODE_ENV=development npm install --ignore-scripts
CMD ["/bin/bash"]
