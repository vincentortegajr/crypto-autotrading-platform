# Cleanup Manifest - October 28, 2025

**Date:** October 28, 2025, 4:09 AM
**Session:** Heatmap Verification System Reorganization
**Agent:** Claude Code (Oracle Dev)

---

## 📦 What Was Moved

### 1. Artifacts Folder (`./artifacts/`)
**Count:** 37 PNG files
**Reason:** Old test heatmap files from previous attempts

**Files Include:**
- `coinglass_liquidation_heatmap_2weeks_*.png` (4 variants)
- `heatmap_chrome_devtools_*` (16 test files)
- `heatmap_playwright_mcp_*` (17 test files)

**New Location:** Organized tests should go in `src/scanners/heatmap/outputs/screenshots/`

**Safe to Delete:** Yes, after 7 days if new system works

---

### 2. Screenshots Folder (`./screenshots/`)
**Count:** 46 PNG files
**Reason:** Scattered screenshots from initial development

**Structure Moved:**
```
screenshots/
├── annotated/
│   ├── BTC_FINAL_STEP1.png
│   ├── BTC_24h_PROFESSIONAL_STEP1.png
│   └── BTC_24h_PROFESSIONAL_STEP2.png
├── cropped/
├── social/
│   ├── BTC_PROFESSIONAL_MARGINS.png
│   ├── BTC_PROFESSIONAL_MARGINS_VIEW.png
│   ├── BTC_FINAL_SIMPLE.png
│   └── BTC_FINAL_SIMPLE_VIEW.png
└── Various test screenshots
```

**New Location:** `src/scanners/heatmap/outputs/screenshots/`

**Safe to Delete:** After 7 days - verify new structure has all needed files

---

### 3. Src Screenshots Folder (`./src/screenshots/`)
**Count:** ~10 files
**Reason:** Temporary test screenshots

**New Location:** `src/scanners/heatmap/outputs/screenshots/clean/`

**Safe to Delete:** Yes, after 7 days

---

## 📊 Summary

| Category | Files Moved | Disk Space | Status |
|----------|-------------|------------|--------|
| Artifacts | 37 | ~15 MB | Test files |
| Screenshots | 46 | ~25 MB | Old attempts |
| Src Screenshots | ~10 | ~8 MB | Temp files |
| **TOTAL** | **~93** | **~48 MB** | Ready to delete after review |

---

## ✅ Verification Checklist

Before permanently deleting this folder:

- [ ] New structure at `src/scanners/heatmap/outputs/` working correctly
- [ ] Can verify BTC 24h successfully
- [ ] All needed screenshots preserved in new location
- [ ] No references to old paths in code
- [ ] At least 7 days have passed
- [ ] Vincent has reviewed and approved deletion

---

## 🔄 Recovery Instructions

If you need any of these files back:

```bash
# Copy entire folder back
cp -r .trashbin/2025-10-28_heatmap-cleanup/screenshots_old ./screenshots

# Or copy specific file
cp .trashbin/2025-10-28_heatmap-cleanup/screenshots_old/annotated/BTC_FINAL_STEP1.png ./somewhere/
```

---

## 🗑️ Permanent Deletion

When ready to permanently delete (after 7+ days):

```bash
# Review contents first
ls -lR .trashbin/2025-10-28_heatmap-cleanup/

# Then delete
rm -rf .trashbin/2025-10-28_heatmap-cleanup/

# Or move to external backup
mv .trashbin/2025-10-28_heatmap-cleanup/ ~/Desktop/backup-before-delete/
```

---

## 📝 Notes

**Why These Files Were Created:**
- Multiple attempts to get box alignment correct (failed 4 times)
- Testing Chrome DevTools vs Playwright MCP
- Testing different timeframes (12h, 24h, 2weeks)
- Iterating on annotation styles

**Lessons Learned:**
- Don't annotate blind (need to see while drawing)
- Programmatic color detection needed
- Proper organization from start saves cleanup time

**New Best Practices:**
- All outputs go to `src/scanners/heatmap/outputs/`
- Use dated filenames: `BTC_24h_2025-10-28_0355.png`
- Keep test files organized in proper folders

---

**This folder can be safely deleted after November 4, 2025 (7 days)**

---

**Moved by:** Claude Code
**Approved by:** Vincent (review required)
**Status:** Ready for review
