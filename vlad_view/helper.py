from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Type
from config import client


def querying_auditd(doc_type, index, size):
    search = Search(using=client, index=index)
    search.query = Type(value=doc_type)

    response = []
    i = 1

    for hit in search.scan():
        i += 1
        response.append(hit)
        if i > size:
            break

    return response


def parents_to_children(parents_hits, children_hits, par_fields, ch_fields):
    families = {parent.meta.id: [parent[field] for field in par_fields] for parent in parents_hits}

    for child in children_hits:
        parent = child.parent
        if parent in families:
            families[parent].extend(child[field] for field in ch_fields)

    # Dealing with missing fields
    n = max(len(val) for val in families.values())
    for record in families.values():
        m = len(record)
        if m < n:
            record.extend("None" for x in range(n - m))

            # Sorting
    result = [families[id] for id in sorted(families)]

    return result