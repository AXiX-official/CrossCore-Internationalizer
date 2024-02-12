from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://cdn.megagamelog.com/cross/release/ilist.txt":
        flow.request.url = "https://github.com/AXiX-official/CrossCore-Internationalizer/blob/main/ilist.txt"

        # # 对于需要梯子上GitHub的，如果不想每次都要挂梯子到GitHub来获取txt，可更改至本地文件（修改为自己对应本地文件的绝对路径）
        # with open(r"C:\path\to\your\ilist.txt", "r") as file:
        #     content = file.read()

        # # Modify the response
        # flow.response = http.Response.make(
        #     200,  # status code
        #     content,  # content
        #     {"Content-Type": "text/plain"}  # headers
        # )
