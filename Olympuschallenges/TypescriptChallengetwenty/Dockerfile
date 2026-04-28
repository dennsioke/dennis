FROM public.ecr.aws/x8v8d7g8/mars-base:latest

WORKDIR /app

COPY package.json pnpm-lock.yaml ./

RUN pnpm install --frozen-lockfile

COPY . .

CMD ["/bin/bash"]
