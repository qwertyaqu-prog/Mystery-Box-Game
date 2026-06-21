🎁 Mystery Box Game
A fun interactive web application where players can discover hidden prizes by clicking on mystery boxes! Built with Flask and JavaScript.

📋 Features
Dynamic Categories: Create, edit, and delete prize categories

Interactive Mystery Boxes: Click to reveal hidden prizes with congratulations messages

Drag & Drop: Rearrange boxes by dragging them to your preferred order

Shuffle Mode: Randomize box positions for different game experiences

Image Upload: Upload custom images for each mystery box

Mobile Responsive: Works on both desktop and mobile devices

Real-time Updates: No page refresh needed for box interactions

🚀 Quick Start
Prerequisites
Python 3.7 or higher

pip (Python package manager)

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/mystery-box-game.git
cd mystery-box-game
Install dependencies:

bash
pip install flask werkzeug
Run the application:

bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000

🎮 How to Use
Player View
Select a category from the dropdown menu

Click on any box to reveal its content

A congratulations message will appear with the prize

Admin Panel
Access the admin panel at http://127.0.0.1:5000/admin

Managing Categories
Add Category: Creates a new category with default settings

Edit Category: Change category name, congratulations message

Delete Category: Remove entire category and its boxes

Managing Boxes
Upload Images: Upload up to 26 images (A-Z) for boxes

Drag & Drop: Reorder boxes by dragging

Shuffle: Randomize box positions

📁 Project Structure
text
mystery-box-game/
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html         # Player interface
│   └── admin.html         # Admin panel
├── static/
│   └── uploads/           # Uploaded images directory
├── requirements.txt       # Python dependencies
└── README.md             # This file
🛠️ API Endpoints
Endpoint	Method	Description
/api/get_categories	GET	Get all categories
/api/get_boxes/<cat_key>	GET	Get boxes for specific category
/api/update_pos	POST	Update box positions
/api/shuffle	POST	Shuffle boxes in a category
📝 File Structure Details
app.py
The main Flask application handles:

Route definitions

Category management

File uploads

API endpoints

index.html
The player interface featuring:

Category selector

Grid of mystery boxes

Congratulations popup

Box interaction handling

admin.html
Administrative interface with:

Category management

Box image upload

Drag & drop functionality

Shuffle controls

🔧 Customization
Changing Default Messages
In app.py, modify the default category structure:

python
all_categories = {
    "cat_1": {"name": "PLATINUM", "boxes": [], "msg": "SELAMAT! (PLATINUM)"},
}
Styling
CSS is embedded in the HTML templates. You can customize:

Box colors and sizes

Animation effects

Layout and spacing

Color schemes

📸 Screenshots
Screenshots coming soon

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Built with Flask

Drag & drop functionality using HTML5 Drag and Drop API

Icons and styling inspired by modern web design patterns

🐛 Known Issues
Maximum of 26 boxes per category (limited by A-Z labeling)

File size limit depends on Flask's default settings

Drag & drop may have issues on some mobile browsers

🔮 Future Improvements
User authentication system

Database integration (SQLite/PostgreSQL)

Export/Import categories

Statistics and analytics

Sound effects for box opening

Timer-based game modes

Social sharing features

Made with ❤️ for fun and interactive experiences