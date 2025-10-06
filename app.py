from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask on Render</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: white;
                color: #333;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            }
            h1 { color: #667eea; }
            .status { 
                background: #4CAF50; 
                color: white; 
                padding: 10px; 
                border-radius: 5px;
                display: inline-block;
                margin: 10px 0;
            }
            button {
                background: #667eea;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                margin: 5px;
            }
            button:hover { background: #5568d3; }
            #result {
                margin-top: 20px;
                padding: 15px;
                background: #f5f5f5;
                border-radius: 5px;
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask App on Render</h1>
            <div class="status">✅ Ứng dụng đang chạy!</div>
            <p>Chúc mừng! Bạn đã deploy thành công Flask app lên Render.</p>
            
            <h3>Test API:</h3>
            <button onclick="testAPI()">Test API Endpoint</button>
            
            <div id="result"></div>
        </div>
        
        <script>
            function testAPI() {
                fetch('/api/hello')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('result').innerHTML = 
                            '<strong>API Response:</strong><br>' + 
                            JSON.stringify(data, null, 2);
                        document.getElementById('result').style.display = 'block';
                    });
            }
        </script>
    </body>
    </html>
    '''

@app.route('/api/hello')
def hello():
    return jsonify({
        'message': 'Hello from Flask API!',
        'status': 'success'
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)