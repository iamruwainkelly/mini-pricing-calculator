from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Configuration constants - Match C# version exactly
BASE_WHOLESALE_PRICE = 18.00
BASE_RETAIL_PRICE = 21.50
MINIMUM_PRICE_FLOOR = 12.00

# Customer tier discounts (1-14)
TIER_DISCOUNTS = {
    1: 15, 2: 14, 3: 13, 4: 12, 5: 11,
    6: 10, 7: 9, 8: 8, 9: 7, 10: 6,
    11: 5, 12: 4, 13: 3, 14: 2
}

# Local market adjustments per country
LOCAL_MARKET_ADJUSTMENTS = {
    'South Africa': 0.00,
    'Zimbabwe': -5.65,
    'Botswana': -6.40
}

# Grid location adjustments
GRID_LOCATION_ADJUSTMENTS = {
    'Coastal': 0.75,
    'Inland': 1.60
}

# Currency conversion rates
CURRENCY_RATES = {
    'South Africa': {'rate': 1.0, 'symbol': 'R', 'currency': 'ZAR'},
    'Zimbabwe': {'rate': 19.97, 'symbol': '$', 'currency': 'USD'},
    'Botswana': {'rate': 1.36, 'symbol': 'P', 'currency': 'BWP'}
}

def calculate_price(customer_tier, country, grid_location):
    """Calculate fuel price based on inputs"""
    
    # Get discount percentage
    discount_percentage = TIER_DISCOUNTS.get(customer_tier, 0) / 100
    tier_discount = BASE_RETAIL_PRICE * discount_percentage
    
    # Get market adjustments
    local_market_adjustment = LOCAL_MARKET_ADJUSTMENTS.get(country, 0)
    grid_adjustment = GRID_LOCATION_ADJUSTMENTS.get(grid_location, 0)
    
    # Calculate final price
    calculated_price = (BASE_RETAIL_PRICE 
                       - tier_discount 
                       + local_market_adjustment 
                       + grid_adjustment)
    
    # Apply minimum price protection
    final_price = max(calculated_price, MINIMUM_PRICE_FLOOR)
    
    return {
        'baseWholesalePrice': BASE_WHOLESALE_PRICE,
        'baseRetailPrice': BASE_RETAIL_PRICE,
        'customerTier': customer_tier,
        'country': country,
        'gridLocation': grid_location,
        'tierDiscountPercentage': discount_percentage,
        'tierDiscount': tier_discount,
        'localMarketAdjustment': local_market_adjustment,
        'gridLocationAdjustment': grid_adjustment,
        'finalPrice': final_price
    }

def format_adjustment(value):
    """Format adjustment values with proper signs"""
    if abs(value) < 0.01:  # Handle zero values
        return f"R{abs(value):.2f}"
    elif value > 0:
        return f"+R{value:.2f}"
    else:
        return f"-R{abs(value):.2f}"

def format_final_price(result):
    """Format final price with currency conversion"""
    country = result['country']
    final_price = result['finalPrice']
    currency_info = CURRENCY_RATES[country]
    
    if country == 'South Africa':
        return f"R{final_price:.2f} ZAR"
    else:
        local_price = final_price / currency_info['rate']
        return f"{currency_info['symbol']}{local_price:.2f} {currency_info['currency']} | R{final_price:.2f} ZAR"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        customer_tier = int(data['customerTier'])
        country = data['country']
        grid_location = data['gridLocation']
        
        # Validate inputs
        if customer_tier < 1 or customer_tier > 14:
            return jsonify({'error': 'Invalid customer tier'}), 400
        
        if country not in LOCAL_MARKET_ADJUSTMENTS:
            return jsonify({'error': 'Invalid country'}), 400
            
        if grid_location not in GRID_LOCATION_ADJUSTMENTS:
            return jsonify({'error': 'Invalid grid location'}), 400
        
        # Calculate price
        result = calculate_price(customer_tier, country, grid_location)
        
        # Format for display
        response = {
            'result': result,
            'formatted': {
                'wholesalePrice': f"R{result['baseWholesalePrice']:.2f}",
                'baseRetailPrice': f"R{result['baseRetailPrice']:.2f}",
                'tierDiscount': f"-R{result['tierDiscount']:.2f}",
                'localMarketAdjustment': format_adjustment(result['localMarketAdjustment']),
                'gridLocationAdjustment': f"+R{result['gridLocationAdjustment']:.2f}",
                'finalPrice': format_final_price(result)
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)