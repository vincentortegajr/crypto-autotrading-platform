#!/usr/bin/env node
/**
 * Capture the 2-week BTC liquidation heatmap from CoinGlass.
 *
 * Uses Playwright to open the page, switch the timeframe to "2 Weeks",
 * wait for the heatmap to render, and save a screenshot.
 */

const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

async function main() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent:
      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    locale: 'en-US',
    viewport: { width: 1600, height: 900 },
  });
  const page = await context.newPage();

  try {
    await page.goto('https://www.coinglass.com/pro/futures/LiquidationHeatMapNew', {
      waitUntil: 'networkidle',
      timeout: 120_000,
    });

    // Dismiss cookie banner if it appears
    const consentButton = page.locator('.fc-button.fc-cta-consent, .fc-button.fc-data-preferences-accept-all');
    if ((await consentButton.count()) > 0) {
      await consentButton.first().click({ timeout: 10_000 });
      await page.waitForTimeout(1000);
    }

    // Open timeframe selector if necessary and choose 2 Weeks
    const twoWeekOption = page.locator('text=/2\\s*week/i');
    const isVisible = await twoWeekOption.isVisible().catch(() => false);

    if (!isVisible) {
      // Attempt to open dropdown/selector
      const dropdown = page
        .locator('button:has-text("24 hour"), button:has-text("24h"), button:has-text("24-hour")')
        .first();
      if (await dropdown.count()) {
        await dropdown.click();
      } else {
        await page.click('text=/24\\s*H/i', { timeout: 5_000 }).catch(() => undefined);
      }
    }

    await twoWeekOption.waitFor({ timeout: 15_000 });
    await twoWeekOption.first().click();

    // Wait for the heatmap to update by watching for network idleness and a short pause
    await page.waitForTimeout(5000);

    const outputDir = path.resolve('artifacts');
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    await page.screenshot({
      path: 'artifacts/coinglass_liquidation_heatmap_2weeks.png',
      fullPage: true,
    });
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
