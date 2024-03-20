from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'split_your_bills_t0_pay_your_bills!' 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/finalize_items', methods=['POST'])
def finalize_items():
    participants_input = request.form.get('participants')
    item_names = request.form.getlist('item_name[]')
    item_costs = request.form.getlist('item_cost[]')

    participants = [name.strip() for name in participants_input.split(',')]
    items = [{"name": name.strip(), "cost": float(cost)} for name, cost in zip(item_names, item_costs)]

    # session storage
    session['participants'] = participants
    session['items'] = items

    # move to enter_shares page
    return redirect(url_for('enter_shares'))


@app.route('/enter_shares', methods=['GET', 'POST'])
def enter_shares():
    if request.method == 'GET':
        participants = session.get('participants', [])
        items = session.get('items', [])

        return render_template('enter_shares.html', participants=participants, items=items)
    else:
        # Extract participants and items from the form
        participants = request.form.getlist('participant_names[]')
        # items_json = request.form.get('items_json')

        # session retrieval
        participants = session.get('participants', [])
        items = session.get('items', [])
        # Initialize a dictionary to store each participant's total share
        person_shares = {participant: 0.0 for participant in participants}

        # Calculate the share of the total bill for each participant
        for item in items:
            item_total_share = 0.0
            for participant in participants:
                share_input_name = f"{participant}_{item['name']}"
                participant_share = float(request.form.get(share_input_name, 0))
                participant_cost = participant_share * item['cost']
                person_shares[participant] += participant_cost
                item_total_share += participant_cost

        # Calculate the total bill from the items
        total_bill = sum(item['cost'] for item in items)
        
        # Calculate the sum of all shares (should be equal to total_bill if correctly divided)
        shares_total = sum(person_shares.values())

        # Pass calculated data to the template
        return render_template('bill_summary.html', person_shares=person_shares, total_bill=total_bill, shares_total=shares_total, participants=participants, items=items)


if __name__ == '__main__':
    app.run(debug=False)
