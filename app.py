from flask import Flask
from insurance_management_system.routes import insurance_management_system_bp

import sys

app = Flask(__name__)


app.register_blueprint(insurance_management_system_bp)


if __name__ == '__main__':
    #DO not remove any Code below
    port = int(sys.argv[1])
    app.run(debug=True, host="0.0.0.0", port=port)
