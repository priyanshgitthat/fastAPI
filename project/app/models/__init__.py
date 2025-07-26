from .user_model import Users
from .admin_model import Admin  # ✅ Add this line when you create admin_model.py

from app.database.db import Base  # Central Base

# Now Base.metadata will include all models
