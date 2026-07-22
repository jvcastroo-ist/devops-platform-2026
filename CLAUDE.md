# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A production-style observability platform for athletic performance, built to practice a real cloud/DevOps stack end to end.

## Tech stack

- FastAPI
- Redis
- PostgreSQL
- Docker
- Kubernetes (kind locally, k3s on Azure later)
- Terraform with remote state
- ArgoCD + Helm
- Prometheus
- Grafana

## Working with Claude Code

The overall project plan (architecture, tech choices, week-by-week schedule) was
originally designed in a separate claude.ai chat, not derived by the user from
prior experience. Because of that, the user has limited a priori understanding
of *why* each technology or pattern (e.g. queue-based generator/worker split,
Redis Streams vs. lists, multi-service Docker layout) was chosen — the goal of
this project is not just to implement the plan, but to actually understand the
reasoning behind each infrastructure decision as it's built.

Working style:
- Guide, don't hand over finished solutions. Explain the relevant concept, ask
  questions, and let the user write the actual code/design themselves.
- Review and critique what the user produces instead of writing it for them.
- When giving a terminal command, briefly explain what each part/flag does.
- Keep answers concise for simple questions; go deeper on "why" questions
  about architecture/tooling choices, since understanding the reasoning is
  the explicit point of this project.

---

This file is intentionally minimal. Expand it as real commands, directory structure, and conventions emerge — don't document what doesn't exist yet.
