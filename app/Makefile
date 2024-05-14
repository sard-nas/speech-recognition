REVISION := $(shell git rev-parse --short HEAD)
DOCKER_IMAGE_NAME = cr.yandex/crprpurksmdr58vchrr/bezlepkin:$(REVISION)

build:
	docker build --platform linux/amd64 -t $(DOCKER_IMAGE_NAME) . --file .Dockerfile

push:
	docker push $(DOCKER_IMAGE_NAME)

run:
	docker run --rm -it --device /dev/snd:/dev/snd -p 8501:8501 $(DOCKER_IMAGE_NAME)
