# Inventory Application
To demonstrate the power of FastAPI, I built a **REST API** for a hypothetical inventory application. This API will be connected to a database, support image uploads, and have protected routes. 
This API will have the following endpoints:
- `GET /items` - To fetch all the items stored on the server
- `GET /items/{item_id}` - to get a specific item from the server
- `POST /items` - to get add a new item to our server
- `PATCH /items/{item_id}` - to update the item on the server
- `DELETE /items/{item_id}` - to delete an item from the inventory

## Project requirements and Packages
- All the packages and their versions are well document in [requirements.txt](./requirements.txt)
- the user who cloned the repo can simply get the latest package version by:
    ```bash
    pip install -r requirements.txt
    ```
