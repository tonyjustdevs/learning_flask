from flask import Flask, make_response, jsonify, request

app = Flask(__name__)

@app.route('/inspect')
def inspect_response():
    data = {"hello": "world"}
    response = make_response(jsonify(data))
    response.status_code = 202
    response.headers['X-Custom-Header'] = 'TonysCustomHeaderValue'
    response.set_cookie('tony_test_cookie', 'tony_cookie_value')

    # You can print to the console or return debug info
    print("Status:", response.status)
    print()
    print("Headers list:", list(response.headers))
    print("Headers:", len(response.headers))
    
    print("Data:", response.get_data(as_text=True))
    print("Cookies:", response.headers.getlist('Set-Cookie'))

    # return jsonify(data)
    return response


@app.route('/debug')
def debug():
    response = make_response("Some Tony Custom String Content", 201)
    response.headers['X-Debug'] = 'true'
    response.set_cookie('debug_cookie1', 'enabled')
    response.set_cookie('debug_cookie2', 'enabled')

    debug_info = {
        "status": response.status,
        "headers": dict(response.headers),
        "body": response.get_data(as_text=True),
        "cookies": response.headers.getlist('Set-Cookie')
    }

    return jsonify(debug_info)

@app.route('/tony1')
def tony1():
    response = make_response(jsonify("Tonys UnJsonified Content"), 200)
    
    response.headers["TonyCustomHeader1"] = "mate"
    response.headers["TonyCustomHeader2"] = 420
    
    response.set_cookie("tonycookie1", "cookievalue")
    response.set_cookie("tonycookie2", "69")
    
    print()
    print(response.headers)
    print()
    print(response.get_data())
    print()
    
    debug_info = {
        "status":   response.status,
        "headers":  dict(response.headers),
        "body":     response.get_data(as_text=True),
        "cookies":  response.headers.getlist('Set-Cookie')
    }
    return jsonify(debug_info)



@app.route('/tony2')
def tony2():
    response = make_response(jsonify("Tonys Jsonified Content"), 200)
    # response = make_response("Tonys UnJsonified Content", 200)
    return response


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)