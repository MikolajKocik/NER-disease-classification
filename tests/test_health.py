from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health_check_returns_ok():
    """
    Should return ok (200) if service is available
    """
    # Act
    response = client.get("/health")
    
    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok", 
           "service": "medical-entity-recognition-gateway"
    }
