from flask import Flask, render_template, request, jsonify
import random  # For simulating radar signals

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_signal', methods=['POST'])
def generate_signal():
    frequency = float(request.form.get('frequency', 1))
    pulse_width = float(request.form.get('pulse_width', 1))
    
    # Simulate target detection
    num_targets = random.randint(1, 5)  # Simulate detecting 1 to 5 targets
    targets = []
    for _ in range(num_targets):
        target_distance = random.uniform(10, 100)  # Simulated target distance
        target_velocity = random.uniform(-50, 50)  # Simulated target velocity
        targets.append({'distance': target_distance, 'velocity': target_velocity})

    waveform = generate_waveform(frequency, pulse_width)
    return jsonify({'targets': targets, 'waveform': waveform})

def generate_waveform(frequency, pulse_width):
    # Create a simple textual waveform representation
    waveform = "Signal: " + "|".join(["*" for _ in range(int(frequency * 10))]) + f"\nPulse Width: {pulse_width}s"
    return waveform

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
