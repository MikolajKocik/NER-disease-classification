from fastapi.testclient import TestClient

from src.api.main import app
from src.api.extensions.dependencies import get_strategy

class FakeStrategy():
    async def predict(self, request):
        return {
            "entities": []
        }
        
def override_strategy():
    return FakeStrategy()

app.dependency_overrides[get_strategy] = override_strategy
client = TestClient(app)

def test_predict_returns_entities():
    response = client.post(
        "/v1/predict",
        json={"text": "Patient has diabetes."}
    )
    
    assert response.status_code == 200
    assert response.json() == {"entities": []}
    
def teardown_module():
    app.dependency_overrides.clear()