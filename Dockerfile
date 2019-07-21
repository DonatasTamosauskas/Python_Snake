FROM tensorflow/tensorflow:2.0.0b1-py3-jupyter

RUN pip install tensorlayer tensorflow-probability gym && pip install --upgrade tf-nightly-2.0-preview tfp-nightly && apt-get update && apt-get install -y python-opengl

