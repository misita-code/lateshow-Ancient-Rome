📺 Late Show API
A simple RESTful API for managing TV show episodes, guests, and their appearances. Built using Flask, SQLAlchemy, and Flask-Migrate.

🚀 Features
View all episodes and guests.

View details of a specific episode, including guest appearances.

Create a new guest appearance in an episode with a rating.

Validations for guest appearances (rating range, presence of related episode and guest).

🛠 Tech Stack
Flask — Web framework

SQLAlchemy — ORM for database management

Flask-Migrate — Handle database migrations

SQLite — Lightweight database used for development

📂 Project Structure
graphql
Copy
Edit
.
├── app.py               # Main application file with route definitions
├── models.py            # Database models for Episode, Guest, Appearance
├── database.db          # SQLite database file (after running migrations)
└── migrations/          # Auto-generated DB migration scripts
📦 Installation & Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/late-show-api.git
cd late-show-api
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Initialize the database:

bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the app:

bash
Copy
Edit
flask run
App will run on http://127.0.0.1:5000

📬 API Endpoints
📺 Episodes
GET /episodes — List all episodes

GET /episodes/<id> — Get one episode with its guest appearances

👤 Guests
GET /guests — List all guests

🎤 Appearances
POST /appearances — Create a new appearance
Body Example (JSON):

json
Copy
Edit
{
  "rating": 4,
  "episode_id": 1,
  "guest_id": 2
}
✅ Validations
rating must be between 1 and 5

episode_id and guest_id must refer to existing records

Errors return JSON with descriptive messages

🧪 Testing
Use Postman or curl to test API endpoints.

📌 Notes
Ensure the database is migrated before running the app.

Make sure models.py defines .to_dict() methods for serialization.

📄 License
MIT License. Feel free to use, modify, and share.

