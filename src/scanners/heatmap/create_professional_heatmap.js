#!/usr/bin/env node
/**
 * PROFESSIONAL COINGLASS HEATMAP CAPTURE
 * Bloomberg Terminal Quality - Trillion-Dollar Platform Worthy
 *
 * Creates pixel-perfect heatmap screenshots with ZERO UI clutter
 * Author: Oracle Dev AI for Vince Quant Whale Empire
 */

const playwright = require('playwright');
const path = require('path');

async function createProfessionalHeatmap(coin = 'BTC', timeframe = '24h') {
    console.log('🐋 VINCE QUANT WHALE EMPIRE - PROFESSIONAL HEATMAP CREATOR');
    console.log('═══════════════════════════════════════════════════════════');
    console.log(`Coin: ${coin}`);
    console.log(`Timeframe: ${timeframe}`);
    console.log('Quality Target: Bloomberg Terminal Level\n');

    const browser = await playwright.chromium.launch({
        headless: true,
        args: ['--no-sandbox']
    });

    const context = await browser.newContext({
        viewport: { width: 2560, height: 1440 },
        deviceScaleFactor: 2  // High DPI for crisp output
    });

    const page = await context.newPage();

    try {
        console.log('[1/8] Navigating to CoinGlass...');
        await page.goto('https://www.coinglass.com/pro/futures/LiquidationHeatMapNew', {
            waitUntil: 'networkidle',
            timeout: 30000
        });

        console.log('[2/8] Waiting for initial load...');
        await page.waitForTimeout(3000);

        console.log('[3/8] Dismissing cookie popup...');
        try {
            // Look for "Consent" button
            const consentButton = await page.locator('button:has-text("Consent")').first();
            if (await consentButton.isVisible()) {
                await consentButton.click();
                console.log('  ✅ Cookie popup dismissed');
                await page.waitForTimeout(2000);
            }
        } catch (e) {
            console.log('  ℹ️  No cookie popup found (already dismissed)');
        }

        console.log('[4/8] Dismissing promo banner...');
        try {
            // Look for X button on promo banner
            const closeButton = await page.locator('button[aria-label="Close"], .close-btn, button:has-text("×")').first();
            if (await closeButton.isVisible()) {
                await closeButton.click();
                console.log('  ✅ Promo banner dismissed');
                await page.waitForTimeout(1000);
            }
        } catch (e) {
            console.log('  ℹ️  No promo banner to dismiss');
        }

        console.log('[5/8] Waiting for heatmap to fully render...');
        await page.waitForTimeout(5000);  // Let heatmap fully load

        console.log('[6/8] Capturing full page screenshot...');
        const screenshotPath = path.join(__dirname, '../../screenshots/raw', `${coin}_${timeframe}_PROFESSIONAL_RAW.png`);
        await page.screenshot({
            path: screenshotPath,
            fullPage: false  // Just viewport, not full scroll
        });
        console.log(`  ✅ Saved: ${screenshotPath}`);

        console.log('[7/8] Measuring heatmap chart coordinates...');
        // The heatmap chart canvas is usually in a specific container
        // We'll measure it precisely
        const chartBounds = await page.evaluate(() => {
            // Find the actual heatmap canvas/container
            // CoinGlass uses a chart container - let's find it
            const chartElements = document.querySelectorAll('canvas, .chart-container, [class*="heatmap"]');

            for (let element of chartElements) {
                const rect = element.getBoundingClientRect();
                // Look for the main chart (usually large width/height)
                if (rect.width > 800 && rect.height > 300) {
                    return {
                        x: rect.left,
                        y: rect.top,
                        width: rect.width,
                        height: rect.height
                    };
                }
            }

            // Fallback: estimate based on typical layout
            return {
                x: 300,
                y: 250,
                width: 1800,
                height: 600
            };
        });

        console.log(`  Chart bounds: x=${chartBounds.x}, y=${chartBounds.y}, w=${chartBounds.width}, h=${chartBounds.height}`);

        console.log('[8/8] Capturing clean chart-only screenshot...');
        const cleanPath = path.join(__dirname, '../../screenshots/cropped', `${coin}_${timeframe}_CLEAN_CHART.png`);
        await page.screenshot({
            path: cleanPath,
            clip: {
                x: chartBounds.x,
                y: chartBounds.y,
                width: chartBounds.width,
                height: chartBounds.height
            }
        });
        console.log(`  ✅ Saved clean chart: ${cleanPath}`);

        console.log('\n✅ SCREENSHOT CAPTURE COMPLETE');
        console.log('═══════════════════════════════════════════════════════════');
        console.log('Next: Run ImageSorcery for MASSIVE annotations\n');

        return {
            rawPath: screenshotPath,
            cleanPath: cleanPath,
            bounds: chartBounds
        };

    } catch (error) {
        console.error('❌ ERROR:', error.message);
        throw error;
    } finally {
        await browser.close();
    }
}

// Run if called directly
if (require.main === module) {
    const coin = process.argv[2] || 'BTC';
    const timeframe = process.argv[3] || '24h';

    createProfessionalHeatmap(coin, timeframe)
        .then((result) => {
            console.log('SUCCESS:', result);
            process.exit(0);
        })
        .catch((error) => {
            console.error('FAILED:', error);
            process.exit(1);
        });
}

module.exports = { createProfessionalHeatmap };
