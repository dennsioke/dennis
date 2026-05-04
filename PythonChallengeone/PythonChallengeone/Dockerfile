FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app

# Install package before copying testdata to avoid pip modifying
# files in tests/testdata during the build upload scan
COPY pyproject.toml ./
COPY src/ ./src/
RUN pip install -e . && \
    pip install pytest pytest-timeout hypothesis

# Copy the full repository (testdata, tests, etc.)
COPY . .

CMD ["/bin/bash"]
