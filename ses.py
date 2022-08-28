from migrations.main import SessionLocal

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()