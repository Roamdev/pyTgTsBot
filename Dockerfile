FROM python:3.12 as python-package

COPY requirements.txt /.
COPY bot.py /.
COPY currencies.py /.
COPY exchange_api.py /.
COPY template_text.py /.

RUN pip3 install -r requirements.txt

CMD ["python", "bot.py"]