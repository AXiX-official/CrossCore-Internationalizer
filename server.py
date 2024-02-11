from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://cdn.megagamelog.com/cross/release/ilist.txt":
        flow.request.url = "https://raw.githubusercontent.com/AXiX-official/CrossCore-Internationalizer/main/ilist.txt"