# MCP Usage Notes

## 📝 IMPORTANT NOTES

### **IMAGE PATHS**
- Always use FULL absolute paths for images
- Example: `/Users/vincentortegajr/crypto-autotrading-platform/screenshot.png`
- NOT: `~/screenshot.png` or `./screenshot.png`

### **COLOR FORMAT (BGR not RGB)**
- Red: `[0, 0, 255]`
- Green: `[0, 255, 0]`
- Blue: `[255, 0, 0]`
- White: `[255, 255, 255]`
- Black: `[0, 0, 0]`
- Yellow: `[0, 255, 255]`

### **COORDINATES**
- Origin (0,0) is top-left corner
- X increases going right
- Y increases going down
- Example: (100, 200) = 100px from left, 200px from top

### **TERMINATOR BROWSER SCRIPTS**
- Must wrap in IIFE: `(function() { /* code */ })()`
- Always use typeof checks for env variables
- Return JSON stringified results
- Chrome extension required for execute_browser_script

### **TERMINATOR SELECTORS**
- Format: `role:Type|name:Name`
- Example: `role:Button|name:Submit`
- Use numeric ID if name is empty: `#12345`
- Check with `get_window_tree` first to find correct selectors

---

## 🎯 QUICK START COMMANDS

### **"I want to..."**

**Control my computer:**
```
"Click the Submit button in Chrome"
"Open Telegram and send a message"
"Take a screenshot of my trading dashboard"
"Press Ctrl+C to copy selected text"
```

**Process images:**
```
"Annotate this screenshot with a red rectangle"
"Extract all text from this document image"
"Detect buttons in this UI screenshot"
"Blur the sensitive information in this image"
```

**Run workflows:**
```
"Execute this 10-step automation sequence"
"Monitor the website and alert me if price changes"
"Automatically fill this form every hour"
"Take screenshots every 5 minutes"
```

---

**COPY THIS ENTIRE DOCUMENT AND TELL ME WHAT TO DO!** 🚀

I now understand:
- 🖥️ Terminator = Your digital hands (control everything)
- 🎨 ImageSorcery = Your visual editor (create & annotate)
- 🔥 Together = Unstoppable automation + visual proof
