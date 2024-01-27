from mp_api.client import MPRester

MAPI_KEY = ""  # Your Materials Project Key here
with MPRester(api_key=MAPI_KEY) as mpr:
    # retrieve SummaryDocs for a list of materials
    docs = mpr.summary.search(material_ids=["mp-2534", "mp-406"])
