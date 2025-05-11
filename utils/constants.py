log_file = 'vsearch.log'
directory = 'cati_666.txt'
dbconfig = {'host': '127.0.0.1',
           'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }


_SQL = """show tables"""
_SQL2 = """describe log"""
SQL3 = """insert into log
(phrase, letters, ip, browser_string, results)
values
(%s, %s, %s, %s, %s)""" # сюди будуть приходити данні від методу
SQl4 = """select * from log"""