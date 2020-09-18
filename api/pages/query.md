---
title: arXiv Metadata Search API
spec: https://github.com/cul-it/arxiv-search/blob/api/schema/search.yaml
template: page.html
---

{% import "api/openapi.html" as openapi %}

{{ openapi.render_schema(schemas.query.openapi.data, render_markdown) }}
