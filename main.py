import json

from flask import Flask, request
from web3 import Web3

from supply import calculate_supply_information

app = Flask(__name__)

WORKLOCK_FINAL_SUPPLY = 225000000000000000000000000  # nunits
SE_FINAL_SUPPLY = 1380688920644254727736959922  # nunits


@app.route('/supply_information', methods=["GET"])
def supply_information():
    parameter = request.args.get('q')

    if parameter is None or parameter == 'est_circulating_supply':
        # the original max supply no longer applies because of Threshold merger
        max_supply = SE_FINAL_SUPPLY

        # no query - return all supply information
        supply_info = calculate_supply_information(max_supply=max_supply,
                                                   current_total_supply=SE_FINAL_SUPPLY,
                                                   worklock_supply=WORKLOCK_FINAL_SUPPLY)
        if parameter is None:
            # return all information
            response = app.response_class(
                response=json.dumps(supply_info),
                status=200,
                mimetype='application/json'
            )
        else:
            # only return est. circulating supply
            est_circulating_supply = supply_info['est_circulating_supply']
            response = app.response_class(
                response=str(est_circulating_supply),
                status=200,
                mimetype='text/plain'
            )
    else:
        # only current total supply requested
        if parameter == 'current_total_supply':
            response = app.response_class(
                response=str(float(Web3.fromWei(SE_FINAL_SUPPLY, 'ether'))),
                status=200,
                mimetype='text/plain'
            )
        else:
            response = app.response_class(
                response=f"Unsupported supply parameter: {parameter}",
                status=400,
                mimetype='text/plain'
            )
    return response
