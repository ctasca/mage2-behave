from typing import Dict


def dictionary(context) -> Dict:
    cur = context.conn.cursor()
    cur.execute(
        "SELECT code, website_id FROM store"
    )
    stores = cur.fetchall()
    keys = []
    values = []
    for store in stores:
        keys.append(store[0])
        values.append(store[1])
    return dict(zip(keys, values))
