import os
import sys
import random
import webbrowser
from flask import Flask, render_template, request, url_for, redirect, jsonify
from werkzeug.utils import secure_filename

if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

UPLOAD_FOLDER = os.path.join(base_dir, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Data default awal
all_categories = {
    "cat_1": {"name": "PLATINUM", "boxes": [], "msg": "SELAMAT! (PLATINUM)"},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global all_categories
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == "add_category":
            new_id = f"cat_{int(random.random()*1000)}"
            all_categories[new_id] = {"name": "KATEGORI BARU", "boxes": [], "msg": "SELAMAT!"}
            
        elif action == "delete_category":
            cat_key = request.form.get('category_key')
            if cat_key in all_categories:
                del all_categories[cat_key]
                
        elif action == "update_category":
            cat_key = request.form.get('category_key')
            new_msg = request.form.get('congrats_msg')
            new_name = request.form.get('category_name')
            
            if cat_key in all_categories:
                if new_msg: all_categories[cat_key]["msg"] = new_msg
                if new_name: all_categories[cat_key]["name"] = new_name
                
                files = request.files.getlist('files')
                if files and files[0].filename != '':
                    all_categories[cat_key]["boxes"] = []
                    for i, file in enumerate(files[:26]): # Max 26 untuk A-Z
                        if file and file.filename:
                            filename = secure_filename(file.filename)
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f"{cat_key}_{filename}"))
                            all_categories[cat_key]["boxes"].append({
                                "id": i, 
                                "content": f"/static/uploads/{cat_key}_{filename}"
                            })
        return redirect(url_for('admin'))
    return render_template('admin.html', cats=all_categories)

@app.route('/api/get_categories')
def get_categories_menu():
    menu = {k: v['name'] for k, v in all_categories.items()}
    return jsonify(menu)

@app.route('/api/get_boxes/<cat_key>')
def get_boxes(cat_key):
    return jsonify(all_categories.get(cat_key, {"boxes": [], "msg": ""}))

@app.route('/api/update_pos', methods=['POST'])
def update_pos():
    global all_categories
    data = request.json
    cat_key = data.get('cat_key')
    new_order = data.get('new_order')
    if cat_key in all_categories:
        temp_map = {b['id']: b for b in all_categories[cat_key]["boxes"]}
        all_categories[cat_key]["boxes"] = [temp_map[int(id_)] for id_ in new_order if int(id_) in temp_map]
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"}), 400

@app.route('/api/shuffle', methods=['POST'])
def shuffle_api():
    cat_key = request.json.get('cat_key')
    if cat_key in all_categories:
        random.shuffle(all_categories[cat_key]["boxes"])
        return jsonify({"status": "shuffled"})
    return jsonify({"status": "error"}), 400

if __name__ == '__main__':
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=False, host='0.0.0.0', port=5000)