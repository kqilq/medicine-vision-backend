from typing import Dict, List, Optional

class FeatureStore:
    def __init__(self):
        # In-memory database mapping:
        # { medicine_id: [ { "photo_id": str, "descriptors": list } ] }
        self._store: Dict[str, List[dict]] = {}

    def add_photo_features(self, medicine_id: str, photo_id: str, descriptors: list):
        if medicine_id not in self._store:
            self._store[medicine_id] = []
        
        # Remove existing photo descriptor if updating
        self.remove_photo(medicine_id, photo_id)

        self._store[medicine_id].append({
            "photo_id": photo_id,
            "descriptors": descriptors
        })
        print(f"[STORE] Indexed photo '{photo_id}' for medicine '{medicine_id}'.")

    def remove_photo(self, medicine_id: str, photo_id: Optional[str] = None):
        if medicine_id not in self._store:
            return False

        if photo_id:
            self._store[medicine_id] = [
                item for item in self._store[medicine_id] if item["photo_id"] != photo_id
            ]
            print(f"[STORE] Removed photo '{photo_id}' from medicine '{medicine_id}'.")
        else:
            del self._store[medicine_id]
            print(f"[STORE] Purged all photos for medicine '{medicine_id}'.")
        return True

    def get_all_medicines(self):
        return list(self._store.keys())

feature_store = FeatureStore()
