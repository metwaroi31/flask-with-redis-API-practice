from server import create_app


redis = Redis(host='redis', port=6379)

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
    # app.run(host="0.0.0.0", port=5000)
