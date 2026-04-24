import os
from flask import Flask, send_from_directory, render_template_string, abort

app = Flask(__name__)

REPO_ROOT = os.path.abspath(os.path.dirname(__file__))

def get_html_apps():
    """finds all .html files in the repository (cuz I'll be adding more apps and me lazy to hardcode)"""
    html_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'venv']
        
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, REPO_ROOT)
                html_files.append(rel_path)
    return sorted(html_files)

@app.route('/')
def index():
    """Renders a simple dashboard listing all discovered HTML applications."""
    apps = get_html_apps()
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Da "backend", if you dint make this table, you're not supposed to be here</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; padding: 40px; background-color: #f8f9fa; color: #333; }
            h1 { color: #212529; border-bottom: 2px solid #dee2e6; padding-bottom: 10px; }
            ul { list-style-type: none; padding: 0; }
            li { background: white; margin: 8px 0; padding: 12px; border-radius: 4px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
            a { text-decoration: none; color: #007bff; font-weight: 500; }
            a:hover { color: #0056b3; text-decoration: underline; }
            .path { color: #6c757d; font-size: 0.9em; margin-left: 10px; }
        </style>
    </head>
    <body>
        <h1>Da Apps, you might wanna just click on index.html</h1>
        <ul>
            {% for app in apps %}
                <li><a href="/{{ app }}">{{ app.split('/')[-1] }}</a> <span class="path">({{ app }})</span></li>
            {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(html_template, apps=apps)

@app.route('/<path:filename>')
def serve_app(filename):
    return send_from_directory(REPO_ROOT, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
