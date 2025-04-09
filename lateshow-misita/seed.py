from app import create_app
from extensions import db
from models.models import Episode, Guest, Appearance

app = create_app()

with app.app_context():
    print("Clearing db...")
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()

    print("Seeding episodes...")
    ep1 = Episode(date="1/11/99", number=1)
    ep2 = Episode(date="1/12/99", number=2)

    print("Seeding guests...")
    g1 = Guest(name="Michael J. Fox", occupation="actor")
    g2 = Guest(name="Sandra Bernhard", occupation="Comedian")
    g3 = Guest(name="Tracey Ullman", occupation="television actress")

    print("Seeding appearances...")
    a1 = Appearance(rating=4, episode=ep1, guest=g1)
    a2 = Appearance(rating=5, episode=ep2, guest=g3)

    db.session.add_all([ep1, ep2, g1, g2, g3, a1, a2])
    db.session.commit()

    print("✅ Done seeding 🌱")
