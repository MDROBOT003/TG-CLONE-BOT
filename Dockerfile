FROM arata74/enc
COPY . .

RUN pip3 install -U -r requirements.txt

CMD ["bash", "start.sh"]
