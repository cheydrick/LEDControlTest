from flask import Flask, render_template, url_for, jsonify

log_messages = []

try:
    from gpiozero import LED
    led = LED(17)
    gpio_enabled = True
except:
    gpio_enabled = False
    log_messages.append("Couldn't load gpiozero library")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on')
def on():
    print("LED is being turned on.")
    log_messages.append("Turning On")
    if gpio_enabled:
        led.on()
    return jsonify('ON')

@app.route('/off')
def off():
    print("LED is being turned off.")
    log_messages.append("Turning Off")
    if gpio_enabled:
        led.off()
    return jsonify('OFF')

@app.route('/log')
def log():
    print("Sending log data")
    return_string = ''
    if len(log_messages) == 0:
        return ''
    for i in log_messages:
        return_string += i + '<br>'
    return return_string