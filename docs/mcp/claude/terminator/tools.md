# Terminator MCP Tool Reference

### **1. APPLICATION CONTROL**

#### `open_application`
```markdown
CMD: Open [application name]
EXAMPLE: Open Chrome
EXAMPLE: Open Telegram Desktop
EXAMPLE: Launch Visual Studio Code
```

#### `get_applications_and_windows_list`
```markdown
CMD: Show me all running applications
CMD: List all open windows
CMD: What apps are currently open?
```

#### `activate_element`
```markdown
CMD: Bring [window name] to front
EXAMPLE: Focus the Chrome window
EXAMPLE: Switch to Terminal
```

#### `close_element`
```markdown
CMD: Close [window/dialog name]
EXAMPLE: Close the popup
EXAMPLE: Close Chrome
```

---

### **2. BROWSER CONTROL**

#### `navigate_browser`
```markdown
CMD: Open Chrome and go to [URL]
EXAMPLE: Navigate to https://www.coinglass.com
EXAMPLE: Open Bybit in Chrome: https://app.bybit.com
```

#### `execute_browser_script`
```markdown
CMD: In Chrome, run this JavaScript: [code]
EXAMPLE: Get all the text from the page
EXAMPLE: Click the hidden element with ID "submit-btn"
EXAMPLE: Extract table data from the DOM

CODE TEMPLATE:
(function() {
  // Your JavaScript here
  const data = document.querySelector('.data');
  return JSON.stringify({ result: data.textContent });
})()
```

#### `set_zoom`
```markdown
CMD: Set browser zoom to [percentage]%
EXAMPLE: Zoom to 150%
EXAMPLE: Reset zoom to 100%
EXAMPLE: Zoom out to 50%
```

---

### **3. CLICKING & INTERACTION**

#### `click_element`
```markdown
CMD: Click the [element description]
EXAMPLE: Click the "Connect Wallet" button
EXAMPLE: Click the submit button
EXAMPLE: Click on the first search result
```

#### `invoke_element`
```markdown
CMD: Invoke/activate [element] (more reliable for buttons)
EXAMPLE: Invoke the Login button
EXAMPLE: Trigger the Save button
```

#### `validate_element`
```markdown
CMD: Check if [element] exists on screen
EXAMPLE: Check if the logout button is visible
EXAMPLE: Verify the login dialog is present
```

---

### **4. TYPING & TEXT INPUT**

#### `type_into_element`
```markdown
CMD: Type "[text]" into [field description]
EXAMPLE: Type "vincent@trading.com" into the email field
EXAMPLE: Enter "MyPassword123" in the password box
EXAMPLE: Fill the search box with "Bitcoin liquidations"
```

#### `set_value`
```markdown
CMD: Set [field] value to "[value]"
EXAMPLE: Set the amount field to "1000"
EXAMPLE: Change the price to "45000"
```

---

### **5. KEYBOARD CONTROL**

#### `press_key`
```markdown
CMD: Press [key combination] on [element]
EXAMPLE: Press Enter on the search box
EXAMPLE: Press Tab to move to next field
EXAMPLE: Press Ctrl+A to select all text
```

#### `press_key_global`
```markdown
CMD: Press [key combination] globally
EXAMPLE: Press Alt+Tab to switch windows
EXAMPLE: Press Cmd+Space to open Spotlight
EXAMPLE: Press Ctrl+Shift+I to open DevTools
```

---

### **6. WINDOW MANAGEMENT**

#### `maximize_window`
```markdown
CMD: Maximize [window name]
EXAMPLE: Maximize the Chrome window
```

#### `minimize_window`
```markdown
CMD: Minimize [window name]
EXAMPLE: Minimize all windows
```

#### `get_window_tree`
```markdown
CMD: Show me the UI structure of [window]
EXAMPLE: Get the full UI tree of Chrome
EXAMPLE: Show me all elements in the Telegram window
```

#### `get_focused_window_tree`
```markdown
CMD: Show me the UI of the currently focused window
CMD: What's in the active window right now?
```

---

### **7. SCREENSHOTS & VISUAL**

#### `capture_element_screenshot`
```markdown
CMD: Take a screenshot of [element/window]
EXAMPLE: Screenshot the trading chart
EXAMPLE: Capture the notification popup
EXAMPLE: Take a pic of the entire Chrome window
```

#### `highlight_element`
```markdown
CMD: Highlight [element] with [color] for [duration]
EXAMPLE: Highlight the Buy button in red for 2 seconds
EXAMPLE: Show me where the logout link is
```

---

### **8. SCROLLING & NAVIGATION**

#### `scroll_element`
```markdown
CMD: Scroll [direction] in [element] by [amount]
EXAMPLE: Scroll down 5 times in the main window
EXAMPLE: Scroll to the bottom of the page
EXAMPLE: Scroll right in the trading chart
```

#### `mouse_drag`
```markdown
CMD: Drag from [x1, y1] to [x2, y2]
EXAMPLE: Drag from (100, 200) to (500, 600)
EXAMPLE: Select text by dragging
```

---

### **9. DROPDOWNS & SELECTIONS**

#### `select_option`
```markdown
CMD: Select "[option text]" from [dropdown]
EXAMPLE: Select "USD" from the currency dropdown
EXAMPLE: Choose "Last 24 Hours" from the time filter
```

#### `list_options`
```markdown
CMD: Show me all options in [dropdown]
EXAMPLE: List all available currencies
EXAMPLE: What options are in the timeframe selector?
```

#### `set_selected`
```markdown
CMD: Select [item] in [list/calendar]
EXAMPLE: Select the date October 27th
EXAMPLE: Choose the first option in the list
```

---

### **10. TOGGLES & CHECKBOXES**

#### `set_toggled`
```markdown
CMD: Turn [checkbox/toggle] ON/OFF
EXAMPLE: Enable the "Remember Me" checkbox
EXAMPLE: Turn off notifications toggle
EXAMPLE: Check the "Accept Terms" box
```

#### `is_toggled`
```markdown
CMD: Check if [toggle] is ON or OFF
EXAMPLE: Is the auto-trade toggle enabled?
EXAMPLE: Check if notifications are on
```

---

### **11. SLIDERS & RANGE INPUTS**

#### `set_range_value`
```markdown
CMD: Set [slider] to [value]
EXAMPLE: Set volume slider to 75
EXAMPLE: Adjust risk level to 50%
```

#### `get_range_value`
```markdown
CMD: Get current value of [slider]
EXAMPLE: What's the current volume level?
```

---

### **12. WAITING & TIMING**

#### `wait_for_element`
```markdown
CMD: Wait until [element] appears/is ready
EXAMPLE: Wait for the "Trade Complete" message
EXAMPLE: Wait until the loading spinner disappears
EXAMPLE: Hold until the chart loads
```

#### `delay`
```markdown
CMD: Wait [X] seconds before next action
EXAMPLE: Pause for 3 seconds
EXAMPLE: Delay 5000ms (5 seconds)
```

---

### **13. ADVANCED - WORKFLOWS**

#### `execute_sequence`
```markdown
CMD: Run this automated workflow: [steps]

EXAMPLE:
Execute this sequence:
1. Open Chrome
2. Navigate to app.bybit.com
3. Wait for page to load
4. Click "Connect Wallet"
5. Take screenshot
6. If error occurs, retry 3 times
```

#### `run_command`
```markdown
CMD: Execute this code: [JavaScript/Python]

JAVASCRIPT EXAMPLE:
Run this JavaScript code with desktop SDK access:
const apps = await desktop.locator('role:Window').all(5000);
return apps.length;

PYTHON EXAMPLE:
Run this Python code:
print("Hello from Python")
```

---
