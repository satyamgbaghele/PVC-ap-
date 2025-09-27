"""
Web conversion of the original Tkinter PVC Production Calculator.

This file now implements a small Flask web app that exposes the same
calculations through a friendly HTML/CSS frontend located in
`templates/index.html` and `static/styles.css`.

Run with:
    python clculationsheet.py

Open http://127.0.0.1:5000 in your browser.
"""

from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


def compute_values(PVC, PE, PVDC, weight_kg, single_roll_weight, jumbo_width):
    """Perform the same calculations that were in the original script.

    Returns a dict with computed values or raises ValueError on invalid inputs.
    """
    # Defensive checks
    if PVC <= 0:
        raise ValueError("PVC must be greater than 0")
    if jumbo_width <= 0:
        raise ValueError("Jumbo width must be greater than 0")

    # PVC GSM = (C2*1.35)/1000
    PVC_GSM = (PVC * 1.35) / 1000

    # Total GSM = (C2*1.35 + C3*0.92 + C4*1)/1000
    Total_GSM = (PVC * 1.35 + PE * 0.92 + PVDC * 1) / 1000
    if Total_GSM == 0:
        raise ValueError("Total GSM computed as zero, check inputs")

    # Extra +10% Considering Wastage = C6 + C6*0.05 (kept formula from original)
    extra_wastage = weight_kg + (weight_kg * 0.05)

    # How much PVC required = (E6/E3)*D3
    PVC_required = (extra_wastage / Total_GSM) * PVC_GSM

    # Jumbo Roll Length = (((K6/(C2/1000)) / (K9/1000)) / 1.35)
    # Protect against division by zero
    if PVC == 0 or jumbo_width == 0:
        raise ValueError("PVC and jumbo width must be non-zero")
    jumbo_length = ((single_roll_weight / (PVC / 1000)) / (jumbo_width / 1000)) / 1.35

    return {
        "PVC_GSM": PVC_GSM,
        "Total_GSM": Total_GSM,
        "extra_wastage": extra_wastage,
        "PVC_required": PVC_required,
        "jumbo_length": jumbo_length,
    }


@app.route('/', methods=('GET', 'POST'))
def index():
    errors = None
    results = None
    # default values for convenience
    defaults = {
        'PVC': '600',
        'PE': '20',
        'PVDC': '5',
        'weight_kg': '100',
        'single_roll_weight': '5',
        'jumbo_width': '1200',
    }

    if request.method == 'POST':
        try:
            # Parse input values from the form
            PVC = float(request.form.get('PVC', defaults['PVC']))
            PE = float(request.form.get('PE', defaults['PE']))
            PVDC = float(request.form.get('PVDC', defaults['PVDC']))
            weight_kg = float(request.form.get('weight_kg', defaults['weight_kg']))
            single_roll_weight = float(request.form.get('single_roll_weight', defaults['single_roll_weight']))
            jumbo_width = float(request.form.get('jumbo_width', defaults['jumbo_width']))

            results = compute_values(PVC, PE, PVDC, weight_kg, single_roll_weight, jumbo_width)
            # Keep form values for re-render
            defaults.update({
                'PVC': str(PVC), 'PE': str(PE), 'PVDC': str(PVDC),
                'weight_kg': str(weight_kg), 'single_roll_weight': str(single_roll_weight),
                'jumbo_width': str(jumbo_width)
            })
        except Exception as exc:
            errors = str(exc)

    return render_template('index.html', inputs=defaults, results=results, errors=errors)


if __name__ == '__main__':
    import os
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # Control debug mode via environment variable FLASK_DEBUG (set to '1' to enable)
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(host='0.0.0.0', port=port, debug=debug)
