install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py

format:
	black *.py

build:
	docker build -t k8s-flask-scaffold .

run:
	docker run -d -p 3000:3000 k8s-flask-scaffold:latest
