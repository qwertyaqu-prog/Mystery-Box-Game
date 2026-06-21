# 🎁 Mystery Box Game
### A fun interactive web application where players can discover hidden prizes by clicking on mystery boxes! Built with Flask and JavaScript.

## 📋 Features
- Dynamic Categories: Create, edit, and delete prize categories

- Interactive Mystery Boxes: Click to reveal hidden prizes with congratulations messages

- Drag & Drop: Rearrange boxes by dragging them to your preferred order

- Shuffle Mode: Randomize box positions for different game experiences

- Image Upload: Upload custom images for each mystery box

- Mobile Responsive: Works on both desktop and mobile devices

- Real-time Updates: No page refresh needed for box interactions

## 🚀 Quick Start
### Prerequisites
- Python 3.7 or higher

- pip (Python package manager)

### Installation
1. Clone the repository:

```bash
git clone https://github.com/yourusername/mystery-box-game.git
cd mystery-box-game
```
2. Install dependencies:

```bash
pip install flask werkzeug
```
3. Run the application:

```bash
python app.py
```
4. Open your browser and navigate to http://127.0.0.1:5000

## 🎮 How to Use
### Player View
1. Select a category from the dropdown menu

2. Click on any box to reveal its content

3. A congratulations message will appear with the prize

### Admin Panel
Access the admin panel at http://127.0.0.1:5000/admin

Managing Categories
- Add Category: Creates a new category with default settings

- Edit Category: Change category name, congratulations message

- Delete Category: Remove entire category and its boxes

Managing Boxes
- Upload Images: Upload up to 26 images (A-Z) for boxes

- Drag & Drop: Reorder boxes by dragging

- Shuffle: Randomize box positions

## 📁 Project Structure
mystery-box-game/

├── app.py                 # Main Flask application

├── templates/

│   ├── index.html         # Player interface

│   └── admin.html         # Admin panel

├── static/

│   └── uploads/           # Uploaded images directory

├── requirements.txt       # Python dependencies

└── README.md             # This file

## 🛠️ API Endpoints
Endpoint	Method	Description

/api/get_categories	GET	Get all categories

/api/get_boxes/<cat_key>	GET	Get boxes for specific category

/api/update_pos	POST	Update box positions

/api/shuffle	POST	Shuffle boxes in a category

## 📝 File Structure Details
### app.py
The main Flask application handles:

- Route definitions

- Category management

- File uploads

- API endpoints

### index.html
The player interface featuring:

- Category selector

- Grid of mystery boxes

- Congratulations popup

- Box interaction handling

### admin.html
Administrative interface with:

- Category management

- Box image upload

- Drag & drop functionality

- Shuffle controls

## 🔧 Customization
### Changing Default Messages
In app.py, modify the default category structure:

python
```
all_categories = {
    "cat_1": {"name": "PLATINUM", "boxes": [], "msg": "SELAMAT! (PLATINUM)"},
}
```
### Styling
CSS is embedded in the HTML templates. You can customize:

- Box colors and sizes

- Animation effects

- Layout and spacing

- Color schemes

### 📸 Screenshots
Screenshots coming soon

### 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

### 🙏 Acknowledgments
- Built with Flask

- Drag & drop functionality using HTML5 Drag and Drop API

- Icons and styling inspired by modern web design patterns

🐛 Known Issues
- Maximum of 26 boxes per category (limited by A-Z labeling)

- File size limit depends on Flask's default settings

- Drag & drop may have issues on some mobile browsers

- If the uploaded image is blank or the image is damaged, change the image with a sequence number (Ex 1.png, 2.png, 3.png ...)

🔮 Future Improvements
- User authentication system

- Database integration (SQLite/PostgreSQL)

- Export/Import categories

- Statistics and analytics

- Sound effects for box opening

- Timer-based game modes

- Social sharing features

### Made with ❤️ for fun and interactive experiences

