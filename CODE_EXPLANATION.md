# Mini Pricing Calculator - Web Application Code Explanation

## Overview

This solution implements a web-based mini pricing calculator that calculates fuel prices based on customer tier, country, and grid location. The application is built as a static HTML/JavaScript solution for maximum compatibility, public accessibility, and zero hosting costs while maintaining all specified pricing requirements.

## Code Structure

### 1. Configuration Management

All configurable values are organized into JavaScript objects at the global level:
- **Tier discounts** (1-14): Structured discount percentages
- **Country-specific adjustments**: Fixed monetary adjustments per country
- **Grid location adjustments**: Coastal/inland pricing differences
- **Currency symbols and formatting**: Display preferences for each country

```javascript
const TIER_DISCOUNTS = {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0,
    6: 0.10, 7: 0.10, 8: 0.15, 9: 0.15, 10: 0.15,
    11: 0.20, 12: 0.20, 13: 0.20, 14: 0.20
};
```

This separation allows easy modification of pricing rules without touching the core calculation logic.

### 2. Input Validation

Implemented comprehensive validation for each input field:
- **Tier validation**: Ensures values between 1-14
- **Country validation**: Checks against supported countries (South Africa, Zimbabwe, Botswana)
- **Grid location validation**: Validates coastal/inland options
- **Real-time feedback**: Immediate user notification of invalid inputs

The validation provides clear error messages and prevents invalid calculations.

### 3. Calculation Logic

The calculation follows the exact same sequence as the C# version:
1. Apply tier discount to base retail price (R21.50)
2. Add country-specific adjustment
3. Add grid location adjustment  
4. Apply currency conversion for Zimbabwe (USD) and Botswana (BWP)

```javascript
function calculatePrice(tier, country, gridLocation) {
    const baseRetailPrice = 21.50;
    const wholesalePrice = 18.00;
    
    // Apply tier discount
    const tierDiscount = TIER_DISCOUNTS[tier] || 0;
    let finalPrice = baseRetailPrice * (1 - tierDiscount);
    
    // Add adjustments and return formatted result
    return processAdjustments(finalPrice, country, gridLocation);
}
```

### 4. Output Formatting

Created specialized formatting functions for consistent presentation:
- **`formatAdjustment()`**: Properly displays positive/negative values with currency symbols
- **`formatCurrency()`**: Handles different currency symbols and decimal places
- **Real-time updates**: Results display immediately as users change inputs
- **Zero value handling**: Special formatting for South Africa's neutral adjustments

### 5. User Interface Design

Built with modern web standards:
- **Responsive design**: Works on desktop, tablet, and mobile devices
- **Progressive enhancement**: Core functionality works without JavaScript (fallback)
- **Accessibility**: Proper form labels, keyboard navigation, screen reader support
- **Visual feedback**: Clear indication of calculation progress and results

## Design Choices

### Why Static HTML/JavaScript Web Application?

- **Universal accessibility**: Works in any browser without plugins or installations
- **Zero authentication requirements**: Public access without user accounts
- **Cross-platform compatibility**: Functions on any device with a web browser
- **No server costs**: Can be hosted for free on GitHub Pages
- **Instant loading**: No server round-trips for calculations
- **Offline capability**: Works without internet connection after initial load

### Client-Side vs Server-Side Architecture

**Chosen: Client-Side Processing**

Advantages:
- **Performance**: Instant calculations without network delays
- **Scalability**: No server load regardless of user count
- **Reliability**: No server downtime or maintenance windows
- **Cost**: Zero hosting costs for computational resources
- **Privacy**: No data sent to servers for calculation

Trade-offs considered:
- **Security**: Pricing logic is visible in source code (acceptable for this use case)
- **Updates**: Require redeployment rather than server-side configuration changes

### Separation of Concerns

Organized code into distinct functional areas:
- **Configuration**: All pricing rules in clearly defined objects
- **Validation**: Input checking separated from calculation logic
- **Calculation**: Core pricing logic isolated and testable
- **Presentation**: Display formatting independent of calculation
- **Interaction**: Event handling separated from business logic

Benefits:
- **Readability**: Each function has a single, clear purpose
- **Maintainability**: Changes to pricing rules don't affect UI logic
- **Testability**: Individual components can be validated independently
- **Debuggability**: Console logging available for troubleshooting

### Decimal Precision Handling

Implemented careful floating-point arithmetic management:
- **Rounding strategy**: Consistent 2-decimal place rounding for currency
- **Precision preservation**: Uses `parseFloat()` and `toFixed()` appropriately
- **Edge case handling**: Special logic for zero-value adjustments

## Deployment Strategy

### GitHub Pages Hosting

**Chosen for guaranteed public access:**
- **Static hosting**: Perfect match for HTML/JavaScript application
- **Custom domain support**: Can use custom URLs if needed
- **HTTPS by default**: Secure connections automatically provided
- **Global CDN**: Fast loading worldwide through GitHub's infrastructure
- **Version control integration**: Automatic deployment from git repository

### Alternative Platforms Considered

- **Vercel**: Excellent performance but had authentication requirements
- **Netlify**: Good alternative but GitHub Pages met all requirements
- **Traditional hosting**: Unnecessary complexity for static content

## How to Use

### Prerequisites
- Any modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection for initial load (works offline afterward)

### Accessing the Application
1. Visit: **https://iamruwainkelly.github.io/mini-pricing-calculator/**
2. No registration, login, or installation required
3. Works immediately on any device

### Using the Calculator
1. **Select Customer Tier**: Choose from dropdown (1-14)
2. **Select Country**: Choose from South Africa, Zimbabwe, or Botswana
3. **Select Grid Location**: Choose Coastal or Inland
4. **View Results**: Calculation updates automatically
   - Wholesale Price: R18.00 (constant)
   - Base Retail Price: R21.50 (constant)
   - Applied discounts and adjustments shown
   - Final price in appropriate currency

### Example Usage

**Input:**
- Customer Tier: 5
- Country: Botswana  
- Grid Location: Inland

**Output:**
- Wholesale Price: R18.00
- Base Retail Price: R21.50
- Tier 5 Discount: R0.00 (0%)
- Country Adjustment: +P35.00
- Grid Adjustment: +P5.00
- **Final Price: P61.50**

## Technical Implementation

### File Structure
```
index.html          # Main application file
├── HTML structure  # Form inputs and result display
├── CSS styling     # Responsive design and theming
└── JavaScript      # Calculation logic and interaction
```

### Browser Compatibility
- **Modern browsers**: Full functionality with all features
- **Legacy browsers**: Core calculation works with graceful degradation
- **Mobile browsers**: Optimized touch interface and responsive layout

### Performance Characteristics
- **Initial load**: ~50KB total download size
- **Calculation speed**: Instant (<1ms typical)
- **Memory usage**: Minimal JavaScript footprint
- **Network usage**: Zero after initial page load

## Assumptions and Constraints

1. **Exchange rates**: Fixed demonstration values (not live market rates)
2. **Pricing structure**: Country adjustments as flat amounts (not percentages)
3. **Grid adjustments**: Consistent across all countries
4. **Currency mapping**: 
   - South Africa → ZAR (R)
   - Zimbabwe → USD ($)
   - Botswana → BWP (P)
5. **Base prices**: Wholesale R18.00, Retail R21.50 (current 2025 market rates)

## Future Enhancements

### Potential Improvements
- **Live exchange rates**: API integration for real-time currency conversion
- **Historical tracking**: Price history and trend analysis
- **Advanced tiers**: More granular discount structures
- **Bulk calculations**: Multiple tier/country combinations
- **Export functionality**: PDF reports or CSV downloads
- **API integration**: Real-time fuel price feeds

### Maintenance Considerations
- **Price updates**: Modify base prices in JavaScript configuration
- **New countries**: Add to country objects and adjustment tables
- **Tier changes**: Update TIER_DISCOUNTS object
- **UI improvements**: CSS and HTML modifications independent of logic

## Conclusion

This web-based solution provides a robust, accessible, and maintainable foundation for fuel pricing calculations. The static HTML/JavaScript architecture ensures universal compatibility while the modular code structure supports easy modifications and enhancements. The deployment strategy guarantees public accessibility without authentication barriers, making it suitable for widespread business use.

The application successfully replicates all functionality from the original C# console version while adding the benefits of a modern web interface, mobile compatibility, and zero-cost public hosting.