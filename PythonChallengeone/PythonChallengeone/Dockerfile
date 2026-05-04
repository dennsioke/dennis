FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app

# Copy entire repository
COPY . .

# Install dependencies
RUN pip install -e . && \
    pip install pytest pytest-timeout hypothesis

CMD ["/bin/bash"]
