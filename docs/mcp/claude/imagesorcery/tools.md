# ImageSorcery MCP Tool Reference

### **1. BASIC OPERATIONS**

#### `get_metainfo`
```markdown
CMD: Get info about [image path]
EXAMPLE: Show me the dimensions of /path/to/screenshot.png
EXAMPLE: What's the file size and format of image.jpg?
```

#### `resize`
```markdown
CMD: Resize [image] to [width]x[height]
EXAMPLE: Resize /path/to/image.png to 1920x1080
EXAMPLE: Scale screenshot.png to 50% (use scale_factor: 0.5)
```

#### `rotate`
```markdown
CMD: Rotate [image] by [degrees]
EXAMPLE: Rotate /path/to/chart.png by 90 degrees clockwise
EXAMPLE: Flip screenshot.png upside down (180 degrees)
```

#### `crop`
```markdown
CMD: Crop [image] from (x1,y1) to (x2,y2)
EXAMPLE: Crop /path/to/screenshot.png from (0,0) to (500,300)
EXAMPLE: Cut out the top-left corner: x1=0, y1=0, x2=400, y2=400
```

---

### **2. DRAWING & ANNOTATION**

#### `draw_rectangles`
```markdown
CMD: Draw [color] rectangle on [image] at coordinates [x1,y1,x2,y2]

EXAMPLE:
Draw a red rectangle on /path/to/screenshot.png:
- Top-left: (100, 100)
- Bottom-right: (400, 300)
- Color: red (BGR: [0, 0, 255])
- Thickness: 3
```

#### `draw_circles`
```markdown
CMD: Draw circle on [image] at center [x,y] with radius [r]

EXAMPLE:
Draw a blue circle on /path/to/image.png:
- Center: (250, 250)
- Radius: 50
- Color: blue (BGR: [255, 0, 0])
- Filled: true
```

#### `draw_arrows`
```markdown
CMD: Draw arrow on [image] from [x1,y1] to [x2,y2]

EXAMPLE:
Draw green arrow pointing to button:
- Start: (100, 100)
- End: (300, 200)
- Color: green (BGR: [0, 255, 0])
- Thickness: 3
```

#### `draw_lines`
```markdown
CMD: Draw line on [image] from [x1,y1] to [x2,y2]

EXAMPLE:
Draw white line:
- Start: (0, 100)
- End: (500, 100)
- Color: white (BGR: [255, 255, 255])
- Thickness: 2
```

#### `draw_texts`
```markdown
CMD: Write "[text]" on [image] at position [x,y]

EXAMPLE:
Add "BUY ZONE" text on /path/to/chart.png:
- Position: (200, 300)
- Color: green (BGR: [0, 255, 0])
- Font size: 2.0
- Thickness: 3
```

---

### **3. IMAGE EFFECTS**

#### `blur`
```markdown
CMD: Blur [areas] in [image]

EXAMPLE:
Blur the background of /path/to/image.png:
- Area: rectangle from (0,0) to (100,100)
- Blur strength: 25

EXAMPLE:
Blur everything EXCEPT the main subject:
- Define subject area: (200,200) to (600,600)
- Set invert_areas: true
```

#### `change_color`
```markdown
CMD: Convert [image] to [grayscale/sepia]

EXAMPLE: Convert /path/to/photo.png to grayscale
EXAMPLE: Apply sepia tone to screenshot.png
```

#### `fill`
```markdown
CMD: Fill [area] of [image] with [color] at [opacity]

EXAMPLE:
Highlight a region in /path/to/screenshot.png:
- Area: rectangle (100,100) to (400,400)
- Color: yellow (BGR: [0, 255, 255])
- Opacity: 0.3 (30% transparent)

EXAMPLE:
Remove background (make transparent):
- Area: polygon [[0,0], [100,0], [100,100], [0,100]]
- Color: null (transparent)
- invert_areas: true (keeps only the subject)
```

---

### **4. OVERLAYS & COMPOSITION**

#### `overlay`
```markdown
CMD: Overlay [image1] on top of [image2] at position [x,y]

EXAMPLE:
Place logo.png on screenshot.png:
- Base image: /path/to/screenshot.png
- Overlay image: /path/to/logo.png
- Position: (50, 50) - top-left corner
- Output: /path/to/result.png
```

---

### **5. OBJECT DETECTION & AI**

#### `detect`
```markdown
CMD: Detect objects in [image] using [model]

EXAMPLE:
Detect all buttons and UI elements in /path/to/screenshot.png:
- Model: yoloe-11l-seg-pf.pt
- Return masks: true
- Confidence threshold: 0.5

RETURNS: List of detected objects with bounding boxes and masks
```

#### `find`
```markdown
CMD: Find "[description]" in [image]

EXAMPLE:
Find "red button" in /path/to/screenshot.png

EXAMPLE:
Locate "submit button" in the UI:
- Description: "submit button"
- Return all matches: false (only best match)
- Return geometry: true (get mask/polygon)
```

---

### **6. TEXT EXTRACTION**

#### `ocr`
```markdown
CMD: Extract text from [image]

EXAMPLE:
Read all text from /path/to/document.png:
- Language: en (English)

EXAMPLE:
Extract Russian text from screenshot:
- Language: ru
- Returns: text content, confidence, bounding boxes
```

---

### **7. CONFIGURATION**

#### `config`
```markdown
CMD: Show ImageSorcery configuration

CMD: Set detection confidence threshold to 0.7

CMD: Reset configuration to defaults
```

---
