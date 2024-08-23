from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def load_data():
    # Load data from code_base.json
    json_file_path = "C:/Users/nisha/OneDrive/Desktop/jinja/apps/code_base.json"  # Forward slashes
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

@app.route('/')
def index():
    tab = request.args.get('tab', 'functions')  # Default to 'functions' tab

    # Load data from JSON file
    data = load_data()
    functions = data.get('functions', [])
    files = data.get('files', [])

    # Render the appropriate template based on the tab parameter
    rendered_html = render_template(
        'index.html',
        title='Project Overview',
        tab=tab,
        functions=functions if tab == 'functions' else [],
        files=files if tab == 'files' else []
    )

    # Paths to save the rendered HTML files
    functions_output_path = "C:/Users/nisha/OneDrive/Desktop/jinja/apps/templates/main_page.html"
    files_output_path = "C:/Users/nisha/OneDrive/Desktop/jinja/apps/templates/files_page.html"

    # Save the rendered HTML for the current tab
    if tab == 'functions':
        with open(functions_output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)
    elif tab == 'files':
        with open(files_output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_html)

    # Return the rendered HTML to be displayed in the browser
    return rendered_html

if __name__ == '__main__':
    app.run(debug=True)
