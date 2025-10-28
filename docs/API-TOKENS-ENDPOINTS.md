# API Tokens & Endpoint Ledger

## Live Credentials
| Label | Value | Notes |
| --- | --- | --- |
| COINGLASS_API_KEY | 0e0cdf60bc4745aeb7e14532704f8a57 | CoinGlass Pro tier key |
| COINGLASS_REST_BASE | https://open-api-v4.coinglass.com/api | Use for all REST requests |
| COINGLASS_WEBSOCKET | wss://open-ws.coinglass.com/ws-api?cg-api-key=0e0cdf60bc4745aeb7e14532704f8a57 | Subscribe to liquidationOrders, futures_trades feeds |
| BYBIT_API_KEY | cPknlvGxnxsRd1nXav | Bybit REST v5 credential |
| BYBIT_API_SECRET | iTlBxV6XJMwcy0lgMhwRqJwb4Ji7t7CA1Xid | Bybit REST v5 secret |
| BYBIT_REST_BASE | https://api.bybit.com | Live endpoint |
| TELEGRAM_BOT_TOKEN | 8220654602:AAFq31SxR5oBcCcdmJo6-4KBnwkpoJw9qpc | @CryptoWhaleMining_bot |
| TELEGRAM_CHAT_ID | 722324078 | Vincent direct line |
| TELEGRAM_BOT_USERNAME | @CryptoWhaleMining_bot | Bot identity |
| TELEGRAM_API_BASE | https://api.telegram.org | REST entrypoint (append `/bot{TOKEN}`) |

## Affiliate & Revenue Links
| Label | URL |
| --- | --- |
| CoinGlass Pro | https://www.coinglass.com/?ref_code=cryptowhaleapp |
| CoinGlass Heatmap (auto coin) | https://www.coinglass.com/pro/futures/LiquidationHeatMapNew?coin={SYMBOL}&ref_code=cryptowhaleapp |
| Bybit Trade | https://www.bybit.com/trade/usdt/{SYMBOL}USDT?ref=JWNJQWP |
| Bybit Invite | https://www.bybit.com/invite?ref=JWNJQWP |
| AsterDEX | https://www.asterdex.com/en/referral/cE4Abd |
| Bankr Pro | https://bankr.bot/terminal?refCode=P77VUTD7-BNKR |

### Telegram Affiliate Block (use `{SYMBOL}` placeholder)
| Line | Text |
| --- | --- |
| 1 | 🔗 CoinGlass Pro: https://www.coinglass.com/?ref_code=cryptowhaleapp |
| 2 | 🟡 Heatmap: https://www.coinglass.com/pro/futures/LiquidationHeatMapNew?coin={SYMBOL}&ref_code=cryptowhaleapp |
| 3 | 🟣 Bybit (trade): https://www.bybit.com/trade/usdt/{SYMBOL}USDT?ref=JWNJQWP |
| 4 | 🛫 Bybit invite: https://www.bybit.com/invite?ref=JWNJQWP |
| 5 | ⚡ AsterDEX: https://www.asterdex.com/en/referral/cE4Abd |
| 6 | 🤖 Bankr Pro: https://bankr.bot/terminal?refCode=P77VUTD7-BNKR |

## CoinGlass REST Endpoints
### Required Headers
| Header | Value |
| --- | --- |
| accept | application/json |
| CG-API-KEY | 0e0cdf60bc4745aeb7e14532704f8a57 |

### Futures Market Radar
| Endpoint | Function |
| --- | --- |
| /futures/supported-coins | Universe of futures coins |
| /futures/supported-exchange-pairs | Exchange-specific pair list |
| /futures/coins-markets | Coin-level market snapshot |
| /futures/pairs-markets | Pair-level market snapshot |
| /futures/price-change-list | Ranked price velocity |
| /futures/coins-price-change | Coin price change feed |
| /futures/price/history | Historical price for specified exchange, symbol, interval |

### Liquidation Monopoly
| Endpoint | Function |
| --- | --- |
| /futures/liquidation/aggregated-map | Current 7d liquidation fuel (coin view) |
| /futures/liquidation/map | Exchange + pair liquidation band map |
| /futures/liquidation/aggregated-heatmap/model1 | Historical liquidation heatmap (coin, 12h–1y) |
| /futures/liquidation/aggregated-heatmap/model2 | Historical liquidation heatmap (preferred model) |
| /futures/liquidation/aggregated-heatmap/model3 | Historical liquidation heatmap (alt model) |
| /futures/liquidation/heatmap/model1 | Exchange + pair historical heatmap |
| /futures/liquidation/heatmap/model2 | Exchange + pair historical heatmap |
| /futures/liquidation/heatmap/model3 | Exchange + pair historical heatmap |
| /futures/liquidation/aggregated-history | Liquidation history by coin |
| /futures/liquidation/history | Liquidation history by pair |
| /futures/liquidation/order | Recent liquidation orders (7d) |
| /futures/liquidation/coin-list | List of liquidation-supported coins |
| /futures/liquidation/exchange-list | List of exchanges with liquidation coverage |

### Footprint & Net Position
| Endpoint | Function |
| --- | --- |
| /futures/volume/footprint-history | 90d taker buy/sell ladder (Pro tier) |
| /futures/v2/net-position/history | Net long vs short change history |

### Open Interest Stack
| Endpoint | Function |
| --- | --- |
| /futures/open-interest/aggregated-history | Aggregated OI by coin |
| /futures/openInterest/ohlc-history | Exchange + pair OI OHLC |
| /futures/openInterest/ohlc-aggregated-history | Coin aggregated OI OHLC |
| /futures/openInterest/ohlc-aggregated-stablecoin | Stablecoin-settled OI |
| /futures/openInterest/ohlc-aggregated-coin-margin-history | Coin-margined OI |
| /futures/openInterest/exchange-list | Exchange list for OI data |
| /futures/openInterest/exchange-history-chart | Exchange OI history |

### Funding Rate Arsenal
| Endpoint | Function |
| --- | --- |
| /futures/fundingRate/ohlc-history | Funding rate OHLC |
| /futures/fundingRate/oi-weight-ohlc-history | OI-weighted funding series |
| /futures/fundingRate/vol-weight-ohlc-history | Volume-weighted funding series |
| /futures/fundingRate/exchange-list | Exchange list for funding |
| /futures/fundingRate/accumulated-exchange-list | Accumulated funding per exchange |
| /futures/fundingRate/arbitrage | Funding arbitrage snapshots |

### Long/Short & Taker Volume Matrix
| Endpoint | Function |
| --- | --- |
| /futures/global-long-short-account-ratio/history | Global account ratio |
| /futures/top-long-short-account-ratio/history | Top account ratio |
| /futures/top-long-short-position-ratio/history | Top position ratio |
| /futures/taker-buy-sell-volume/exchange-list | Exchange coverage for taker volume |
| /futures/taker-buy-sell-volume/history | Pair-level taker volume history |
| /futures/aggregated-taker-buy-sell-volume/history | Coin-level aggregated taker volume |

### Order Book Gravity
| Endpoint | Function |
| --- | --- |
| /futures/orderbook/ask-bids-history | Pair-level order book history |
| /futures/orderbook/aggregated-ask-bids-history | Coin-level aggregated depth |
| /futures/orderbook/history | Order book heatmap |
| /futures/orderbook/large-limit-order | Current large limit orders |
| /futures/orderbook/large-limit-order-history | Historical large limit orders |

### Hyperliquid Whale Radar
| Endpoint | Function |
| --- | --- |
| /hyperliquid/whale-alert | Whale alert feed |
| /hyperliquid/whale-position | Whale positioning |
| /hyperliquid/position | Current Hyperliquid position snapshot |

### Spot Market Mirrors
| Endpoint | Function |
| --- | --- |
| /spot/supported-coins | Spot coin list |
| /spot/supported-exchange-pairs | Spot pair list |
| /spot/coins-markets | Spot coin market snapshot |
| /spot/pairs-markets | Spot pair market snapshot |
| /spot/price/history | Spot price history |
| /spot/orderbook/ask-bids-history | Spot order book history |
| /spot/orderbook/aggregated-ask-bids-history | Spot aggregated depth |
| /spot/orderbook/history | Spot order book heatmap |
| /spot/orderbook/large-limit-order | Spot large limit orders |
| /spot/orderbook/large-limit-order-history | Spot large order history |
| /spot/taker-buy-sell-volume/history | Spot taker volume history |
| /spot/aggregated-taker-buy-sell-volume/history | Aggregated spot taker volume |

### Options Intelligence
| Endpoint | Function |
| --- | --- |
| /option/max-pain | Max pain levels |
| /option/info | Options contract metadata |
| /option/exchange-oi-history | Options OI history |
| /option/exchange-vol-history | Options volume history |

### On-Chain Exchange Flows
| Endpoint | Function |
| --- | --- |
| /exchange/assets | Exchange asset overview |
| /exchange/balance/list | Exchange balance list for symbol |
| /exchange/balance/chart | Exchange balance chart |
| /exchange/chain/tx/list | Exchange chain transactions (min USD filter) |

### ETF & Grayscale Command Center
| Endpoint | Function |
| --- | --- |
| /etf/bitcoin/list | Bitcoin ETF list |
| /etf/bitcoin/net-assets/history | Bitcoin ETF net assets |
| /etf/bitcoin/flow-history | Bitcoin ETF flows |
| /etf/bitcoin/premium-discount/history | Bitcoin ETF premium/discount |
| /etf/bitcoin/history | Bitcoin ETF performance |
| /etf/bitcoin/price/history | Bitcoin ETF price history |
| /etf/bitcoin/detail | Bitcoin ETF detail |
| /etf/ethereum/list | Ethereum ETF list |
| /etf/ethereum/net-assets/history | Ethereum ETF net assets |
| /etf/ethereum/flow-history | Ethereum ETF flows |
| /hk-etf/bitcoin/flow-history | Hong Kong ETF flows |
| /grayscale/holdings-list | Grayscale holdings list |
| /grayscale/premium-history | Grayscale premium history |

### Macro & Stablecoin Surveillance
| Endpoint | Function |
| --- | --- |
| /futures/rsi/list | RSI readings |
| /futures/basis/history | Futures basis history |
| /borrow-interest-rate/history | Borrow interest rate history |
| /coinbase-premium-index | Coinbase premium index |
| /index/fear-greed-history | Fear and Greed index |
| /index/stableCoin-marketCap-history | Stablecoin market cap (USDC monitor) |
| /index/ahr999 | AHR999 indicator |
| /index/puell-multiple | Puell Multiple |
| /index/stock-to-flow | Stock-to-Flow |
| /index/pi-cycle | Pi Cycle top/bottom |

### AUX Quick Calls
| Endpoint | Function |
| --- | --- |
| /futures/coins-price-change | Coin price change summary |
| /futures/rsi/list | RSI list (duplicate for quick access) |

### WebSocket Streams
| Endpoint | Function |
| --- | --- |
| wss://open-ws.coinglass.com/ws-api?cg-api-key=0e0cdf60bc4745aeb7e14532704f8a57 | Subscribe with payloads such as `{ "op": "subscribe", "args": ["liquidationOrders", "futures_trades@binance_BTCUSDT@1000000"] }`; ping every 20 seconds |

## Bybit REST Highlights (use X-BAPI headers)
### Required Headers
| Header | Value |
| --- | --- |
| X-BAPI-API-KEY | cPknlvGxnxsRd1nXav |
| X-BAPI-SIGN | Signature per request |
| X-BAPI-TIMESTAMP | Milliseconds timestamp |
| X-BAPI-RECV-WINDOW | Optional window (default 5000) |

| Endpoint | Function |
| --- | --- |
| /v5/order/create | Place order |
| /v5/order/create-batch | Batch place orders (scaling ladders) |
| /v5/order/cancel | Cancel order |
| /v5/order/cancel-all | Cancel all symbol orders |
| /v5/order/list | Order history |
| /v5/position/list | Position info |
| /v5/account/wallet-balance | Wallet balance |
| /v5/market/tickers | Market tickers |
| /v5/market/kline | Candlestick data |
| /v5/market/instruments-info | Instrument metadata |

## Telegram Bot REST
### Required Fields
| Field | Value |
| --- | --- |
| Base URL | https://api.telegram.org/bot{TOKEN} |
| chat_id | 722324078 |

| Endpoint | Function |
| --- | --- |
| /sendMessage | Send text message |
| /sendPhoto | Send photo (heatmap screenshots) |
| /editMessageText | Edit existing message |
| /deleteMessage | Delete message |

---

Keep this ledger synchronized with `zzzchatgptdesktop1111.md` and update immediately when any key, link, or endpoint changes.

## Parameter Notes
| Parameter | Accepted Values | Notes |
| --- | --- | --- |
| symbol | BTC, ETH, SOL, BTCUSDT, etc. | Coin for aggregated calls; pair for exchange-specific calls |
| exchange | Binance, Bybit, OKX, Hyperliquid, etc. | Required for exchange-scoped endpoints |
| interval | 1m,3m,5m,15m,30m,1h,4h,6h,8h,12h,1d,1w | Check endpoint-specific support |
| range | 12h,24h,3d,7d,30d,90d,180d,1y | Liquidation heatmaps/maps |
| limit | Up to 1000 | History endpoints default to 1000 |
| min_liquidation_amount | USD value | Filter for `/futures/liquidation/order` |
| exchange_list | Comma-separated exchanges | Used for aggregated taker endpoints |

## Documentation Links
| Resource | URL | Notes |
| --- | --- | --- |
| CoinGlass API Reference | https://docs.coinglass.com | Endpoint details, rate limits, auth |
| CoinGlass WebSocket Guide | https://docs.coinglass.com/reference/websocket-api | Channel specs & payloads |
| Bybit REST v5 Docs | https://bybit-exchange.github.io/docs/v5/intro | REST authentication & endpoints |
| Bybit WebSocket v5 Docs | https://bybit-exchange.github.io/docs/v5/ws/public/intro | WebSocket channels & heartbeats |
| Telegram Bot API | https://core.telegram.org/bots/api | Methods, parameters, rate limits |
| Telegram Bot FAQ | https://core.telegram.org/bots/faq | Bot management, best practices |
