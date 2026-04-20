FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY . .
RUN yarn install --frozen-lockfile
RUN yarn prepare
CMD ["/bin/bash"]
