# We're using Ubuntu 20.10
FROM ximfine/remix:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b x-sql-extended https://github.com/Patrick489/lel_remake_UserBoto /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Patrick489/lel_remake_UserBoto/x-sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
