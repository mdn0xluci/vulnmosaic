# VulnMosaic 🧩

**AI-powered security operator that actually leaves receipts.**

VulnMosaic combines AI reasoning with deterministic scanners and structured workflows. No vibes-only security — every finding has evidence you can reproduce.

## What is this?

A mosaic is many tiles. Each tile is a scanner, a module, a connector that produces structured findings with provenance attached. The orchestrator stitches them into a single, reproducible report.

This is not "AI replaces scanners." This is **AI orchestrates scanners, contextualizes results, insists on evidence, and ships reports that can be replayed.**

## Architecture

```
vulnmosaic/
  core/          # Session management, task runner, concurrency
  providers/     # AI model abstractions (Claude, GPT, Gemini, Ollama)
  tools/         # Wrappers around external binaries (nuclei, httpx, nmap...)
  modules/       # Detection modules (recon, web, api, auth, misconfig)
  reporting/     # Jinja2 templates, Markdown + JSON output
  plugins/       # Entry-points based plugin loader (v2)
```

## Execution Phases

- **Phase A:** Recon (fast, mostly deterministic)
- **Phase B:** Attack surface mapping (routes, params, schemas)
- **Phase C:** Hypothesis & exploit attempts (AI proposes, tools execute)
- **Phase D:** Validate & de-duplicate (reduce false positives)
- **Phase E:** Report (with reproduction steps)

## Philosophy

- Evidence is the currency. No evidence, no claim.
- Clean contracts beat clever hacks.
- Ethics arent a disclaimer — theyre an architecture decision.
- Edgewatch connectors as first-class intelligence layer.

## Status

🚧 Early development. I'm building this in public because I think security tooling deserves better than a pile of scripts and vibes.

## License

MIT
