# Validated Repos for Python Challenges

<!-- Criteria: has tests, size <250MB, pip install -e . compatible, self-contained test suite, complex enough for hard challenges -->

---

## [vacanza/holidays](https://github.com/vacanza/holidays)
Latest commit: [`9d862c4`](https://github.com/vacanza/holidays/commit/9d862c4be35465faa23918f827d31b94a1a2e896) — 2026-04-28
Open World Holidays Framework
python
calendar
holiday
hacktoberfest
holiday-calculation
Python
· 22 MB (small)
· Has tests: tests/ (calendars, countries, financial markets)
· Install: pyproject.toml

```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app

# Copy entire repository
COPY . .

# Install dependencies
RUN pip install -e . && \
    pip install pytest pytest-timeout hypothesis

CMD ["/bin/bash"]
```

---

## [ContextLab/hypertools](https://github.com/ContextLab/hypertools)
Latest commit: [`125a09b`](https://github.com/ContextLab/hypertools/commit/125a09b556c080e5d8bd464154116da2a7f0c044) — 2026-01-29
A Python toolbox for gaining geometric insights into high-dimensional data
visualization
python
time-series
data-visualization
high-dimensional-data
Python
· 109 MB (medium)
· Has tests: tests/ (test_align, test_cluster, test_backend, test_describe, test_format_data, ...)
· Install: setup.py

```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app

# Copy entire repository
COPY . .

# Install dependencies
RUN pip install -e . && \
    pip install pytest pytest-timeout hypothesis

CMD ["/bin/bash"]
```

---

## [karlicoss/promnesia](https://github.com/karlicoss/promnesia)
Latest commit: [`f102b0a`](https://github.com/karlicoss/promnesia/commit/f102b0acd63b27a8053002c1e3de3cccd48c5adb) — 2026-04-08
Another piece of your extended mind — personal web history search & annotation tool
memory
mind
memex
pkm
browser-history
Python
· 3.4 MB (small)
· Has tests: src/promnesia/tests/ (test_extract_urls, test_cannon, test_compare, test_traverse, ...)
· Install: pyproject.toml

```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app

# Copy entire repository
COPY . .

# Install dependencies
RUN pip install -e . && \
    pip install pytest pytest-timeout hypothesis

CMD ["/bin/bash"]
```

---

## Removed Repos

| Repo | Reason Removed |
|---|---|
| maguowei/starred | No tests |
| lucidrains/byol-pytorch | No tests |
| bayasdev/envycontrol | No tests; GPU hardware-dependent (can't run in Docker) |
| zabbix/community-templates | No `setup.py`/`pyproject.toml`; no tests |
| benavlabs/FastAPI-boilerplate | Tests require external PostgreSQL + Redis services |
| aio-libs/aiomysql | Tests require external MySQL server |
| run-llama/notebookllama | Tests require LlamaCloud API key |