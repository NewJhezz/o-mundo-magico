from app import app
with app.test_request_context():
    from app import adventures
    print(adventures()[:500])
