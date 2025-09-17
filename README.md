# Mini Pricing Calculator

A web-based fuel pricing calculator deployed on Vercel.

## Features

- **Customer Price Tiers**: 14 different tiers with varying discount percentages
- **Multi-Country Support**: South Africa, Zimbabwe, and Botswana
- **Grid Location Pricing**: Coastal vs Inland pricing differences
- **Real-time Calculations**: Instant price calculations
- **Responsive Design**: Works on desktop and mobile devices
- **Minimum Price Protection**: Ensures prices don't fall below threshold

## Deployment

This project is deployed on Vercel as a static website.

### Local Development

1. Clone the repository
2. Open `index.html` in your browser
3. Or use Vercel CLI: `vercel dev`

### Deploy to Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Run: `vercel`
3. Follow the prompts

## Technology Stack

- HTML5
- CSS3 (with CSS Grid and Flexbox)
- Vanilla JavaScript
- Vercel for hosting

## Pricing Logic

The calculator uses the following formula:
```
Final Price = Base Retail Price 
            - Tier Discount 
            + Exchange Rate Adjustment 
            + Local Market Adjustment 
            + Grid Location Adjustment
            
Final Price = Max(Calculated Price, Minimum Price Protection)
```

Built by RUWΔIN KΞLLY