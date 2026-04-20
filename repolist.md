# Validated Repos for TypeScript Challenges

> **Filtering criteria applied:**
> - Has tests (test dir, __tests__, spec, or test script in package.json)
> - Small (<100MB) or Medium (<250MB) repo size
> - Has root `package.json` (Node.js/TypeScript project)
> - Compatible with mars-base Dockerfile (`npm install --ignore-scripts`)
> - Sufficient complexity for super complex challenges
>
> **Removed 24 repos** — too large (>250MB), no tests, no package.json, needs native/platform builds (React Native, VS Code ext, Atom plugin, Ionic), or too simple for complex challenges.

---

## Small Repos (<100MB) — 25 repos

---

### 1. inikulin/parse5
- **URL:** https://github.com/inikulin/parse5
- **Commit:** `e402276597de95b3ce5372a62559d19ff2c7b052`
- **Last Pushed:** 2026-04-17

**HTML parsing/serialization toolset for Node.js. WHATWG HTML5-compliant.**
- **Size:** 13MB (Small)
- **Stars:** 3.9k
- **Tests:** ✅ (test directory)
- **Package Manager:** npm (package-lock.json)
- **Challenge Potential:** ★★★★★ — State machine tokenizer, tree construction algorithm, serialization. Extremely complex parsing logic with rich edge cases.
- **Tags:** html, parser, serialization, html5, tokenizer

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 2. acacode/swagger-typescript-api
- **URL:** https://github.cb57c9d20df2cf7a0f2fe2018d5aa223b5f6a9671om/acacode/swagger-typescript-api
- **Commit:** ``
- **Last Pushed:** 2026-04-18

**Generate the API Client for Fetch or Axios from an OpenAPI Specification.**
- **Size:** 20MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (tests directory)
- **Package Manager:** npm compatible (no lockfile committed)
- **Challenge Potential:** ★★★★★ — Full code generation pipeline. Template rendering, AST construction, type inference from OpenAPI specs.
- **Tags:** openapi, codegen, typescript, swagger, api-client

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 3. compodoc/compodoc
- **URL:** https://github.com/compodoc/compodoc
- **Commit:** `03df881c7394dc079e94641d5aea35b55affd140`
- **Last Pushed:** 2026-04-18

**The missing documentation tool for your Angular, Nest & Stencil application.**
- **Size:** 49MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (test directory)
- **Package Manager:** npm (package-lock.json)
- **Challenge Potential:** ★★★★★ — AST analysis of Angular/NestJS source code, complex template rendering, JSDoc/TSDoc parsing.
- **Tags:** documentation, angular, typescript, generator, jsdoc

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 4. jeffijoe/awilix
- **URL:** https://github.com/jeffijoe/awilix
- **Commit:** `ae94bfd9635cc27acd4c40048f958bd550264f69`
- **Last Pushed:** 2026-03-27

**Extremely powerful Inversion of Control (IoC) container for Node.JS.**
- **Size:** 2MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (test script in package.json)
- **Package Manager:** npm (package-lock.json)
- **Challenge Potential:** ★★★★★ — Complex dependency graph resolution, lifetime scoping (singleton/transient/scoped), injection modes, proxy handling.
- **Tags:** nodejs, ioc, dependency-injection, container

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 5. LegendApp/legend-state
- **URL:** https://github.com/LegendApp/legend-state
- **Commit:** `d65f0608495a3fd022f820b52394d6574e7d551d`
- **Last Pushed:** 2026-03-14

**Super fast and powerful state library with fine-grained reactivity and automatic persistence.**
- **Size:** 19MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (tests directory)
- **Package Manager:** npm compatible (no lockfile committed)
- **Challenge Potential:** ★★★★★ — Proxy-based observable system, fine-grained reactivity tracking, computed values, persistence layer.
- **Tags:** state-management, reactivity, proxy, persistence, observable

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 6. lukeautry/tsoa
- **URL:** https://github.com/lukeautry/tsoa
- **Commit:** `f0f9aa792d25c16c6ad4dd152cbac347c5faa471`
- **Last Pushed:** 2026-04-15

**Build OpenAPI-compliant REST APIs using TypeScript and Node.**
- **Size:** 7MB (Small)
- **Stars:** 4k
- **Tests:** ✅ (tests directory)
- **Package Manager:** yarn (yarn.lock) — npm install compatible
- **Challenge Potential:** ★★★★★ — Decorator-based route generation, request validation, OpenAPI spec generation, metadata extraction.
- **Tags:** rest-api, openapi, typescript, decorators, validation

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json yarn.lock ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 7. sindresorhus/p-queue
- **URL:** https://github.com/sindresorhus/p-queue
- **Commit:** `53848611d103e16f39e94cba8c70a36f0ec791a0`
- **Last Pushed:** 2026-04-07

**Promise queue with concurrency control.**
- **Size:** <1MB (Small)
- **Stars:** 4.2k
- **Tests:** ✅ (test directory)
- **Package Manager:** npm compatible (no lockfile committed)
- **Challenge Potential:** ★★★★☆ — Async queue with priority ordering, concurrency limits, timeouts, pause/resume, event emission.
- **Tags:** queue, promise, async, concurrency, node-module

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 8. cosmiconfig/cosmiconfig
- **URL:** https://github.com/cosmiconfig/cosmiconfig
- **Commit:** `9a5cda3785913cce1eb5fa257e5994914b9ec599`
- **Last Pushed:** 2026-03-02

**Find and load configuration from package.json property, rc file, TypeScript module, and more!**
- **Size:** 1MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (test directory)
- **Package Manager:** npm compatible (no lockfile committed)
- **Challenge Potential:** ★★★★☆ — File system traversal, multi-format config loading (JSON, YAML, JS, TS), caching, custom loaders.
- **Tags:** config, configuration, loader, rc-file, typescript

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 9. prettier/prettier-eslint
- **URL:** https://github.com/prettier/prettier-eslint
- **Commit:** `6797d5df32aa5c19d1d283454184023d7728ace0`
- **Last Pushed:** 2026-04-17

**Code → prettier → eslint --fix → Formatted Code.**
- **Size:** 2MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (tests directory)
- **Package Manager:** yarn (yarn.lock) — npm install compatible
- **Challenge Potential:** ★★★★☆ — AST transformation pipeline, config merging between prettier and eslint, formatting conflict resolution.
- **Tags:** javascript, formatter, eslint, prettier, ast

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json yarn.lock ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 10. alovajs/alova
- **URL:** https://github.com/alovajs/alova
- **Commit:** `2f6d6499cd9b4f141e584bba790c0e4da7ef208e`
- **Last Pushed:** 2026-04-07

**A request toolkit for ultimate efficiency.**
- **Size:** 21MB (Small)
- **Stars:** 4k
- **Tests:** ✅ (packages/alova/test, packages/client/test)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — Multi-adapter request system (axios, fetch, XMLHttpRequest), caching strategies, state management integration, middleware pipeline.
- **Tags:** http-client, request, caching, adapters, middleware

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 11. unplugin/unplugin-vue-components
- **URL:** https://github.com/unplugin/unplugin-vue-components
- **Commit:** `5e2addf639894c3a3d3369502d735f0a19223094`
- **Last Pushed:** 2026-03-23

**On-demand components auto importing for Vue.**
- **Size:** 3MB (Small)
- **Stars:** 4.3k
- **Tests:** ✅ (test directory)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — AST analysis for Vue SFC components, auto-import resolution, transformer pipeline, multi-bundler support (Vite/Webpack/Rollup).
- **Tags:** vue, components, auto-import, unplugin, transformer

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 12. Bowen7/regex-vis
- **URL:** https://github.com/Bowen7/regex-vis
- **Commit:** `5de63f31b2bbf3d39de74072c30dd4aa147f32c8`
- **Last Pushed:** 2026-01-02

**Regex visualizer & editor.**
- **Size:** 2MB (Small)
- **Stars:** 4.3k
- **Tests:** ✅ (test directory)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — Regex parsing into AST, graph visualization algorithms, editor state management, NFA/DFA concepts.
- **Tags:** regex, parser, visualizer, editor, ast

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 13. actions/upload-artifact
- **URL:** https://github.com/actions/upload-artifact
- **Commit:** `043fb46d1a93c77aae656e7c1c64a875d1fc6a0a`
- **Last Pushed:** 2026-04-14

**GitHub Action for uploading artifacts.**
- **Size:** 18MB (Small)
- **Stars:** 4k
- **Tests:** ✅ (__tests__ directory)
- **Package Manager:** npm (package-lock.json)
- **Challenge Potential:** ★★★★☆ — File streaming, chunked uploads, retry logic with backoff, compression, path resolution.
- **Tags:** github-actions, artifacts, upload, streaming, retry

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 14. exa-labs/exa-mcp-server
- **URL:** https://github.com/exa-labs/exa-mcp-server
- **Commit:** `7060e0efbc272dddce126e7a35dbf1722c510d08`
- **Last Pushed:** 2026-04-18

**Exa MCP for web search and web crawling.**
- **Size:** 4MB (Small)
- **Stars:** 4.3k
- **Tests:** ✅ (test directory)
- **Package Manager:** npm (package-lock.json)
- **Challenge Potential:** ★★★☆☆ — MCP protocol implementation, search API integration, result parsing, crawling logic.
- **Tags:** mcp, web-search, crawling, code-search, api

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 15. makenotion/notion-mcp-server
- **URL:** https://github.com/makenotion/notion-mcp-server
- **Commit:** `3bef7addac59b237da3bb41f36a520babc47fa3c`
- **Last Pushed:** 2026-03-18

**Official Notion MCP Server.**
- **Size:** 1MB (Small)
- **Stars:** 4.2k
- **Tests:** ✅ (test directory)
- **Package Manager:** npm (package-lock.json)
- **Challenge Potential:** ★★★☆☆ — MCP protocol, Notion API integration, schema validation, request routing.
- **Tags:** notion, mcp, api, integration

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 16. builderz-labs/mission-control
- **URL:** https://github.com/builderz-labs/mission-control
- **Commit:** `90a5615fc73dc03e35c1dc886bc6468013eb2275`
- **Last Pushed:** 2026-04-14

**Self-hosted AI agent orchestration platform.**
- **Size:** 13MB (Small)
- **Stars:** 4.2k
- **Tests:** ✅ (test directory)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — Multi-agent workflow orchestration, task dispatch, spend monitoring, operation governance.
- **Tags:** ai-agents, orchestration, workflow, dashboard, sqlite

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 17. ollama/ollama-js
- **URL:** https://github.com/ollama/ollama-js
- **Commit:** `9c92b18d4026f5345ff7950f15216372b23401a1`
- **Last Pushed:** 2026-02-18

**Ollama JavaScript library.**
- **Size:** <1MB (Small)
- **Stars:** 4.2k
- **Tests:** ✅ (test directory)
- **Package Manager:** npm (package-lock.json)
- **Challenge Potential:** ★★★☆☆ — Streaming API client, model management, chat/completion interfaces, abort handling.
- **Tags:** ollama, llm, api-client, streaming, javascript

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json package-lock.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 18. antfu-collective/taze
- **URL:** https://github.com/antfu-collective/taze
- **Commit:** `5b22abc56fce4a2a1e8fcaabb65f6d6392729674`
- **Last Pushed:** 2026-04-03

**A modern CLI tool that keeps your deps fresh.**
- **Size:** 3MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (test directory)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — Semver range resolution, npm registry querying, dependency graph analysis, monorepo support.
- **Tags:** cli, dependencies, updates, semver, monorepo

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 19. kentcdodds/match-sorter
- **URL:** https://github.com/kentcdodds/match-sorter
- **Commit:** `e7c9c20efd8fd8b4428ba20795f7a376fb46ff00`
- **Last Pushed:** 2026-04-15

**Simple, expected, and deterministic best-match sorting of an array in JavaScript.**
- **Size:** <1MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (test directory with __tests__)
- **Package Manager:** npm compatible (no lockfile committed)
- **Challenge Potential:** ★★★☆☆ — Ranking algorithm with multiple strategies (case-sensitive, word starts, contains, acronym), threshold filtering, custom key accessors.
- **Tags:** sorting, matching, ranking, search, algorithm

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 20. antvis/mcp-server-chart
- **URL:** https://github.com/antvis/mcp-server-chart
- **Commit:** `7563a99ca758362733b4aa41bc8283c0285ccfb9`
- **Last Pushed:** 2026-02-25

**A visualization MCP & skills with 25+ visual charts using @antvis.**
- **Size:** <1MB (Small)
- **Stars:** 4k
- **Tests:** ✅ (__tests__ directory + vitest.config.ts)
- **Package Manager:** npm compatible (no lockfile committed)
- **Challenge Potential:** ★★★☆☆ — Chart specification generation, data transformation, MCP protocol, visualization grammar.
- **Tags:** visualization, charts, mcp, antv, data-analysis

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 21. vvo/iron-session
- **URL:** https://github.com/vvo/iron-session
- **Commit:** `6b51b419a918a99261fe1c468818fbcfed483834`
- **Last Pushed:** 2026-04-13

**Secure, stateless, and cookie-based session library for JavaScript frameworks.**
- **Size:** 8MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (test script in package.json)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — Cryptographic seal/unseal operations, cookie management, session lifecycle, framework-agnostic middleware.
- **Tags:** session, cookies, authentication, nextjs, crypto

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 22. vite-pwa/vite-plugin-pwa
- **URL:** https://github.com/vite-pwa/vite-plugin-pwa
- **Commit:** `4e1621588676db62c0c0944d64a35485e257f023`
- **Last Pushed:** 2026-03-04

**Zero-config PWA for Vite.**
- **Size:** 3MB (Small)
- **Stars:** 4.1k
- **Tests:** ✅ (test script in package.json)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★☆☆ — Service worker generation, workbox integration, manifest handling, Vite plugin API.
- **Tags:** pwa, vite, service-worker, workbox, plugin

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 23. vuejs/vuefire
- **URL:** https://github.com/vuejs/vuefire
- **Commit:** `efec2403e6137fc3ad051ede1808e3b383b25710`
- **Last Pushed:** 2026-04-15

**Firebase bindings for Vue.js.**
- **Size:** 11MB (Small)
- **Stars:** 3.9k
- **Tests:** ✅ (tests directory)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — Reactive Firebase data binding, real-time sync, Firestore/RTDB abstraction, composable API design.
- **Tags:** firebase, vue, realtime, database, composables

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 24. t3-oss/t3-env
- **URL:** https://github.com/t3-oss/t3-env
- **Commit:** `7d26a645904a8fa8712c16f31a4737a80e7066fd`
- **Last Pushed:** 2026-04-01

**Type-safe environment variable validation.**
- **Size:** 2MB (Small)
- **Stars:** 3.9k
- **Tests:** ✅ (packages/core/test)
- **Package Manager:** npm compatible (no lockfile committed)
- **Challenge Potential:** ★★★★☆ — Zod schema integration, type inference from env schemas, framework adapters (Next.js, Nuxt), build-time validation.
- **Tags:** env, validation, zod, type-safety, nextjs

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

### 25. run-llama/llama_cloud_services
- **URL:** https://github.com/run-llama/llama_cloud_services
- **Commit:** `f385e96ab82ddb88330277c34394546398c8bed0`
- **Last Pushed:** 2026-04-13

**Knowledge Agents and Management in the Cloud.**
- **Size:** 91MB (Small)
- **Stars:** 4.2k
- **Tests:** ✅ (test directory)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★☆ — Document parsing (PDF, PPTX), structured data extraction, knowledge agent orchestration, cloud API patterns.
- **Tags:** pdf, parsing, document, agents, structured-data

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

## Medium Repos (100–250MB) — 1 repo

---

### 26. amannn/next-intl
- **URL:** https://github.com/amannn/next-intl
- **Commit:** `b4aa5380c50ad59a80d1dfdbc229590a4e0133a3`
- **Last Pushed:** 2026-04-10

**Internationalization (i18n) for Next.js.**
- **Size:** 166MB (Medium)
- **Stars:** 4.2k
- **Tests:** ✅ (test directory)
- **Package Manager:** pnpm (pnpm-lock.yaml)
- **Challenge Potential:** ★★★★★ — ICU message formatting, plural rules, date/number formatters, Next.js App Router integration, middleware routing, type-safe message keys.
- **Tags:** i18n, nextjs, react, date-formatting, localization

**Dockerfile:**
```dockerfile
FROM public.ecr.aws/x8v8d7g8/mars-base:latest
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN NODE_ENV=development npm install --ignore-scripts
COPY . .
ENV NODE_ENV=development
CMD ["/bin/bash"]
```

---

## Removed Repos (24 repos)

| Repo | Reason |
|------|--------|
| zoontek/react-native-bootsplash | React Native — needs native iOS/Android build tooling |
| open-pencil/open-pencil | Skia native canvas bindings — --ignore-scripts breaks native build |
| Conway-Research/automaton | Too simple (1MB) for complex challenges |
| dvtng/react-loading-skeleton | Too simple — basic skeleton UI component |
| react-monaco-editor/react-monaco-editor | Thin wrapper around Monaco — core logic is in Monaco itself |
| OHIF/Viewers | Too large (433MB) |
| obytes/react-native-template-obytes | React Native/Expo — needs native mobile tooling |
| autobase-tech/autobase | No package.json — not a Node.js project (PostgreSQL focused) |
| heilcheng/awesome-agent-skills | No package.json — curated list/website only |
| nandorojo/solito | React Native + Next.js — needs native tooling; no tests found |
| elrumordelaluz/reactour | No tests found |
| watsonbox/exportify | No tests found |
| ts-essentials/ts-essentials | Type-only library — no runtime tests, no runtime logic |
| tonybaloney/vscode-pets | VS Code extension — requires VS Code API runtime for testing |
| algolia/instantsearch | Too large (396MB) |
| AzureAD/microsoft-authentication-library-for-js | Too large (250MB); no root-level tests |
| nteract/hydrogen | Atom editor plugin — requires Atom runtime |
| antvis/L7 | Too large (288MB); no root-level tests |
| xiaolin/react-image-gallery | No standard test directory found |
| wojtekmaj/react-lifecycle-methods-diagram | No tests found |
| maurodesouza/profile-readme-generator | No tests found |
| matthewhudson/current-device | Too simple for complex challenges |
| bitpay/wallet | Ionic/Cordova mobile app — needs native mobile tooling (198MB) |
| prazzon/Flexbox-Labs | No tests found |
