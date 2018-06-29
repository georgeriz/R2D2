import requests

def get_get():
	r = requests.get('http://127.0.0.1:5000/api')
	return r.json()
	
if __name__ == "__main__":
	print get_get()