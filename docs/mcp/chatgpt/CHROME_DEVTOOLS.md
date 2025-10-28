# Chrome DevTools MCP Server — ChatGPT Setup

This guide captures the Chrome DevTools MCP server configuration currently in use, how it was installed, and how to leverage it inside ChatGPT (or other OpenAI MCP-compatible clients).

## Where It Lives

- **Config file:** `~/.codex/config.toml`
- **Scope:** Global. The entry applies to every Codex project unless a project-specific override is added elsewhere in the file.
- **Current block:**
  ```toml
  [mcp_servers.chrome-devtools]
  command = "npx"
  args = ["-y", "chrome-devtools-mcp@latest"]
  ```

## Install Steps (Codex CLI)

1. Run from any directory:
   ```bash
   codex mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest
   ```
2. Confirm the entry exists:
   ```bash
   codex mcp list
   ```
3. Inside a Codex session, run `/mcp` to see the server is active.

## Using It in ChatGPT

1. Open ChatGPT → `Settings` → `MCP` (or the equivalent UI in your client build).
2. Add a new server with:
   - **Name:** `chrome-devtools`
   - **Command:** `npx`
   - **Arguments:** `-y`, `chrome-devtools-mcp@latest`
3. Allow the client to bypass sandboxing if prompted so Chrome can launch.
4. Start a conversation and issue Chrome automation prompts like the ones below.

> The same command and arguments work for other MCP-aware clients (Claude, Cursor, Gemini CLI, etc.). Only the configuration UI changes.

## Capabilities Overview

- Launch or attach to Chrome via the DevTools Protocol.
- Automate inputs: `click`, `drag`, `fill`, `press_key`, `upload_file`, `handle_dialog`.
- Navigate tabs/pages: open, select, close, wait for text, resize viewport.
- Emulate CPU/Network/screen conditions.
- Record performance traces, analyze Core Web Vitals, capture screenshots, list network requests, and grab console logs.
- Execute custom JavaScript in the current page with `evaluate_script`.

## Handy Commands & Flags

```bash
codex mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest   # install
codex mcp list                                                       # verify registration
codex mcp remove chrome-devtools                                     # uninstall
npx chrome-devtools-mcp@latest --help                                # view supported flags
```

Common flags for the config `args` array:

- `--headless=true` — run Chrome without a GUI.
- `--isolated=true` — use a temporary profile cleared on exit.
- `--channel=canary|beta|dev` — choose a Chrome release channel.
- `--browser-url=http://127.0.0.1:9222` — attach to a manually started Chrome.
- `--viewport=1280x720` — set the initial viewport size.
- `--categoryPerformance=false` — disable performance tools if unnecessary.

## Prompt Ideas

- “Check the performance of https://developers.chrome.com and summarize the slowest requests.”
- “Open https://app.example, wait for the `Net PnL` widget, and take a screenshot.”
- “Throttle to Fast 3G, reload https://staging.example, and report all console errors.”
- “Start a performance trace for https://shop.example, stop after Largest Contentful Paint, and share the insights.”
- “Evaluate `document.title` on the active page and report the result.”
- “List every network request triggered during login at https://login.example along with status codes.”

## Prompt-Injection & Safety Notes

- Treat any webpage content as untrusted input—explicitly instruct the assistant to ignore on-page prompts or scripts that try to redirect behavior.
- When working with sensitive environments, whitelist domains in your request (e.g., “Only interact with *.mycompany.com”).
- Consider enabling `--isolated=true` for throwaway Chrome profiles, especially when visiting untrusted sites.
- Remember that the assistant can view anything rendered in the controlled browser window; keep confidential data out of scope.

## Quick Test

After adding the server, validate the setup with a simple command:

```
Check the performance of https://developers.chrome.com
```

The assistant should launch Chrome, run a trace, and return performance insights.
