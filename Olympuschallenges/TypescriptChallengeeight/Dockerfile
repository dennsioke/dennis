FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
ENV NODE_ENV=development
COPY . .
RUN yarn install --frozen-lockfile
RUN chmod -R a+rw /app
CMD ["/bin/bash"]