import pysolr
solr = pysolr.Solr('http://localhost:8983/solr/', always_commit=True,
												 timeout=10)


solr.add([
    {
        "id": "doc_1",
        "title": "A very small test document about elmo",
    }
])