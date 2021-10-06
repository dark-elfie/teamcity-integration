deps:
	pip install -r requirements.txt
test:
	PYTHONPATH= pytest --alluredir=C:\Users\Sara\PycharmProjects\TMS_testy\report -m "not not_reusable"