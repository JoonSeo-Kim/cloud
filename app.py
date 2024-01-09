from flask import Flask, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/numericalintegralservice/<lower>/<upper>', methods=['GET'])
def numerical_integral_service(lower, upper):
    lower = float(lower)
    upper = float(upper)        
    def numerical_integration(l, u, N):
        dx = (u - l) / N
        return sum(abs(np.sin(l + i * dx)) * dx for i in range(N))

    intervals = [10, 100, 1000, 10000, 100000, 1000000]
    results = {N: numerical_integration(lower, upper, N) for N in intervals}

    return jsonify(results)

@app.route('/')
def hi():
    return 'Microservice'

if __name__ == '__main__':
    app.run(debug=True)
