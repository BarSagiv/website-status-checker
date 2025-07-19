from flask import Flask, render_template, request
import subprocess
import platform

app = Flask(__name__)

# List of websites
SITES = [
    "ynet.co.il",
    "google.com",
    "wikipedia.com",
    "example.com",
    "github.com"
]

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT, timeout=7)
        return result
    except subprocess.CalledProcessError as e:
        return f"Command failed:\n{e.output}"
    except subprocess.TimeoutExpired:
        return "Command timed out"

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_site = None
    results = {}

    if request.method == 'POST':
        selected_site = request.form['site']
        system = platform.system()

        # OS-specific commands
        ping_cmd = f"ping -n 3 {selected_site}" if system == "Windows" else f"ping -c 3 {selected_site}"
        nslookup_cmd = f"nslookup {selected_site}"
        tracert_cmd = f"tracert {selected_site}" if system == "Windows" else f"traceroute {selected_site}"
        curl_cmd = f"curl -I http://{selected_site}"

        # Run commands
        results['Ping'] = run_command(ping_cmd)
        results['NSLookup'] = run_command(nslookup_cmd)
        results['Traceroute'] = run_command(tracert_cmd)
        results['Curl'] = run_command(curl_cmd)

    return render_template('index.html', sites=SITES, selected_site=selected_site, results=results)

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
