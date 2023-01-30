from flask import Flask, render_template, request
import json
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    with open('form.json') as json_file:
            form_data = json.load(json_file)
                return render_template('form.html', form_data=form_data)

                @app.route('/add_field', methods=['POST'])
                def add_field():
                    new_field = request.form.get('new_field')
                        with open('form.json') as json_file:
                                form_data = json.load(json_file)
                                    form_data['fields'].append({
                                            'name': new_field,
                                                    'label': new_field,
                                                            'type': 'text',
                                                                    'placeholder': f'Enter the {new_field}',
                                                                            'required': True
                                                                                })
                                                                                    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                                                                                        with open(f'form_{current_date}.json', 'w') as json_file:
                                                                                                json.dump(form_data, json_file)
                                                                                                    return render_template('form.html', form_data=form_data)

                                                                                                    if __name__ == '__main__':
                                                                                                        app.run()
