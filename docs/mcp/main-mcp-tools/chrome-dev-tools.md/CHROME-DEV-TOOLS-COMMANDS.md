---
title: "chrome-devtools-mcp/docs/troubleshooting.md at main · ChromeDevTools/chrome-devtools-mcp"
source: "https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md"
author:
  - "[[ChromeDevTools]]"
  - "[[OrKoN]]"
  - "[[Lightning00Blade]]"
published:
created: 2025-10-28
description: "Chrome DevTools for coding agents. Contribute to ChromeDevTools/chrome-devtools-mcp development by creating an account on GitHub."
tags:
  - "clippings"
---
and

[feat: support saving snapshots to file (](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/b0ce08ae2ce422813fef3f28c18f2cb6c976d9fc)[#463](https://github.com/ChromeDevTools/chrome-devtools-mcp/pull/463)[)](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/b0ce08ae2ce422813fef3f28c18f2cb6c976d9fc)

[b0ce08a](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/b0ce08ae2ce422813fef3f28c18f2cb6c976d9fc) ·

- **[Input automation](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#input-automation)** (8 tools)
	- [`click`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#click)
	- [`drag`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#drag)
	- [`fill`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#fill)
	- [`fill_form`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#fill_form)
	- [`handle_dialog`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#handle_dialog)
	- [`hover`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#hover)
	- [`press_key`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#press_key)
	- [`upload_file`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#upload_file)
- **[Navigation automation](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#navigation-automation)** (6 tools)
	- [`close_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#close_page)
	- [`list_pages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#list_pages)
	- [`navigate_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#navigate_page)
	- [`new_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#new_page)
	- [`select_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#select_page)
	- [`wait_for`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#wait_for)
- **[Emulation](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#emulation)** (3 tools)
	- [`emulate_cpu`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#emulate_cpu)
	- [`emulate_network`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#emulate_network)
	- [`resize_page`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#resize_page)
- **[Performance](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#performance)** (3 tools)
	- [`performance_analyze_insight`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#performance_analyze_insight)
	- [`performance_start_trace`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#performance_start_trace)
	- [`performance_stop_trace`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#performance_stop_trace)
- **[Network](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#network)** (2 tools)
	- [`get_network_request`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#get_network_request)
	- [`list_network_requests`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#list_network_requests)
- **[Debugging](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#debugging)** (5 tools)
	- [`evaluate_script`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#evaluate_script)
	- [`get_console_message`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#get_console_message)
	- [`list_console_messages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#list_console_messages)
	- [`take_screenshot`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#take_screenshot)
	- [`take_snapshot`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#take_snapshot)

## Input automation

### click

**Description:** Clicks on the provided element

**Parameters:**

- **dblClick** (boolean) *(optional)*: Set to true for double clicks. Default is false.
- **uid** (string) **(required)**: The uid of an element on the page from the page content snapshot

---

### drag

**Description:**[`Drag`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#drag) an element onto another element

**Parameters:**

- **from\_uid** (string) **(required)**: The uid of the element to [`drag`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#drag)
- **to\_uid** (string) **(required)**: The uid of the element to drop into

---

### fill

**Description:** Type text into a input, text area or select an option from a <select> element.

**Parameters:**

- **uid** (string) **(required)**: The uid of an element on the page from the page content snapshot
- **value** (string) **(required)**: The value to [`fill`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#fill) in

---

### fill\_form

**Description:**[`Fill`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#fill) out multiple form elements at once

**Parameters:**

- **elements** (array) **(required)**: Elements from snapshot to [`fill`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#fill) out.

---

### handle\_dialog

**Description:** If a browser dialog was opened, use this command to handle it

**Parameters:**

- **action** (enum: "accept", "dismiss") **(required)**: Whether to dismiss or accept the dialog
- **promptText** (string) *(optional)*: Optional prompt text to enter into the dialog.

---

### hover

**Description:**[`Hover`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#hover) over the provided element

**Parameters:**

- **uid** (string) **(required)**: The uid of an element on the page from the page content snapshot

---

### press\_key

**Description:** Press a key or key combination. Use this when other input methods like [`fill`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#fill) () cannot be used (e.g., keyboard shortcuts, navigation keys, or special key combinations).

**Parameters:**

- **key** (string) **(required)**: A key or a combination (e.g., "Enter", "Control+A", "Control++", "Control+Shift+R"). Modifiers: Control, Shift, Alt, Meta

---

### upload\_file

**Description:** Upload a file through a provided element.

**Parameters:**

- **filePath** (string) **(required)**: The local path of the file to upload
- **uid** (string) **(required)**: The uid of the file input element or an element that will open file chooser on the page from the page content snapshot

---

## Navigation automation

### close\_page

**Description:** Closes the page by its index. The last open page cannot be closed.

**Parameters:**

- **pageIdx** (number) **(required)**: The index of the page to close. Call [`list_pages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#list_pages) to list pages.

---

### list\_pages

**Description:** Get a list of pages open in the browser.

**Parameters:** None

---

### navigate\_page

**Description:** Navigates the currently selected page to a URL.

**Parameters:**

- **timeout** (integer) *(optional)*: Maximum wait time in milliseconds. If set to 0, the default timeout will be used.
- **type** (enum: "url", "back", "forward", "reload") *(optional)*: Navigate the page by URL, back or forward in history, or reload.
- **url** (string) *(optional)*: Target URL (only type=url)

---

### new\_page

**Description:** Creates a new page

**Parameters:**

- **timeout** (integer) *(optional)*: Maximum wait time in milliseconds. If set to 0, the default timeout will be used.
- **url** (string) **(required)**: URL to load in a new page.

---

### select\_page

**Description:** Select a page as a context for future tool calls.

**Parameters:**

- **pageIdx** (number) **(required)**: The index of the page to select. Call [`list_pages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#list_pages) to list pages.

---

### wait\_for

**Description:** Wait for the specified text to appear on the selected page.

**Parameters:**

- **text** (string) **(required)**: Text to appear on the page
- **timeout** (integer) *(optional)*: Maximum wait time in milliseconds. If set to 0, the default timeout will be used.

---

## Emulation

### emulate\_cpu

**Description:** Emulates CPU throttling by slowing down the selected page's execution.

**Parameters:**

- **throttlingRate** (number) **(required)**: The CPU throttling rate representing the slowdown factor 1-20x. Set the rate to 1 to disable throttling

---

### emulate\_network

**Description:** Emulates network conditions such as throttling or offline mode on the selected page.

**Parameters:**

- **throttlingOption** (enum: "No emulation", "Offline", "Slow 3G", "Fast 3G", "Slow 4G", "Fast 4G") **(required)**: The network throttling option to emulate. Available throttling options are: No emulation, Offline, Slow 3G, Fast 3G, Slow 4G, Fast 4G. Set to "No emulation" to disable. Set to "Offline" to simulate offline network conditions.

---

### resize\_page

**Description:** Resizes the selected page's window so that the page has specified dimension

**Parameters:**

- **height** (number) **(required)**: Page height
- **width** (number) **(required)**: Page width

---

## Performance

### performance\_analyze\_insight

**Description:** Provides more detailed information on a specific Performance Insight that was highlighted in the results of a trace recording.

**Parameters:**

- **insightName** (string) **(required)**: The name of the Insight you want more information on. For example: "DocumentLatency" or "LCPBreakdown"

---

### performance\_start\_trace

**Description:** Starts a performance trace recording on the selected page. This can be used to look for performance problems and insights to improve the performance of the page. It will also report Core Web Vital (CWV) scores for the page.

**Parameters:**

- **autoStop** (boolean) **(required)**: Determines if the trace recording should be automatically stopped.
- **reload** (boolean) **(required)**: Determines if, once tracing has started, the page should be automatically reloaded.

---

### performance\_stop\_trace

**Description:** Stops the active performance trace recording on the selected page.

**Parameters:** None

---

## Network

### get\_network\_request

**Description:** Gets a network request by URL. You can get all requests by calling [`list_network_requests`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#list_network_requests).

**Parameters:**

- **reqid** (number) **(required)**: The reqid of a request on the page from the listed network requests

---

### list\_network\_requests

**Description:** List all requests for the currently selected page since the last navigation.

**Parameters:**

- **includePreservedRequests** (boolean) *(optional)*: Set to true to return the preserved requests over the last 3 navigations.
- **pageIdx** (integer) *(optional)*: Page number to return (0-based). When omitted, returns the first page.
- **pageSize** (integer) *(optional)*: Maximum number of requests to return. When omitted, returns all requests.
- **resourceTypes** (array) *(optional)*: Filter requests to only return requests of the specified resource types. When omitted or empty, returns all requests.

---

## Debugging

### evaluate\_script

**Description:** Evaluate a JavaScript function inside the currently selected page. Returns the response as JSON so returned values have to JSON-serializable.

**Parameters:**

- **args** (array) *(optional)*: An optional list of arguments to pass to the function.
- **function** (string) **(required)**: A JavaScript function declaration to be executed by the tool in the currently selected page. Example without arguments: `() => { return document.title }` or `async () => { return await fetch("example.com") }`. Example with arguments: `(el) => { return el.innerText; }`

---

### get\_console\_message

**Description:** Gets a console message by its ID. You can get all messages by calling [`list_console_messages`](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/#list_console_messages).

**Parameters:**

- **msgid** (number) **(required)**: The msgid of a console message on the page from the listed console messages

---

### list\_console\_messages

**Description:** List all console messages for the currently selected page since the last navigation.

**Parameters:**

- **includePreservedMessages** (boolean) *(optional)*: Set to true to return the preserved messages over the last 3 navigations.
- **pageIdx** (integer) *(optional)*: Page number to return (0-based). When omitted, returns the first page.
- **pageSize** (integer) *(optional)*: Maximum number of messages to return. When omitted, returns all requests.
- **types** (array) *(optional)*: Filter messages to only return messages of the specified resource types. When omitted or empty, returns all messages.

---

### take\_screenshot

**Description:** Take a screenshot of the page or element.

**Parameters:**

- **filePath** (string) *(optional)*: The absolute path, or a path relative to the current working directory, to save the screenshot to instead of attaching it to the response.
- **format** (enum: "png", "jpeg", "webp") *(optional)*: Type of format to save the screenshot as. Default is "png"
- **fullPage** (boolean) *(optional)*: If set to true takes a screenshot of the full page instead of the currently visible viewport. Incompatible with uid.
- **quality** (number) *(optional)*: Compression quality for JPEG and WebP formats (0-100). Higher values mean better quality but larger file sizes. Ignored for PNG format.
- **uid** (string) *(optional)*: The uid of an element on the page from the page content snapshot. If omitted takes a pages screenshot.

---

### take\_snapshot

**Description:** Take a text snapshot of the currently selected page based on the a11y tree. The snapshot lists page elements along with a unique identifier (uid). Always use the latest snapshot. Prefer taking a snapshot over taking a screenshot.

**Parameters:**

- **filePath** (string) *(optional)*: The absolute path, or a path relative to the current working directory, to save the snapshot to instead of attaching it to the response.
- **verbose** (boolean) *(optional)*: Whether to include all possible information available in the full a11y tree. Default is false.

---

