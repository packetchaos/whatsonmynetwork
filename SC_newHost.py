from tenable.sc import TenableSC
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def get_info():
    # Set User data
    hostname = ""
    username = ""
    password = ""

    # Set SC object
    sc = TenableSC(hostname)

    # login to SC
    sc.login(username, password)

    # Get data
    # check Development tools in chrome -> Network tab --> Under Name, choose analysis --> Headers tab --> Request Payload
    # EXAMPLE: sc.analysis.vulns(('pluginID', '=', '19506'), ('firstSeen', '=', '0:60'),('repository','=',[{"id" : "1"}]), tool='sumip')

    current_devices = []

    for device in sc.analysis.vulns(('lastSeen','=','0:30'), tool='sumip'):
        current_devices.append(device)

    # logout of SC
    sc.logout()

    return render_template('index.html', current_devices=current_devices)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
