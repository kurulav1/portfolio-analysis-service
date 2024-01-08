from flask import Flask, request, jsonify
import numpy as np
from scipy.stats import norm

app = Flask(__name__)

def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type")

    return price

@app.route('/black_scholes', methods=['GET'])
def calculate():
    try:
        S = float(request.args.get('S'))
        K = float(request.args.get('K'))
        T = float(request.args.get('T'))
        r = float(request.args.get('r'))
        sigma = float(request.args.get('v'))
        option_type = request.args.get('type', default='call', type=str)

        result = black_scholes(S, K, T, r, sigma, option_type)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
