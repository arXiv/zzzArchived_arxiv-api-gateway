---
title: arXiv API OAuth2 endpoints
spec: https://github.com/cul-it/arxiv-auth/blob/registry/schema/openapi.yaml
template: page.html
---

{% import "api/openapi.html" as openapi %}

{{ openapi.render_schema(schemas.auth.openapi.data, render_markdown) }}
