# Codex MCP Configuration Guide

This guide documents how to connect Codex CLI or the Codex IDE extension to Model Context Protocol (MCP) servers, the protocol features Codex supports, and how to run Codex itself as an MCP server.

## MCP Overview

- **Model Context Protocol (MCP)** lets Codex call external tools and ingest additional context (e.g., documentation, browser automation, Figma, logs).
- Codex CLI and the Codex IDE extension both support MCP servers and share the same configuration under `~/.codex/config.toml`.
- Supported MCP server types and features:
  - STDIO servers (spawned from a local command)
  - Streamable HTTP servers (accessed via URL)
  - Environment variable injection
  - Bearer-token authentication
  - OAuth authentication (requires `experimental_use_rmcp_client = true`)

## Configuring MCP Servers

Codex reads MCP settings from `~/.codex/config.toml`. You can manage servers in two ways:

1. **CLI helper** – use the built-in `codex mcp` commands.
2. **Manual edit** – update `config.toml` directly for fine-grained control.

### CLI Workflow

- **Add a server**
  ```bash
  codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>
  ```
  Example (Context7 documentation server):
  ```bash
  codex mcp add context7 -- npx -y @upstash/context7-mcp
  ```

- **Help**
  ```bash
  codex mcp --help
  ```

- **Inspect active connections inside the TUI**
  - Launch Codex.
  - Run `/mcp` in the command palette to list connected servers.

### Editing `config.toml`

- Config tables live under `[mcp_servers.<server-name>]`.
- Options for STDIO servers:
  ```toml
  [mcp_servers.context7]
  command = "npx"
  args = ["-y", "@upstash/context7-mcp"]

  [mcp_servers.context7.env]
  MY_ENV_VAR = "MY_ENV_VALUE"
  ```

- Options for streamable HTTP servers:
  ```toml
  [mcp_servers.figma]
  url = "https://mcp.figma.com/mcp"
  bearer_token = "YOUR_TOKEN" # optional
  ```

- Global MCP settings (top-level in `config.toml`, not inside a server table):
  ```toml
  experimental_use_rmcp_client = true
  startup_timeout_sec = 120
  tool_timeout_sec = 60
  ```
  Setting `experimental_use_rmcp_client = true` enables the new RMCP client implementation and is required for OAuth-based MCP servers.

### Useful MCP Servers

- Context7 – developer documentation search.
- Figma Local/Remote – access design files.
- Playwright – scripted browser control.
- Chrome Developer Tools – direct Chrome automation.
- Sentry – inspect error logs.
- GitHub – manage issues, PRs, and more via MCP.

## Running Codex as an MCP Server

Codex can act as an MCP server so other MCP-aware clients can drive Codex sessions.

- **Start the server**
  ```bash
  codex mcp-server
  ```

- **Inspect with MCP Inspector**
  ```bash
  npx @modelcontextprotocol/inspector codex mcp-server
  ```

### Available Tools

1. **`codex`** – starts a new Codex session.
   - Key properties:
     - `prompt` (string, required)
     - `approval-policy` (`untrusted`, `on-failure`, `never`)
     - `base-instructions` (string override)
     - `config` (object overrides for `config.toml`)
     - `cwd` (working directory)
     - `include-plan-tool` (boolean)
     - `model` (model name override, e.g., `o3`, `o4-mini`)
     - `profile` (config profile name)
     - `sandbox` (`read-only`, `workspace-write`, or `danger-full-access`)

2. **`codex-reply`** – continue an existing Codex session.
   - Key properties:
     - `prompt` (string, required)
     - `conversationId` (string, required)

### Inspector Timeouts

Codex execution can take several minutes. In the MCP Inspector UI set:

- **Request timeout**: `600000` ms (10 minutes)
- **Total timeout**: `600000` ms (10 minutes)

### Example Exercise

Use the MCP Inspector with `codex mcp-server` to build a tic‑tac‑toe game:

| Property         | Value                                                                 |
|------------------|-----------------------------------------------------------------------|
| `prompt`         | `Implement a simple tic-tac-toe game...`                              |
| `approval-policy`| `never`                                                               |
| `sandbox`        | `workspace-write`                                                     |

Run the `codex` tool with those parameters and observe the emitted events as Codex builds the project.

## Quick Reference

- `codex mcp add <name> -- <command>` – register a STDIO MCP server.
- `codex mcp --help` – list CLI MCP commands.
- `/mcp` inside Codex TUI – show active MCP servers.
- `~/.codex/config.toml` – shared MCP configuration for CLI and IDE.
- `codex mcp-server` – expose Codex itself as an MCP server.

