from fastapi.testclient import TestClient
import pytest
from unittest.mock import patch, MagicMock
from src.routers.fbScrapper import scrap_posts
from src.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_scrap_posts():
      response = await client.get("/scrapper/", params={"page_id": "example_page", "email": "example@gmail.com", "example": "your_password"})
      assert response.status_code == 200
      with patch('your_module.get_posts') as mock_get_posts:
        # Mock the return value of get_posts
        mock_get_posts.return_value = [
            {'time': '2023-01-01', 'text': 'Post 1', 'image': 'image1.jpg', 'likes': 10, 'comments': 5, 'shares': 2},
            {'time': '2023-01-02', 'text': 'Post 2', 'image': 'image2.jpg', 'likes': 20, 'comments': 8, 'shares': 3}
        ]

        # Mocking the suppress context manager
        with patch('your_module.suppress') as mock_suppress:
            # Mock the return value of suppress
            mock_suppress.return_value = MagicMock()

            # Call the function
            result = await scrap_posts(page_id='123', email='example@gmail.com', password='example', num_pages=2)

        # Assert the expected behavior based on the mocked data
        assert result == [
            {'time': '2023-01-01', 'text': 'Post 1', 'image': 'image1.jpg', 'likes': 10, 'comments': 5, 'shares': 2},
            {'time': '2023-01-02', 'text': 'Post 2', 'image': 'image2.jpg', 'likes': 20, 'comments': 8, 'shares': 3}
        ]

       # Assert that get_posts was called with the correct arguments
        mock_get_posts.assert_called_once_with(
            page_id='123',
            pages=2,
            credentials=('example@gmail.com', 'example')
        )
        #there will be an error in test because of the creadentials, change exemple with real email and password

@pytest.mark.asyncio
async def test_get_all_posts():
    response = await client.get("/scrapper/get_all_posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Check if the response is a list

