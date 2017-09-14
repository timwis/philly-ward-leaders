import json

from contentful_management import Client
from tqdm import tqdm

def process_import(filepath, space_id, content_type_id, api_key):
    client = Client(api_key)
    space = client.entries(space_id)

    with open(filepath) as import_file:
        records = json.load(import_file)

        for record in tqdm(records):
            entry_id = None # tell server to auto-generate it
            entry_data = {
                'content_type_id': content_type_id,
                'fields': {key: {'en-US': value} for (key, value) in record.items()}
            }

            try:
                entry = space.create(entry_id, entry_data)
            except Exception:
                print('Creation failed', json.dumps(record))
            else:
                try:
                    entry.publish()
                except Exception:
                    pass

def process_drop(space_id, content_type_id, api_key):
    client = Client(api_key)
    content_type = client.content_types(space_id).find(content_type_id)
    entries = content_type.entries().all({ 'limit': 1000 })

    for entry in tqdm(entries):
        if entry.is_published:
            entry.unpublish()

        entry.delete()
